# `parser` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "access"
        src_backend_access_common_attmap_c["common/attmap.c"]
        src_backend_access_common_reloptions_c["common/reloptions.c"]
        src_backend_access_common_toast_compression_c["common/toast_compression.c"]
        src_backend_access_index_amapi_c["index/amapi.c"]
        src_backend_access_index_genam_c["index/genam.c"]
        src_backend_access_nbtree_nbtree_c["nbtree/nbtree.c"]
        src_backend_access_table_table_c["table/table.c"]
    end
    subgraph "catalog"
        src_backend_catalog_catalog_c["catalog.c"]
        src_backend_catalog_dependency_c["dependency.c"]
        src_backend_catalog_heap_c["heap.c"]
        src_backend_catalog_index_c["index.c"]
        src_backend_catalog_namespace_c["namespace.c"]
        src_backend_catalog_partition_c["partition.c"]
        src_backend_catalog_pg_aggregate_c["pg_aggregate.c"]
        src_backend_catalog_pg_cast_c["pg_cast.c"]
        src_backend_catalog_pg_class_c["pg_class.c"]
        src_backend_catalog_pg_collation_c["pg_collation.c"]
        src_backend_catalog_pg_constraint_c["pg_constraint.c"]
        src_backend_catalog_pg_inherits_c["pg_inherits.c"]
        src_backend_catalog_pg_operator_c["pg_operator.c"]
        src_backend_catalog_pg_proc_c["pg_proc.c"]
    end
    subgraph "commands"
        src_backend_commands_comment_c["comment.c"]
        src_backend_commands_sequence_c["sequence.c"]
        src_backend_commands_tablecmds_c["tablecmds.c"]
        src_backend_commands_tablespace_c["tablespace.c"]
    end
    subgraph "common"
        src_common_stringinfo_c["stringinfo.c"]
    end
    subgraph "include/access"
        src_include_access_htup_h["htup.h"]
        src_include_access_relation_h["relation.h"]
        src_include_access_stratnum_h["stratnum.h"]
        src_include_access_sysattr_h["sysattr.h"]
        src_include_access_tsmapi_h["tsmapi.h"]
    end
    subgraph "include/catalog"
        src_include_catalog_pg_am_h["pg_am.h"]
        src_include_catalog_pg_amproc_h["pg_amproc.h"]
        src_include_catalog_pg_opclass_h["pg_opclass.h"]
        src_include_catalog_pg_propgraph_label_h["pg_propgraph_label.h"]
        src_include_catalog_pg_propgraph_property_h["pg_propgraph_property.h"]
        src_include_catalog_pg_statistic_ext_h["pg_statistic_ext.h"]
    end
    subgraph "include/commands"
        src_include_commands_defrem_h["defrem.h"]
    end
    subgraph "include/mb"
        src_include_mb_pg_wchar_h["pg_wchar.h"]
    end
    subgraph "include/nodes"
        src_include_nodes_miscnodes_h["miscnodes.h"]
        src_include_nodes_parsenodes_h["parsenodes.h"]
        src_include_nodes_pg_list_h["pg_list.h"]
        src_include_nodes_queryjumble_h["queryjumble.h"]
        src_include_nodes_subscripting_h["subscripting.h"]
    end
    subgraph "include/optimizer"
        src_include_optimizer_optimizer_h["optimizer.h"]
    end
    subgraph "include/parser"
        src_include_parser_parsetree_h["parsetree.h"]
        src_include_parser_scanner_h["scanner.h"]
    end
    subgraph "include/storage"
        src_include_storage_lockdefs_h["lockdefs.h"]
    end
    subgraph "include/utils"
        src_include_utils_array_h["array.h"]
        src_include_utils_hsearch_h["hsearch.h"]
    end
    subgraph "nodes"
        src_backend_nodes_makefuncs_c["makefuncs.c"]
        src_backend_nodes_nodeFuncs_c["nodeFuncs.c"]
        src_backend_nodes_params_c["params.c"]
    end
    subgraph "parser"
        src_backend_parser_analyze_c["analyze.c"]
        src_backend_parser_gramparse_h["gramparse.h"]
        src_backend_parser_parse_agg_c["parse_agg.c"]
        src_backend_parser_parse_clause_c["parse_clause.c"]
        src_backend_parser_parse_coerce_c["parse_coerce.c"]
        src_backend_parser_parse_collate_c["parse_collate.c"]
        src_backend_parser_parse_cte_c["parse_cte.c"]
        src_backend_parser_parse_enr_c["parse_enr.c"]
        src_backend_parser_parse_expr_c["parse_expr.c"]
        src_backend_parser_parse_func_c["parse_func.c"]
        src_backend_parser_parse_graphtable_c["parse_graphtable.c"]
        src_backend_parser_parse_jsontable_c["parse_jsontable.c"]
        src_backend_parser_parse_merge_c["parse_merge.c"]
        src_backend_parser_parse_node_c["parse_node.c"]
        src_backend_parser_parse_oper_c["parse_oper.c"]
        src_backend_parser_parse_param_c["parse_param.c"]
        src_backend_parser_parse_relation_c["parse_relation.c"]
        src_backend_parser_parse_target_c["parse_target.c"]
        src_backend_parser_parse_type_c["parse_type.c"]
        src_backend_parser_parse_utilcmd_c["parse_utilcmd.c"]
        src_backend_parser_parser_c["parser.c"]
        src_backend_parser_scansup_c["scansup.c"]
    end
    subgraph "partitioning"
        src_backend_partitioning_partbounds_c["partbounds.c"]
        src_backend_partitioning_partdesc_c["partdesc.c"]
    end
    subgraph "rewrite"
        src_backend_rewrite_rewriteManip_c["rewriteManip.c"]
    end
    subgraph "storage"
        src_backend_storage_lmgr_lmgr_c["lmgr/lmgr.c"]
    end
    subgraph "utils"
        src_backend_utils_activity_backend_status_c["activity/backend_status.c"]
        src_backend_utils_adt_acl_c["adt/acl.c"]
        src_backend_utils_adt_date_c["adt/date.c"]
        src_backend_utils_adt_datum_c["adt/datum.c"]
        src_backend_utils_adt_int_c["adt/int.c"]
        src_backend_utils_adt_json_c["adt/json.c"]
        src_backend_utils_adt_pg_locale_c["adt/pg_locale.c"]
        src_backend_utils_adt_rangetypes_c["adt/rangetypes.c"]
        src_backend_utils_adt_ruleutils_c["adt/ruleutils.c"]
        src_backend_utils_adt_timestamp_c["adt/timestamp.c"]
        src_backend_utils_adt_varlena_c["adt/varlena.c"]
        src_backend_utils_adt_xml_c["adt/xml.c"]
        src_backend_utils_cache_catcache_c["cache/catcache.c"]
        src_backend_utils_cache_inval_c["cache/inval.c"]
        src_backend_utils_cache_partcache_c["cache/partcache.c"]
        src_backend_utils_cache_relcache_c["cache/relcache.c"]
        src_backend_utils_cache_typcache_c["cache/typcache.c"]
        src_backend_utils_fmgr_funcapi_c["fmgr/funcapi.c"]
        src_backend_utils_misc_guc_c["misc/guc.c"]
        src_backend_utils_misc_queryenvironment_c["misc/queryenvironment.c"]
    end
    src_backend_parser_analyze_c --> src_backend_catalog_dependency_c
    src_backend_parser_analyze_c --> src_backend_catalog_pg_operator_c
    src_backend_parser_analyze_c --> src_backend_catalog_pg_proc_c
    src_backend_parser_analyze_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_analyze_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_analyze_c --> src_backend_nodes_params_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_agg_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_clause_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_coerce_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_collate_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_cte_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_expr_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_func_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_merge_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_node_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_oper_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_param_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_relation_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_target_c
    src_backend_parser_analyze_c --> src_backend_parser_parse_type_c
    src_backend_parser_analyze_c --> src_backend_utils_activity_backend_status_c
    src_backend_parser_analyze_c --> src_backend_utils_adt_rangetypes_c
    src_backend_parser_analyze_c --> src_backend_utils_misc_guc_c
    src_backend_parser_analyze_c --> src_include_access_stratnum_h
    src_backend_parser_analyze_c --> src_include_access_sysattr_h
    src_backend_parser_analyze_c --> src_include_catalog_pg_am_h
    src_backend_parser_analyze_c --> src_include_commands_defrem_h
    src_backend_parser_analyze_c --> src_include_nodes_queryjumble_h
    src_backend_parser_analyze_c --> src_include_optimizer_optimizer_h
    src_backend_parser_analyze_c --> src_include_parser_parsetree_h
    src_backend_parser_gramparse_h --> src_include_nodes_parsenodes_h
    src_backend_parser_gramparse_h --> src_include_parser_scanner_h
    src_backend_parser_parse_agg_c --> src_backend_catalog_pg_aggregate_c
    src_backend_parser_parse_agg_c --> src_backend_catalog_pg_constraint_c
    src_backend_parser_parse_agg_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_agg_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_agg_c --> src_backend_parser_parse_clause_c
    src_backend_parser_parse_agg_c --> src_backend_parser_parse_coerce_c
    src_backend_parser_parse_agg_c --> src_backend_parser_parse_expr_c
    src_backend_parser_parse_agg_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_agg_c --> src_backend_parser_parse_relation_c
    src_backend_parser_parse_agg_c --> src_backend_rewrite_rewriteManip_c
    src_backend_parser_parse_agg_c --> src_backend_utils_adt_int_c
    src_backend_parser_parse_agg_c --> src_include_optimizer_optimizer_h
    src_backend_parser_parse_agg_c --> src_include_parser_parsetree_h
    src_backend_parser_parse_clause_c --> src_backend_access_nbtree_nbtree_c
    src_backend_parser_parse_clause_c --> src_backend_access_table_table_c
    src_backend_parser_parse_clause_c --> src_backend_catalog_catalog_c
    src_backend_parser_parse_clause_c --> src_backend_catalog_pg_constraint_c
    src_backend_parser_parse_clause_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_clause_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_clause_c --> src_backend_parser_analyze_c
    src_backend_parser_parse_clause_c --> src_backend_parser_parse_coerce_c
    src_backend_parser_parse_clause_c --> src_backend_parser_parse_collate_c
    src_backend_parser_parse_clause_c --> src_backend_parser_parse_expr_c
    src_backend_parser_parse_clause_c --> src_backend_parser_parse_func_c
    src_backend_parser_parse_clause_c --> src_backend_parser_parse_graphtable_c
    src_backend_parser_parse_clause_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_clause_c --> src_backend_parser_parse_oper_c
    src_backend_parser_parse_clause_c --> src_backend_parser_parse_relation_c
    src_backend_parser_parse_clause_c --> src_backend_parser_parse_target_c
    src_backend_parser_parse_clause_c --> src_backend_parser_parse_type_c
    src_backend_parser_parse_clause_c --> src_backend_parser_parser_c
    src_backend_parser_parse_clause_c --> src_backend_rewrite_rewriteManip_c
    src_backend_parser_parse_clause_c --> src_backend_utils_cache_catcache_c
    src_backend_parser_parse_clause_c --> src_include_access_relation_h
    src_backend_parser_parse_clause_c --> src_include_access_tsmapi_h
    src_backend_parser_parse_clause_c --> src_include_catalog_pg_am_h
    src_backend_parser_parse_clause_c --> src_include_catalog_pg_amproc_h
    src_backend_parser_parse_clause_c --> src_include_commands_defrem_h
    src_backend_parser_parse_clause_c --> src_include_optimizer_optimizer_h
    src_backend_parser_parse_coerce_c --> src_backend_catalog_pg_cast_c
    src_backend_parser_parse_coerce_c --> src_backend_catalog_pg_class_c
    src_backend_parser_parse_coerce_c --> src_backend_catalog_pg_inherits_c
    src_backend_parser_parse_coerce_c --> src_backend_catalog_pg_proc_c
    src_backend_parser_parse_coerce_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_coerce_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_coerce_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_coerce_c --> src_backend_parser_parse_relation_c
    src_backend_parser_parse_coerce_c --> src_backend_parser_parse_type_c
    src_backend_parser_parse_coerce_c --> src_backend_utils_adt_datum_c
    src_backend_parser_parse_coerce_c --> src_backend_utils_cache_typcache_c
    src_backend_parser_parse_collate_c --> src_backend_catalog_pg_aggregate_c
    src_backend_parser_parse_collate_c --> src_backend_catalog_pg_collation_c
    src_backend_parser_parse_collate_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_collate_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_collate_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_cte_c --> src_backend_catalog_pg_collation_c
    src_backend_parser_parse_cte_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_cte_c --> src_backend_parser_analyze_c
    src_backend_parser_parse_cte_c --> src_backend_parser_parse_coerce_c
    src_backend_parser_parse_cte_c --> src_backend_parser_parse_collate_c
    src_backend_parser_parse_cte_c --> src_backend_parser_parse_expr_c
    src_backend_parser_parse_cte_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_cte_c --> src_backend_utils_cache_typcache_c
    src_backend_parser_parse_enr_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_expr_c --> src_backend_catalog_pg_aggregate_c
    src_backend_parser_parse_expr_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_expr_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_expr_c --> src_backend_parser_analyze_c
    src_backend_parser_parse_expr_c --> src_backend_parser_parse_agg_c
    src_backend_parser_parse_expr_c --> src_backend_parser_parse_clause_c
    src_backend_parser_parse_expr_c --> src_backend_parser_parse_coerce_c
    src_backend_parser_parse_expr_c --> src_backend_parser_parse_collate_c
    src_backend_parser_parse_expr_c --> src_backend_parser_parse_func_c
    src_backend_parser_parse_expr_c --> src_backend_parser_parse_graphtable_c
    src_backend_parser_parse_expr_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_expr_c --> src_backend_parser_parse_oper_c
    src_backend_parser_parse_expr_c --> src_backend_parser_parse_relation_c
    src_backend_parser_parse_expr_c --> src_backend_parser_parse_target_c
    src_backend_parser_parse_expr_c --> src_backend_parser_parse_type_c
    src_backend_parser_parse_expr_c --> src_backend_utils_adt_date_c
    src_backend_parser_parse_expr_c --> src_backend_utils_adt_timestamp_c
    src_backend_parser_parse_expr_c --> src_backend_utils_adt_xml_c
    src_backend_parser_parse_expr_c --> src_backend_utils_cache_typcache_c
    src_backend_parser_parse_expr_c --> src_include_optimizer_optimizer_h
    src_backend_parser_parse_func_c --> src_backend_catalog_namespace_c
    src_backend_parser_parse_func_c --> src_backend_catalog_pg_aggregate_c
    src_backend_parser_parse_func_c --> src_backend_catalog_pg_proc_c
    src_backend_parser_parse_func_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_func_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_func_c --> src_backend_parser_parse_agg_c
    src_backend_parser_parse_func_c --> src_backend_parser_parse_clause_c
    src_backend_parser_parse_func_c --> src_backend_parser_parse_coerce_c
    src_backend_parser_parse_func_c --> src_backend_parser_parse_expr_c
    src_backend_parser_parse_func_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_func_c --> src_backend_parser_parse_relation_c
    src_backend_parser_parse_func_c --> src_backend_parser_parse_target_c
    src_backend_parser_parse_func_c --> src_backend_parser_parse_type_c
    src_backend_parser_parse_func_c --> src_backend_utils_fmgr_funcapi_c
    src_backend_parser_parse_func_c --> src_common_stringinfo_c
    src_backend_parser_parse_graphtable_c --> src_backend_access_index_genam_c
    src_backend_parser_parse_graphtable_c --> src_backend_access_table_table_c
    src_backend_parser_parse_graphtable_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_graphtable_c --> src_backend_parser_parse_collate_c
    src_backend_parser_parse_graphtable_c --> src_backend_parser_parse_expr_c
    src_backend_parser_parse_graphtable_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_graphtable_c --> src_backend_utils_cache_relcache_c
    src_backend_parser_parse_graphtable_c --> src_include_catalog_pg_propgraph_label_h
    src_backend_parser_parse_graphtable_c --> src_include_catalog_pg_propgraph_property_h
    src_backend_parser_parse_graphtable_c --> src_include_nodes_pg_list_h
    src_backend_parser_parse_jsontable_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_jsontable_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_jsontable_c --> src_backend_parser_parse_clause_c
    src_backend_parser_parse_jsontable_c --> src_backend_parser_parse_collate_c
    src_backend_parser_parse_jsontable_c --> src_backend_parser_parse_expr_c
    src_backend_parser_parse_jsontable_c --> src_backend_parser_parse_relation_c
    src_backend_parser_parse_jsontable_c --> src_backend_parser_parse_type_c
    src_backend_parser_parse_jsontable_c --> src_backend_utils_adt_json_c
    src_backend_parser_parse_jsontable_c --> src_include_optimizer_optimizer_h
    src_backend_parser_parse_merge_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_merge_c --> src_backend_parser_analyze_c
    src_backend_parser_parse_merge_c --> src_backend_parser_parse_clause_c
    src_backend_parser_parse_merge_c --> src_backend_parser_parse_collate_c
    src_backend_parser_parse_merge_c --> src_backend_parser_parse_cte_c
    src_backend_parser_parse_merge_c --> src_backend_parser_parse_expr_c
    src_backend_parser_parse_merge_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_merge_c --> src_backend_parser_parse_relation_c
    src_backend_parser_parse_merge_c --> src_backend_parser_parse_target_c
    src_backend_parser_parse_merge_c --> src_include_access_sysattr_h
    src_backend_parser_parse_merge_c --> src_include_parser_parsetree_h
    src_backend_parser_parse_node_c --> src_backend_access_table_table_c
    src_backend_parser_parse_node_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_node_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_node_c --> src_backend_utils_cache_relcache_c
    src_backend_parser_parse_node_c --> src_backend_utils_misc_queryenvironment_c
    src_backend_parser_parse_node_c --> src_include_mb_pg_wchar_h
    src_backend_parser_parse_node_c --> src_include_nodes_miscnodes_h
    src_backend_parser_parse_node_c --> src_include_nodes_parsenodes_h
    src_backend_parser_parse_node_c --> src_include_nodes_subscripting_h
    src_backend_parser_parse_oper_c --> src_backend_catalog_pg_operator_c
    src_backend_parser_parse_oper_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_oper_c --> src_backend_parser_parse_coerce_c
    src_backend_parser_parse_oper_c --> src_backend_parser_parse_func_c
    src_backend_parser_parse_oper_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_oper_c --> src_backend_parser_parse_type_c
    src_backend_parser_parse_oper_c --> src_backend_utils_cache_inval_c
    src_backend_parser_parse_oper_c --> src_backend_utils_cache_typcache_c
    src_backend_parser_parse_oper_c --> src_common_stringinfo_c
    src_backend_parser_parse_oper_c --> src_include_access_htup_h
    src_backend_parser_parse_oper_c --> src_include_nodes_parsenodes_h
    src_backend_parser_parse_oper_c --> src_include_utils_hsearch_h
    src_backend_parser_parse_param_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_param_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_relation_c --> src_backend_access_table_table_c
    src_backend_parser_parse_relation_c --> src_backend_catalog_heap_c
    src_backend_parser_parse_relation_c --> src_backend_catalog_namespace_c
    src_backend_parser_parse_relation_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_relation_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_relation_c --> src_backend_parser_parse_enr_c
    src_backend_parser_parse_relation_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_relation_c --> src_backend_parser_parse_type_c
    src_backend_parser_parse_relation_c --> src_backend_storage_lmgr_lmgr_c
    src_backend_parser_parse_relation_c --> src_backend_utils_adt_varlena_c
    src_backend_parser_parse_relation_c --> src_backend_utils_fmgr_funcapi_c
    src_backend_parser_parse_relation_c --> src_include_access_relation_h
    src_backend_parser_parse_relation_c --> src_include_parser_parsetree_h
    src_backend_parser_parse_relation_c --> src_include_storage_lockdefs_h
    src_backend_parser_parse_target_c --> src_backend_catalog_namespace_c
    src_backend_parser_parse_target_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_target_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_target_c --> src_backend_parser_parse_coerce_c
    src_backend_parser_parse_target_c --> src_backend_parser_parse_expr_c
    src_backend_parser_parse_target_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_target_c --> src_backend_parser_parse_relation_c
    src_backend_parser_parse_target_c --> src_backend_parser_parse_type_c
    src_backend_parser_parse_target_c --> src_backend_utils_fmgr_funcapi_c
    src_backend_parser_parse_target_c --> src_include_parser_parsetree_h
    src_backend_parser_parse_type_c --> src_backend_catalog_namespace_c
    src_backend_parser_parse_type_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_type_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_type_c --> src_backend_parser_parser_c
    src_backend_parser_parse_type_c --> src_common_stringinfo_c
    src_backend_parser_parse_type_c --> src_include_access_htup_h
    src_backend_parser_parse_type_c --> src_include_utils_array_h
    src_backend_parser_parse_utilcmd_c --> src_backend_access_common_attmap_c
    src_backend_parser_parse_utilcmd_c --> src_backend_access_common_reloptions_c
    src_backend_parser_parse_utilcmd_c --> src_backend_access_common_toast_compression_c
    src_backend_parser_parse_utilcmd_c --> src_backend_access_index_amapi_c
    src_backend_parser_parse_utilcmd_c --> src_backend_access_table_table_c
    src_backend_parser_parse_utilcmd_c --> src_backend_catalog_dependency_c
    src_backend_parser_parse_utilcmd_c --> src_backend_catalog_heap_c
    src_backend_parser_parse_utilcmd_c --> src_backend_catalog_index_c
    src_backend_parser_parse_utilcmd_c --> src_backend_catalog_namespace_c
    src_backend_parser_parse_utilcmd_c --> src_backend_catalog_partition_c
    src_backend_parser_parse_utilcmd_c --> src_backend_catalog_pg_collation_c
    src_backend_parser_parse_utilcmd_c --> src_backend_catalog_pg_constraint_c
    src_backend_parser_parse_utilcmd_c --> src_backend_catalog_pg_operator_c
    src_backend_parser_parse_utilcmd_c --> src_backend_commands_comment_c
    src_backend_parser_parse_utilcmd_c --> src_backend_commands_sequence_c
    src_backend_parser_parse_utilcmd_c --> src_backend_commands_tablecmds_c
    src_backend_parser_parse_utilcmd_c --> src_backend_commands_tablespace_c
    src_backend_parser_parse_utilcmd_c --> src_backend_nodes_makefuncs_c
    src_backend_parser_parse_utilcmd_c --> src_backend_nodes_nodeFuncs_c
    src_backend_parser_parse_utilcmd_c --> src_backend_parser_analyze_c
    src_backend_parser_parse_utilcmd_c --> src_backend_parser_parse_clause_c
    src_backend_parser_parse_utilcmd_c --> src_backend_parser_parse_coerce_c
    src_backend_parser_parse_utilcmd_c --> src_backend_parser_parse_collate_c
    src_backend_parser_parse_utilcmd_c --> src_backend_parser_parse_expr_c
    src_backend_parser_parse_utilcmd_c --> src_backend_parser_parse_node_c
    src_backend_parser_parse_utilcmd_c --> src_backend_parser_parse_relation_c
    src_backend_parser_parse_utilcmd_c --> src_backend_parser_parse_target_c
    src_backend_parser_parse_utilcmd_c --> src_backend_parser_parse_type_c
    src_backend_parser_parse_utilcmd_c --> src_backend_parser_parser_c
    src_backend_parser_parse_utilcmd_c --> src_backend_partitioning_partbounds_c
    src_backend_parser_parse_utilcmd_c --> src_backend_partitioning_partdesc_c
    src_backend_parser_parse_utilcmd_c --> src_backend_rewrite_rewriteManip_c
    src_backend_parser_parse_utilcmd_c --> src_backend_utils_adt_acl_c
    src_backend_parser_parse_utilcmd_c --> src_backend_utils_adt_ruleutils_c
    src_backend_parser_parse_utilcmd_c --> src_backend_utils_cache_partcache_c
    src_backend_parser_parse_utilcmd_c --> src_backend_utils_cache_typcache_c
    src_backend_parser_parse_utilcmd_c --> src_include_access_relation_h
    src_backend_parser_parse_utilcmd_c --> src_include_catalog_pg_am_h
    src_backend_parser_parse_utilcmd_c --> src_include_catalog_pg_opclass_h
    src_backend_parser_parse_utilcmd_c --> src_include_catalog_pg_statistic_ext_h
    src_backend_parser_parse_utilcmd_c --> src_include_commands_defrem_h
    src_backend_parser_parse_utilcmd_c --> src_include_optimizer_optimizer_h
    src_backend_parser_parser_c --> src_backend_parser_gramparse_h
    src_backend_parser_parser_c --> src_backend_parser_scansup_c
    src_backend_parser_parser_c --> src_include_mb_pg_wchar_h
    src_backend_parser_parser_c --> src_include_nodes_parsenodes_h
    src_backend_parser_scansup_c --> src_backend_utils_adt_pg_locale_c
    src_backend_parser_scansup_c --> src_include_mb_pg_wchar_h
```
