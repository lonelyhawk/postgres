# `statistics` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "access"
        src_backend_access_common_detoast_c["common/detoast.c"]
        src_backend_access_heap_heapam_c["heap/heapam.c"]
        src_backend_access_index_genam_c["index/genam.c"]
        src_backend_access_table_table_c["table/table.c"]
    end
    subgraph "catalog"
        src_backend_catalog_index_c["index.c"]
        src_backend_catalog_indexing_c["indexing.c"]
        src_backend_catalog_namespace_c["namespace.c"]
        src_backend_catalog_pg_class_c["pg_class.c"]
        src_backend_catalog_pg_collation_c["pg_collation.c"]
        src_backend_catalog_pg_operator_c["pg_operator.c"]
    end
    subgraph "include/access"
        src_include_access_attnum_h["attnum.h"]
        src_include_access_relation_h["relation.h"]
    end
    subgraph "include/catalog"
        src_include_catalog_pg_database_h["pg_database.h"]
        src_include_catalog_pg_statistic_h["pg_statistic.h"]
        src_include_catalog_pg_statistic_ext_h["pg_statistic_ext.h"]
        src_include_catalog_pg_statistic_ext_data_h["pg_statistic_ext_data.h"]
    end
    subgraph "include/commands"
        src_include_commands_defrem_h["defrem.h"]
        src_include_commands_progress_h["progress.h"]
    end
    subgraph "include/executor"
        src_include_executor_executor_h["executor.h"]
    end
    subgraph "include/optimizer"
        src_include_optimizer_optimizer_h["optimizer.h"]
    end
    subgraph "include/parser"
        src_include_parser_parsetree_h["parsetree.h"]
    end
    subgraph "include/statistics"
        src_include_statistics_extended_stats_internal_h["extended_stats_internal.h"]
        src_include_statistics_statistics_h["statistics.h"]
    end
    subgraph "include/top"
        src_include_varatt_h["varatt.h"]
    end
    subgraph "include/utils"
        src_include_utils_array_h["array.h"]
    end
    subgraph "nodes"
        src_backend_nodes_makefuncs_c["makefuncs.c"]
        src_backend_nodes_nodeFuncs_c["nodeFuncs.c"]
    end
    subgraph "optimizer"
        src_backend_optimizer_util_clauses_c["util/clauses.c"]
    end
    subgraph "postmaster"
        src_backend_postmaster_autovacuum_c["autovacuum.c"]
    end
    subgraph "rewrite"
        src_backend_rewrite_rewriteHandler_c["rewriteHandler.c"]
    end
    subgraph "statistics"
        src_backend_statistics_attribute_stats_c["attribute_stats.c"]
        src_backend_statistics_dependencies_c["dependencies.c"]
        src_backend_statistics_extended_stats_c["extended_stats.c"]
        src_backend_statistics_extended_stats_funcs_c["extended_stats_funcs.c"]
        src_backend_statistics_mcv_c["mcv.c"]
        src_backend_statistics_mvdistinct_c["mvdistinct.c"]
        src_backend_statistics_relation_stats_c["relation_stats.c"]
        src_backend_statistics_stat_utils_c["stat_utils.c"]
    end
    subgraph "storage"
        src_backend_storage_lmgr_lmgr_c["lmgr/lmgr.c"]
    end
    subgraph "utils"
        src_backend_utils_adt_acl_c["adt/acl.c"]
        src_backend_utils_adt_datum_c["adt/datum.c"]
        src_backend_utils_adt_jsonb_c["adt/jsonb.c"]
        src_backend_utils_adt_selfuncs_c["adt/selfuncs.c"]
        src_backend_utils_cache_attoptcache_c["cache/attoptcache.c"]
        src_backend_utils_cache_typcache_c["cache/typcache.c"]
        src_backend_utils_fmgr_fmgr_c["fmgr/fmgr.c"]
        src_backend_utils_fmgr_funcapi_c["fmgr/funcapi.c"]
    end
    src_backend_statistics_attribute_stats_c --> src_backend_access_heap_heapam_c
    src_backend_statistics_attribute_stats_c --> src_backend_catalog_indexing_c
    src_backend_statistics_attribute_stats_c --> src_backend_catalog_namespace_c
    src_backend_statistics_attribute_stats_c --> src_backend_catalog_pg_operator_c
    src_backend_statistics_attribute_stats_c --> src_backend_nodes_makefuncs_c
    src_backend_statistics_attribute_stats_c --> src_backend_statistics_stat_utils_c
    src_backend_statistics_attribute_stats_c --> src_include_statistics_statistics_h
    src_backend_statistics_attribute_stats_c --> src_include_utils_array_h
    src_backend_statistics_dependencies_c --> src_backend_nodes_nodeFuncs_c
    src_backend_statistics_dependencies_c --> src_backend_optimizer_util_clauses_c
    src_backend_statistics_dependencies_c --> src_backend_utils_adt_selfuncs_c
    src_backend_statistics_dependencies_c --> src_backend_utils_cache_typcache_c
    src_backend_statistics_dependencies_c --> src_include_catalog_pg_statistic_ext_h
    src_backend_statistics_dependencies_c --> src_include_catalog_pg_statistic_ext_data_h
    src_backend_statistics_dependencies_c --> src_include_optimizer_optimizer_h
    src_backend_statistics_dependencies_c --> src_include_parser_parsetree_h
    src_backend_statistics_dependencies_c --> src_include_statistics_extended_stats_internal_h
    src_backend_statistics_extended_stats_c --> src_backend_access_common_detoast_c
    src_backend_statistics_extended_stats_c --> src_backend_access_index_genam_c
    src_backend_statistics_extended_stats_c --> src_backend_access_table_table_c
    src_backend_statistics_extended_stats_c --> src_backend_catalog_indexing_c
    src_backend_statistics_extended_stats_c --> src_backend_nodes_nodeFuncs_c
    src_backend_statistics_extended_stats_c --> src_backend_postmaster_autovacuum_c
    src_backend_statistics_extended_stats_c --> src_backend_rewrite_rewriteHandler_c
    src_backend_statistics_extended_stats_c --> src_backend_utils_adt_acl_c
    src_backend_statistics_extended_stats_c --> src_backend_utils_adt_datum_c
    src_backend_statistics_extended_stats_c --> src_backend_utils_adt_selfuncs_c
    src_backend_statistics_extended_stats_c --> src_backend_utils_cache_attoptcache_c
    src_backend_statistics_extended_stats_c --> src_include_catalog_pg_statistic_ext_h
    src_backend_statistics_extended_stats_c --> src_include_catalog_pg_statistic_ext_data_h
    src_backend_statistics_extended_stats_c --> src_include_commands_defrem_h
    src_backend_statistics_extended_stats_c --> src_include_commands_progress_h
    src_backend_statistics_extended_stats_c --> src_include_executor_executor_h
    src_backend_statistics_extended_stats_c --> src_include_optimizer_optimizer_h
    src_backend_statistics_extended_stats_c --> src_include_parser_parsetree_h
    src_backend_statistics_extended_stats_c --> src_include_statistics_extended_stats_internal_h
    src_backend_statistics_extended_stats_c --> src_include_statistics_statistics_h
    src_backend_statistics_extended_stats_c --> src_include_utils_array_h
    src_backend_statistics_extended_stats_funcs_c --> src_backend_access_heap_heapam_c
    src_backend_statistics_extended_stats_funcs_c --> src_backend_catalog_indexing_c
    src_backend_statistics_extended_stats_funcs_c --> src_backend_catalog_namespace_c
    src_backend_statistics_extended_stats_funcs_c --> src_backend_catalog_pg_operator_c
    src_backend_statistics_extended_stats_funcs_c --> src_backend_nodes_makefuncs_c
    src_backend_statistics_extended_stats_funcs_c --> src_backend_nodes_nodeFuncs_c
    src_backend_statistics_extended_stats_funcs_c --> src_backend_statistics_stat_utils_c
    src_backend_statistics_extended_stats_funcs_c --> src_backend_utils_adt_acl_c
    src_backend_statistics_extended_stats_funcs_c --> src_backend_utils_adt_jsonb_c
    src_backend_statistics_extended_stats_funcs_c --> src_backend_utils_cache_typcache_c
    src_backend_statistics_extended_stats_funcs_c --> src_include_catalog_pg_database_h
    src_backend_statistics_extended_stats_funcs_c --> src_include_catalog_pg_statistic_ext_h
    src_backend_statistics_extended_stats_funcs_c --> src_include_catalog_pg_statistic_ext_data_h
    src_backend_statistics_extended_stats_funcs_c --> src_include_optimizer_optimizer_h
    src_backend_statistics_extended_stats_funcs_c --> src_include_statistics_extended_stats_internal_h
    src_backend_statistics_extended_stats_funcs_c --> src_include_utils_array_h
    src_backend_statistics_mcv_c --> src_backend_nodes_nodeFuncs_c
    src_backend_statistics_mcv_c --> src_backend_utils_adt_selfuncs_c
    src_backend_statistics_mcv_c --> src_backend_utils_cache_typcache_c
    src_backend_statistics_mcv_c --> src_backend_utils_fmgr_fmgr_c
    src_backend_statistics_mcv_c --> src_backend_utils_fmgr_funcapi_c
    src_backend_statistics_mcv_c --> src_include_catalog_pg_statistic_ext_h
    src_backend_statistics_mcv_c --> src_include_catalog_pg_statistic_ext_data_h
    src_backend_statistics_mcv_c --> src_include_statistics_extended_stats_internal_h
    src_backend_statistics_mcv_c --> src_include_statistics_statistics_h
    src_backend_statistics_mcv_c --> src_include_utils_array_h
    src_backend_statistics_mvdistinct_c --> src_backend_utils_cache_typcache_c
    src_backend_statistics_mvdistinct_c --> src_include_catalog_pg_statistic_ext_h
    src_backend_statistics_mvdistinct_c --> src_include_catalog_pg_statistic_ext_data_h
    src_backend_statistics_mvdistinct_c --> src_include_statistics_extended_stats_internal_h
    src_backend_statistics_mvdistinct_c --> src_include_varatt_h
    src_backend_statistics_relation_stats_c --> src_backend_access_heap_heapam_c
    src_backend_statistics_relation_stats_c --> src_backend_catalog_indexing_c
    src_backend_statistics_relation_stats_c --> src_backend_catalog_namespace_c
    src_backend_statistics_relation_stats_c --> src_backend_nodes_makefuncs_c
    src_backend_statistics_relation_stats_c --> src_backend_statistics_stat_utils_c
    src_backend_statistics_stat_utils_c --> src_backend_catalog_index_c
    src_backend_statistics_stat_utils_c --> src_backend_catalog_namespace_c
    src_backend_statistics_stat_utils_c --> src_backend_catalog_pg_class_c
    src_backend_statistics_stat_utils_c --> src_backend_catalog_pg_collation_c
    src_backend_statistics_stat_utils_c --> src_backend_nodes_nodeFuncs_c
    src_backend_statistics_stat_utils_c --> src_backend_storage_lmgr_lmgr_c
    src_backend_statistics_stat_utils_c --> src_backend_utils_adt_acl_c
    src_backend_statistics_stat_utils_c --> src_backend_utils_cache_typcache_c
    src_backend_statistics_stat_utils_c --> src_backend_utils_fmgr_fmgr_c
    src_backend_statistics_stat_utils_c --> src_backend_utils_fmgr_funcapi_c
    src_backend_statistics_stat_utils_c --> src_include_access_attnum_h
    src_backend_statistics_stat_utils_c --> src_include_access_relation_h
    src_backend_statistics_stat_utils_c --> src_include_catalog_pg_database_h
    src_backend_statistics_stat_utils_c --> src_include_catalog_pg_statistic_h
    src_backend_statistics_stat_utils_c --> src_include_utils_array_h
```
