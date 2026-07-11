#!/usr/bin/env python3
"""Generate Mermaid dependency diagrams for the postgres backend executable.

Scope: the source files linked into the `postgres` server binary --
src/backend/**, plus the server-side parts of src/common, src/port and
src/timezone.  Frontend programs, contrib modules, libpq etc. are ignored.

A header (.h) that has a "corresponding" .c file (same module) is merged
into that .c file's node, so an #include of the header counts as a
dependency on the module.  Headers without a corresponding .c file (e.g.
the generated catalog headers) appear as their own nodes.

Outputs (in this directory):
  README.md          - overview diagram (subsystem level) + notes
  <subsystem>.md     - file-level diagrams per backend subsystem

Run from the repository root:  python3 dependency-diagrams/generate.py
"""

import os
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dependency-diagrams"

INCLUDE_RE = re.compile(r'^\s*#\s*include\s*[<"]([^">]+)[">]', re.M)

# src/common files that are only linked into frontend programs
COMMON_FRONTEND_ONLY = {
    "fe_memutils.c", "restricted_token.c", "sprompt.c", "logging.c",
}

# Modules included by a huge share of the tree; drawing their edges would
# turn every diagram black.  They are omitted from the diagrams and listed
# in the README instead.  (Computed below by in-degree threshold.)
HUB_THRESHOLD = 130   # modules with more than this many dependents are hubs

# Maximum edges per emitted mermaid block; bigger diagrams are split.
# (GitHub's Mermaid config allows 500 edges / 50000 chars per diagram.)
MAX_EDGES = 300


def collect_sources():
    """Return the set of .c files linked into the postgres binary."""
    cfiles = set()
    for sub in ("backend", "timezone", "port", "common"):
        for p in (ROOT / "src" / sub).rglob("*.c"):
            rel = p.relative_to(ROOT)
            if sub == "common" and p.name in COMMON_FRONTEND_ONLY:
                continue
            if "win32" in str(rel):  # not built on the primary platforms
                continue
            cfiles.add(rel)
    return cfiles


def collect_headers():
    hfiles = set()
    for sub in ("include", "backend", "timezone", "port", "common"):
        for p in (ROOT / "src" / sub).rglob("*.h"):
            hfiles.add(p.relative_to(ROOT))
    return hfiles


def build_module_map(cfiles, hfiles):
    """Map every file to its module node.  A module is named after its .c
    file; a header with a corresponding .c is merged into that module."""
    module_of = {}
    for c in cfiles:
        module_of[c] = c

    # index .c files by stem for the fallback rule
    by_stem = defaultdict(list)
    for c in cfiles:
        by_stem[c.stem].append(c)

    for h in hfiles:
        cand = []
        # rule 1: same directory, same stem
        same_dir = h.with_suffix(".c")
        if same_dir in cfiles:
            cand.append(same_dir)
        # rule 2: src/include/<rel>.h <-> src/backend/<rel>.c or src/<rel>.c
        parts = h.parts
        if not cand and parts[:2] == ("src", "include"):
            rel = Path(*parts[2:]).with_suffix(".c")
            for base in ("src/backend", "src"):
                c = Path(base) / rel
                if c in cfiles:
                    cand.append(c)
                    break
        # rule 3: unique stem match anywhere in the binary
        if not cand and len(by_stem.get(h.stem, [])) == 1:
            cand.append(by_stem[h.stem][0])
        module_of[h] = cand[0] if cand else h
    return module_of


def build_include_index(files):
    """Map include-path suffixes to repo files for resolution."""
    by_suffix = defaultdict(list)
    for f in files:
        s = str(f)
        parts = f.parts
        for i in range(len(parts)):
            by_suffix["/".join(parts[i:])].append(f)
    return by_suffix


def resolve(inc, includer, all_files, by_suffix):
    """Resolve an #include string to a repo file (or None if external)."""
    # relative to the including file's directory
    local = (includer.parent / inc)
    try:
        local = Path(os.path.normpath(local))
    except ValueError:
        return None
    if local in all_files:
        return local
    si = Path("src/include") / inc
    if si in all_files:
        return si
    hits = by_suffix.get(inc, [])
    if len(hits) == 1:
        return hits[0]
    return None


