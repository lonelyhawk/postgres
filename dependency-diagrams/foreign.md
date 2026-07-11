# `foreign` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "access"
        src_backend_access_common_reloptions_c["common/reloptions.c"]
    end
    subgraph "foreign"
        src_backend_foreign_foreign_c["foreign.c"]
    end
    subgraph "include/catalog"
        src_include_catalog_pg_foreign_data_wrapper_h["pg_foreign_data_wrapper.h"]
        src_include_catalog_pg_foreign_server_h["pg_foreign_server.h"]
        src_include_catalog_pg_foreign_table_h["pg_foreign_table.h"]
        src_include_catalog_pg_user_mapping_h["pg_user_mapping.h"]
    end
    subgraph "include/foreign"
        src_include_foreign_fdwapi_h["fdwapi.h"]
    end
    subgraph "include/nodes"
        src_include_nodes_parsenodes_h["parsenodes.h"]
    end
    subgraph "include/optimizer"
        src_include_optimizer_paths_h["paths.h"]
    end
    subgraph "include/tcop"
        src_include_tcop_tcopprot_h["tcopprot.h"]
    end
    subgraph "utils"
        src_backend_utils_adt_varlena_c["adt/varlena.c"]
        src_backend_utils_fmgr_funcapi_c["fmgr/funcapi.c"]
        src_backend_utils_sort_tuplestore_c["sort/tuplestore.c"]
    end
    src_backend_foreign_foreign_c --> src_backend_access_common_reloptions_c
    src_backend_foreign_foreign_c --> src_backend_utils_adt_varlena_c
    src_backend_foreign_foreign_c --> src_backend_utils_fmgr_funcapi_c
    src_backend_foreign_foreign_c --> src_backend_utils_sort_tuplestore_c
    src_backend_foreign_foreign_c --> src_include_catalog_pg_foreign_data_wrapper_h
    src_backend_foreign_foreign_c --> src_include_catalog_pg_foreign_server_h
    src_backend_foreign_foreign_c --> src_include_catalog_pg_foreign_table_h
    src_backend_foreign_foreign_c --> src_include_catalog_pg_user_mapping_h
    src_backend_foreign_foreign_c --> src_include_foreign_fdwapi_h
    src_backend_foreign_foreign_c --> src_include_nodes_parsenodes_h
    src_backend_foreign_foreign_c --> src_include_optimizer_paths_h
    src_backend_foreign_foreign_c --> src_include_tcop_tcopprot_h
```
