# `bootstrap` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "access"
        src_backend_access_common_toast_compression_c["common/toast_compression.c"]
        src_backend_access_heap_heapam_c["heap/heapam.c"]
        src_backend_access_index_genam_c["index/genam.c"]
        src_backend_access_table_tableam_c["table/tableam.c"]
    end
    subgraph "bootstrap"
        src_backend_bootstrap_bootstrap_c["bootstrap.c"]
    end
    subgraph "catalog"
        src_backend_catalog_index_c["index.c"]
        src_backend_catalog_pg_collation_c["pg_collation.c"]
        src_backend_catalog_pg_proc_c["pg_proc.c"]
    end
    subgraph "common"
        src_common_link_canary_c["link-canary.c"]
    end
    subgraph "include/catalog"
        src_include_catalog_pg_attribute_h["pg_attribute.h"]
        src_include_catalog_pg_authid_h["pg_authid.h"]
    end
    subgraph "include/nodes"
        src_include_nodes_execnodes_h["execnodes.h"]
        src_include_nodes_parsenodes_h["parsenodes.h"]
    end
    subgraph "include/port"
        src_include_port_win32_msvc_unistd_h["win32_msvc/unistd.h"]
    end
    subgraph "include/storage"
        src_include_storage_shmem_internal_h["shmem_internal.h"]
    end
    subgraph "nodes"
        src_backend_nodes_makefuncs_c["makefuncs.c"]
    end
    subgraph "port"
        src_port_pg_getopt_ctx_c["pg_getopt_ctx.c"]
    end
    subgraph "postmaster"
        src_backend_postmaster_postmaster_c["postmaster.c"]
    end
    subgraph "storage"
        src_backend_storage_file_fd_c["file/fd.c"]
        src_backend_storage_ipc_ipc_c["ipc/ipc.c"]
        src_backend_storage_lmgr_proc_c["lmgr/proc.c"]
        src_backend_storage_page_bufpage_c["page/bufpage.c"]
        src_backend_storage_page_checksum_c["page/checksum.c"]
    end
    subgraph "utils"
        src_backend_utils_cache_relmapper_c["cache/relmapper.c"]
        src_backend_utils_misc_guc_c["misc/guc.c"]
    end
    src_backend_bootstrap_bootstrap_c --> src_backend_access_common_toast_compression_c
    src_backend_bootstrap_bootstrap_c --> src_backend_access_heap_heapam_c
    src_backend_bootstrap_bootstrap_c --> src_backend_access_index_genam_c
    src_backend_bootstrap_bootstrap_c --> src_backend_access_table_tableam_c
    src_backend_bootstrap_bootstrap_c --> src_backend_catalog_index_c
    src_backend_bootstrap_bootstrap_c --> src_backend_catalog_pg_collation_c
    src_backend_bootstrap_bootstrap_c --> src_backend_catalog_pg_proc_c
    src_backend_bootstrap_bootstrap_c --> src_backend_nodes_makefuncs_c
    src_backend_bootstrap_bootstrap_c --> src_backend_postmaster_postmaster_c
    src_backend_bootstrap_bootstrap_c --> src_backend_storage_file_fd_c
    src_backend_bootstrap_bootstrap_c --> src_backend_storage_ipc_ipc_c
    src_backend_bootstrap_bootstrap_c --> src_backend_storage_lmgr_proc_c
    src_backend_bootstrap_bootstrap_c --> src_backend_storage_page_bufpage_c
    src_backend_bootstrap_bootstrap_c --> src_backend_storage_page_checksum_c
    src_backend_bootstrap_bootstrap_c --> src_backend_utils_cache_relmapper_c
    src_backend_bootstrap_bootstrap_c --> src_backend_utils_misc_guc_c
    src_backend_bootstrap_bootstrap_c --> src_common_link_canary_c
    src_backend_bootstrap_bootstrap_c --> src_include_catalog_pg_attribute_h
    src_backend_bootstrap_bootstrap_c --> src_include_catalog_pg_authid_h
    src_backend_bootstrap_bootstrap_c --> src_include_nodes_execnodes_h
    src_backend_bootstrap_bootstrap_c --> src_include_nodes_parsenodes_h
    src_backend_bootstrap_bootstrap_c --> src_include_port_win32_msvc_unistd_h
    src_backend_bootstrap_bootstrap_c --> src_include_storage_shmem_internal_h
    src_backend_bootstrap_bootstrap_c --> src_port_pg_getopt_ctx_c
```