def subsystem_of(module):
    """Human grouping: backend/<dir>, common, port, timezone, include/<dir>."""
    p = module.parts
    if p[:2] == ("src", "backend"):
        return p[2] if len(p) > 3 else "backend-top"
    if p[:2] == ("src", "include"):
        return "include/" + (p[2] if len(p) > 3 else "top")
    return p[1]  # common, port, timezone

def node_id(module):
    return re.sub(r"[^A-Za-z0-9]", "_", str(module))


def label(module):
    """Short display label: path below the subsystem directory."""
    p = module.parts
    if p[:2] == ("src", "backend"):
        return "/".join(p[3:]) if len(p) > 3 else p[-1]
    if p[:2] == ("src", "include"):
        return "/".join(p[3:]) if len(p) > 3 else p[-1]
    return "/".join(p[2:])


def main():
    cfiles = collect_sources()
    hfiles = collect_headers()
    all_files = cfiles | hfiles
    module_of = build_module_map(cfiles, hfiles)
    by_suffix = build_include_index(all_files)

    # module -> set of modules it depends on
    deps = defaultdict(set)
    files_of = defaultdict(set)
    for f, m in module_of.items():
        files_of[m].add(f)
    for f in sorted(all_files):
        src = module_of[f]
        try:
            text = (ROOT / f).read_text(errors="replace")
        except OSError:
            continue
        for inc in INCLUDE_RE.findall(text):
            t = resolve(inc, f, all_files, by_suffix)
            if t is None:
                continue
            dst = module_of[t]
            if dst != src:
                deps[src].add(dst)

    # keep only modules reachable in the binary: all .c modules plus any
    # header-only module referenced by them
    modules = set(module_of[c] for c in cfiles)
    referenced_headers = set()
    for m in modules:
        for d in deps[m]:
            if d not in modules:
                referenced_headers.add(d)
    keep = modules | referenced_headers
    deps = {m: {d for d in deps[m] if d in keep} for m in keep}

    # in-degree -> hubs
    indeg = defaultdict(int)
    for m, ds in deps.items():
        for d in ds:
            indeg[d] += 1
    hubs = {m for m, n in indeg.items() if n > HUB_THRESHOLD}

    OUT.mkdir(exist_ok=True)
    write_overview(deps, keep, hubs, indeg)
    subsystems = sorted({subsystem_of(m) for m in modules
                         if subsystem_of(m).split("/")[0] != "include"})
    for ss in subsystems:
        write_subsystem(ss, deps, keep, hubs)
    print(f"{len(keep)} modules, "
          f"{sum(len(v) for v in deps.values())} edges, "
          f"{len(hubs)} hubs, {len(subsystems)} subsystem pages")


def write_overview(deps, keep, hubs, indeg):
    # fold "include/X" header-only groups into backend subsystem X, so the
    # overview shows one node per subsystem
    backend_ss = {subsystem_of(m) for m in keep
                  if m.parts[:2] == ("src", "backend")}

    def fold(m):
        s = subsystem_of(m)
        if s.startswith("include/"):
            base = s.split("/", 1)[1]
            return base if base in backend_ss else "include (other)"
        return s

    agg = defaultdict(set)
    for m, ds in deps.items():
        s = fold(m)
        for d in ds:
            t = fold(d)
            if t != s:
                agg[s].add(t)
    lines = ["# PostgreSQL backend (`postgres` binary) dependency diagrams",
             "",
             "Generated by [`generate.py`](generate.py) from the `#include`",
             "graph of the sources linked into the `postgres` server",
             "executable (`src/backend`, `src/common`, `src/port`,",
             "`src/timezone`).  Headers are folded into their corresponding",
             "`.c` file, so each node is a *module*; headers without a `.c`",
             "(e.g. generated catalog headers) appear as their own nodes.",
             "",
             "## Subsystem overview",
             "",
             "An arrow `A --> B` means at least one file in `A` includes a",
             "file belonging to `B`.",
             "",
             "```mermaid",
             "graph LR"]
    for s in sorted(agg):
        for t in sorted(agg[s]):
            lines.append(f'    {node_id(Path(s))}["{s}"] --> {node_id(Path(t))}["{t}"]')
    lines.append("```")
    lines += ["",
              "## Ubiquitous modules (omitted from the diagrams)",
              "",
              f"These modules are depended on by more than {HUB_THRESHOLD}",
              "other modules; drawing their edges would make every diagram",
              "unreadable, so they are left out:",
              ""]
    for h in sorted(hubs, key=lambda m: -indeg[m]):
        lines.append(f"- `{h}` ({indeg[h]} dependents)")
    lines += ["",
              "## File-level diagrams",
              ""]
    for ss in sorted({subsystem_of(m) for m in keep
                      if subsystem_of(m).split("/")[0] != "include"
                      and str(m).endswith(".c")}):
        lines.append(f"- [{ss}]({ss.replace('/', '_')}.md)")
    lines.append("")
    (OUT / "README.md").write_text("\n".join(lines))


