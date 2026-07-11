# `lib` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "common"
        src_common_hashfn_c["hashfn.c"]
        src_common_stringinfo_c["stringinfo.c"]
    end
    subgraph "lib"
        src_backend_lib_bloomfilter_c["bloomfilter.c"]
        src_backend_lib_dshash_c["dshash.c"]
        src_backend_lib_hyperloglog_c["hyperloglog.c"]
        src_backend_lib_knapsack_c["knapsack.c"]
        src_backend_lib_pairingheap_c["pairingheap.c"]
    end
    subgraph "nodes"
        src_backend_nodes_bitmapset_c["bitmapset.c"]
    end
    subgraph "port"
        src_port_pg_bitutils_c["pg_bitutils.c"]
    end
    subgraph "storage"
        src_backend_storage_lmgr_lwlock_c["lmgr/lwlock.c"]
    end
    subgraph "utils"
        src_backend_utils_mmgr_dsa_c["mmgr/dsa.c"]
    end
    src_backend_lib_bloomfilter_c --> src_common_hashfn_c
    src_backend_lib_bloomfilter_c --> src_port_pg_bitutils_c
    src_backend_lib_dshash_c --> src_backend_storage_lmgr_lwlock_c
    src_backend_lib_dshash_c --> src_backend_utils_mmgr_dsa_c
    src_backend_lib_dshash_c --> src_common_hashfn_c
    src_backend_lib_hyperloglog_c --> src_port_pg_bitutils_c
    src_backend_lib_knapsack_c --> src_backend_nodes_bitmapset_c
    src_backend_lib_pairingheap_c --> src_common_stringinfo_c
```
