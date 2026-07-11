# `nodes` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "access"
        src_backend_access_common_printtup_c["common/printtup.c"]
        src_backend_access_transam_parallel_c["transam/parallel.c"]
        src_backend_access_transam_transam_c["transam/transam.c"]
    end
    subgraph "catalog"
        src_backend_catalog_pg_class_c["pg_class.c"]
        src_backend_catalog_pg_collation_c["pg_collation.c"]
        src_backend_catalog_pg_proc_c["pg_proc.c"]
    end
    subgraph "commands"
        src_backend_commands_explain_state_c["explain_state.c"]
    end
    subgraph "common"
        src_common_hashfn_c["hashfn.c"]
        src_common_string_c["string.c"]
        src_common_stringinfo_c["stringinfo.c"]
    end
    subgraph "include/access"
        src_include_access_attnum_h["attnum.h"]
    end
    subgraph "include/common"
        src_include_common_shortest_dec_h["shortest_dec.h"]
    end
    subgraph "include/executor"
        src_include_executor_tuptable_h["tuptable.h"]
    end
    subgraph "include/lib"
        src_include_lib_simplehash_h["simplehash.h"]
    end
    subgraph "include/nodes"
        src_include_nodes_execnodes_h["execnodes.h"]
        src_include_nodes_nodes_h["nodes.h"]
        src_include_nodes_parsenodes_h["parsenodes.h"]
        src_include_nodes_pathnodes_h["pathnodes.h"]
        src_include_nodes_pg_list_h["pg_list.h"]
        src_include_nodes_plannodes_h["plannodes.h"]
        src_include_nodes_queryjumble_h["queryjumble.h"]
    end
    subgraph "include/parser"
        src_include_parser_parsetree_h["parsetree.h"]
        src_include_parser_scanner_h["scanner.h"]
    end
    subgraph "include/utils"
        src_include_utils_hsearch_h["hsearch.h"]
    end
    subgraph "nodes"
        src_backend_nodes_bitmapset_c["bitmapset.c"]
        src_backend_nodes_copyfuncs_c["copyfuncs.c"]
        src_backend_nodes_equalfuncs_c["equalfuncs.c"]
        src_backend_nodes_extensible_c["extensible.c"]
        src_backend_nodes_list_c["list.c"]
        src_backend_nodes_makefuncs_c["makefuncs.c"]
        src_backend_nodes_multibitmapset_c["multibitmapset.c"]
        src_backend_nodes_nodeFuncs_c["nodeFuncs.c"]
        src_backend_nodes_outfuncs_c["outfuncs.c"]
        src_backend_nodes_params_c["params.c"]
        src_backend_nodes_print_c["print.c"]
        src_backend_nodes_queryjumblefuncs_c["queryjumblefuncs.c"]
        src_backend_nodes_read_c["read.c"]
        src_backend_nodes_readfuncs_c["readfuncs.c"]
        src_backend_nodes_tidbitmap_c["tidbitmap.c"]
        src_backend_nodes_value_c["value.c"]
    end
    subgraph "parser"
        src_backend_parser_parse_node_c["parse_node.c"]
        src_backend_parser_scansup_c["scansup.c"]
    end
    subgraph "port"
        src_port_pg_bitutils_c["pg_bitutils.c"]
    end
    subgraph "storage"
        src_backend_storage_ipc_shmem_c["ipc/shmem.c"]
        src_backend_storage_lmgr_lwlock_c["lmgr/lwlock.c"]
        src_backend_storage_page_itemptr_c["page/itemptr.c"]
    end
    subgraph "utils"
        src_backend_utils_adt_datum_c["adt/datum.c"]
        src_backend_utils_adt_int_c["adt/int.c"]
        src_backend_utils_fmgr_fmgr_c["fmgr/fmgr.c"]
        src_backend_utils_mb_stringinfo_mb_c["mb/stringinfo_mb.c"]
        src_backend_utils_mmgr_dsa_c["mmgr/dsa.c"]
        src_backend_utils_mmgr_memdebug_c["mmgr/memdebug.c"]
    end
    src_backend_nodes_bitmapset_c --> src_common_hashfn_c
    src_backend_nodes_bitmapset_c --> src_include_nodes_nodes_h
    src_backend_nodes_bitmapset_c --> src_include_nodes_pg_list_h
    src_backend_nodes_bitmapset_c --> src_port_pg_bitutils_c
    src_backend_nodes_copyfuncs_c --> src_backend_utils_adt_datum_c
    src_backend_nodes_equalfuncs_c --> src_backend_utils_adt_datum_c
    src_backend_nodes_extensible_c --> src_backend_access_transam_parallel_c
    src_backend_nodes_extensible_c --> src_backend_commands_explain_state_c
    src_backend_nodes_extensible_c --> src_include_nodes_execnodes_h
    src_backend_nodes_extensible_c --> src_include_nodes_pathnodes_h
    src_backend_nodes_extensible_c --> src_include_nodes_plannodes_h
    src_backend_nodes_extensible_c --> src_include_utils_hsearch_h
    src_backend_nodes_list_c --> src_backend_utils_adt_int_c
    src_backend_nodes_list_c --> src_backend_utils_mmgr_memdebug_c
    src_backend_nodes_list_c --> src_include_nodes_pg_list_h
    src_backend_nodes_list_c --> src_port_pg_bitutils_c
    src_backend_nodes_makefuncs_c --> src_backend_catalog_pg_class_c
    src_backend_nodes_makefuncs_c --> src_backend_nodes_nodeFuncs_c
    src_backend_nodes_makefuncs_c --> src_include_nodes_execnodes_h
    src_backend_nodes_makefuncs_c --> src_include_nodes_parsenodes_h
    src_backend_nodes_multibitmapset_c --> src_backend_nodes_bitmapset_c
    src_backend_nodes_multibitmapset_c --> src_include_nodes_pg_list_h
    src_backend_nodes_nodeFuncs_c --> src_backend_catalog_pg_collation_c
    src_backend_nodes_nodeFuncs_c --> src_include_nodes_execnodes_h
    src_backend_nodes_nodeFuncs_c --> src_include_nodes_parsenodes_h
    src_backend_nodes_nodeFuncs_c --> src_include_nodes_pathnodes_h
    src_backend_nodes_outfuncs_c --> src_backend_nodes_bitmapset_c
    src_backend_nodes_outfuncs_c --> src_backend_utils_adt_datum_c
    src_backend_nodes_outfuncs_c --> src_common_stringinfo_c
    src_backend_nodes_outfuncs_c --> src_include_access_attnum_h
    src_backend_nodes_outfuncs_c --> src_include_common_shortest_dec_h
    src_backend_nodes_outfuncs_c --> src_include_nodes_nodes_h
    src_backend_nodes_outfuncs_c --> src_include_nodes_pg_list_h
    src_backend_nodes_params_c --> src_backend_parser_parse_node_c
    src_backend_nodes_params_c --> src_backend_storage_ipc_shmem_c
    src_backend_nodes_params_c --> src_backend_utils_adt_datum_c
    src_backend_nodes_params_c --> src_backend_utils_fmgr_fmgr_c
    src_backend_nodes_params_c --> src_backend_utils_mb_stringinfo_mb_c
    src_backend_nodes_print_c --> src_backend_access_common_printtup_c
    src_backend_nodes_print_c --> src_backend_nodes_nodeFuncs_c
    src_backend_nodes_print_c --> src_common_stringinfo_c
    src_backend_nodes_print_c --> src_include_executor_tuptable_h
    src_backend_nodes_print_c --> src_include_nodes_pathnodes_h
    src_backend_nodes_print_c --> src_include_parser_parsetree_h
    src_backend_nodes_queryjumblefuncs_c --> src_backend_access_transam_transam_c
    src_backend_nodes_queryjumblefuncs_c --> src_backend_catalog_pg_proc_c
    src_backend_nodes_queryjumblefuncs_c --> src_backend_nodes_nodeFuncs_c
    src_backend_nodes_queryjumblefuncs_c --> src_backend_parser_scansup_c
    src_backend_nodes_queryjumblefuncs_c --> src_backend_utils_adt_int_c
    src_backend_nodes_queryjumblefuncs_c --> src_common_hashfn_c
    src_backend_nodes_queryjumblefuncs_c --> src_include_nodes_queryjumble_h
    src_backend_nodes_queryjumblefuncs_c --> src_include_parser_scanner_h
    src_backend_nodes_read_c --> src_backend_nodes_bitmapset_c
    src_backend_nodes_read_c --> src_backend_nodes_readfuncs_c
    src_backend_nodes_read_c --> src_backend_nodes_value_c
    src_backend_nodes_read_c --> src_common_string_c
    src_backend_nodes_read_c --> src_include_nodes_pg_list_h
    src_backend_nodes_readfuncs_c --> src_backend_nodes_bitmapset_c
    src_backend_nodes_readfuncs_c --> src_include_nodes_nodes_h
    src_backend_nodes_tidbitmap_c --> src_backend_nodes_bitmapset_c
    src_backend_nodes_tidbitmap_c --> src_backend_storage_lmgr_lwlock_c
    src_backend_nodes_tidbitmap_c --> src_backend_storage_page_itemptr_c
    src_backend_nodes_tidbitmap_c --> src_backend_utils_adt_int_c
    src_backend_nodes_tidbitmap_c --> src_backend_utils_mmgr_dsa_c
    src_backend_nodes_tidbitmap_c --> src_common_hashfn_c
    src_backend_nodes_tidbitmap_c --> src_include_lib_simplehash_h
    src_backend_nodes_value_c --> src_include_nodes_nodes_h
```