def mermaid_block(edges, groups, out):
    """Emit one mermaid graph; groups maps subgraph title -> node set."""
    out.append("```mermaid")
    out.append("graph LR")
    nodes = set()
    for a, b in edges:
        nodes.add(a); nodes.add(b)
    for title in sorted(groups):
        members = [n for n in sorted(groups[title]) if n in nodes]
        if not members:
            continue
        out.append(f'    subgraph "{title}"')
        for n in members:
            out.append(f'        {node_id(n)}["{label(n)}"]')
        out.append("    end")
    grouped = set().union(*groups.values()) if groups else set()
    for n in sorted(nodes - grouped):
        out.append(f'    {node_id(n)}["{label(n)}"]')
    for a, b in sorted(edges):
        out.append(f"    {node_id(a)} --> {node_id(b)}")
    out.append("```")
    out.append("")


def write_subsystem(ss, deps, keep, hubs):
    members = sorted(m for m in keep if subsystem_of(m) == ss)
    member_set = set(members)
    internal, external = [], []
    for m in members:
        for d in sorted(deps.get(m, ())):
            if d in hubs:
                continue
            (internal if d in member_set else external).append((m, d))

    out = [f"# `{ss}` — file-level dependencies",
           "",
           "Arrows point from the file that does the `#include` to the file",
           "it needs.  Ubiquitous modules (see [README](README.md)) are",
           "omitted.  Node names are relative to the subsystem directory;",
           "external nodes are grouped by their subsystem.",
           ""]

    def ext_groups(edges):
        g = defaultdict(set)
        for _, d in edges:
            if d not in member_set:
                g[subsystem_of(d)].add(d)
        return g

    if len(internal) + len(external) <= MAX_EDGES:
        out.append("## All dependencies")
        out.append("")
        mermaid_block(internal + external,
                      {ss: member_set, **ext_groups(external)}, out)
    else:
        # split: internal structure first, then per-subdirectory externals
        out.append("## Internal structure")
        out.append("")
        bydir = defaultdict(set)
        for m in members:
            bydir["/".join(m.parts[3:-1]) or "."].add(m)
        if len(internal) <= MAX_EDGES:
            mermaid_block(internal, dict(bydir), out)
        else:
            for sd in sorted(bydir):
                edges = [(m, d) for m, d in internal
                         if ("/".join(m.parts[3:-1]) or ".") == sd]
                if not edges:
                    continue
                out.append(f"### from `{sd or '.'}`")
                out.append("")
                for i in range(0, len(edges), MAX_EDGES):
                    mermaid_block(edges[i:i + MAX_EDGES], dict(bydir), out)
        out.append("## External dependencies")
        out.append("")
        subdirs = sorted({"/".join(m.parts[:-1]) for m, _ in external})
        for sd in subdirs:
            edges = [(m, d) for m, d in external
                     if "/".join(m.parts[:-1]) == sd]
            if not edges:
                continue
            out.append(f"### `{sd}`")
            out.append("")
            for i in range(0, len(edges), MAX_EDGES):
                chunk = edges[i:i + MAX_EDGES]
                mermaid_block(chunk, {sd: {m for m, _ in chunk},
                                      **ext_groups(chunk)}, out)
    (OUT / f"{ss.replace('/', '_')}.md").write_text("\n".join(out))


if __name__ == "__main__":
    main()
