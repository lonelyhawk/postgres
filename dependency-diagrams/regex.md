# `regex` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "catalog"
        src_backend_catalog_pg_collation_c["pg_collation.c"]
    end
    subgraph "common"
        src_common_unicode_case_c["unicode_case.c"]
        src_common_unicode_category_c["unicode_category.c"]
    end
    subgraph "include/regex"
        src_include_regex_regerrs_h["regerrs.h"]
        src_include_regex_regex_h["regex.h"]
        src_include_regex_regguts_h["regguts.h"]
    end
    subgraph "include/utils"
        src_include_utils_pg_locale_c_h["pg_locale_c.h"]
    end
    subgraph "regex"
        src_backend_regex_regc_color_c["regc_color.c"]
        src_backend_regex_regc_cvec_c["regc_cvec.c"]
        src_backend_regex_regc_lex_c["regc_lex.c"]
        src_backend_regex_regc_locale_c["regc_locale.c"]
        src_backend_regex_regc_nfa_c["regc_nfa.c"]
        src_backend_regex_regc_pg_locale_c["regc_pg_locale.c"]
        src_backend_regex_regcomp_c["regcomp.c"]
        src_backend_regex_rege_dfa_c["rege_dfa.c"]
        src_backend_regex_regerror_c["regerror.c"]
        src_backend_regex_regexec_c["regexec.c"]
        src_backend_regex_regexport_c["regexport.c"]
        src_backend_regex_regfree_c["regfree.c"]
        src_backend_regex_regprefix_c["regprefix.c"]
    end
    subgraph "utils"
        src_backend_utils_adt_pg_locale_c["adt/pg_locale.c"]
    end
    src_backend_regex_regc_pg_locale_c --> src_backend_catalog_pg_collation_c
    src_backend_regex_regc_pg_locale_c --> src_backend_utils_adt_pg_locale_c
    src_backend_regex_regc_pg_locale_c --> src_common_unicode_case_c
    src_backend_regex_regc_pg_locale_c --> src_common_unicode_category_c
    src_backend_regex_regc_pg_locale_c --> src_include_utils_pg_locale_c_h
    src_backend_regex_regcomp_c --> src_backend_regex_regc_color_c
    src_backend_regex_regcomp_c --> src_backend_regex_regc_cvec_c
    src_backend_regex_regcomp_c --> src_backend_regex_regc_lex_c
    src_backend_regex_regcomp_c --> src_backend_regex_regc_locale_c
    src_backend_regex_regcomp_c --> src_backend_regex_regc_nfa_c
    src_backend_regex_regcomp_c --> src_backend_regex_regc_pg_locale_c
    src_backend_regex_regcomp_c --> src_include_regex_regguts_h
    src_backend_regex_regerror_c --> src_include_regex_regerrs_h
    src_backend_regex_regerror_c --> src_include_regex_regguts_h
    src_backend_regex_regexec_c --> src_backend_regex_rege_dfa_c
    src_backend_regex_regexec_c --> src_include_regex_regguts_h
    src_backend_regex_regexport_c --> src_include_regex_regex_h
    src_backend_regex_regexport_c --> src_include_regex_regguts_h
    src_backend_regex_regfree_c --> src_include_regex_regguts_h
    src_backend_regex_regprefix_c --> src_include_regex_regguts_h
```
