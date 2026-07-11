# `rewrite` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "access"
        src_backend_access_common_attmap_c["common/attmap.c"]
        src_backend_access_index_genam_c["index/genam.c"]
        src_backend_access_table_table_c["table/table.c"]
    end
    subgraph "catalog"
        src_backend_catalog_catalog_c["catalog.c"]
        src_backend_catalog_dependency_c["dependency.c"]
        src_backend_catalog_indexing_c["indexing.c"]
        src_backend_catalog_namespace_c["namespace.c"]
        src_backend_catalog_objectaccess_c["objectaccess.c"]
        src_backend_catalog_objectaddress_c["objectaddress.c"]
        src_backend_catalog_pg_class_c["pg_class.c"]
        src_backend_catalog_pg_operator_c["pg_operator.c"]
    end
    subgraph "commands"
        src_backend_commands_trigger_c["trigger.c"]
    end
    subgraph "include/access"
        src_include_access_relation_h["relation.h"]
        src_include_access_sysattr_h["sysattr.h"]
    end
    subgraph "include/catalog"
        src_include_catalog_pg_propgraph_element_h["pg_propgraph_element.h"]
        src_include_catalog_pg_propgraph_element_label_h["pg_propgraph_element_label.h"]
        src_include_catalog_pg_propgraph_label_h["pg_propgraph_label.h"]
        src_include_catalog_pg_propgraph_label_property_h["pg_propgraph_label_property.h"]
        src_include_catalog_pg_propgraph_property_h["pg_propgraph_property.h"]
        src_include_catalog_pg_rewrite_h["pg_rewrite.h"]
    end
    subgraph "include/executor"
        src_include_executor_executor_h["executor.h"]
    end
    subgraph "include/foreign"
        src_include_foreign_fdwapi_h["fdwapi.h"]
    end
    subgraph "include/nodes"
        src_include_nodes_parsenodes_h["parsenodes.h"]
        src_include_nodes_pathnodes_h["pathnodes.h"]
        src_include_nodes_pg_list_h["pg_list.h"]
        src_include_nodes_plannodes_h["plannodes.h"]
        src_include_nodes_primnodes_h["primnodes.h"]
    end
    subgraph "include/optimizer"
        src_include_optimizer_optimizer_h["optimizer.h"]
    end
    subgraph "include/parser"
        src_include_parser_parsetree_h["parsetree.h"]
    end
    subgraph "include/tcop"
        src_include_tcop_tcopprot_h["tcopprot.h"]
    end
    subgraph "include/utils"
        src_include_utils_array_h["array.h"]
    end
    subgraph "nodes"
        src_backend_nodes_makefuncs_c["makefuncs.c"]
        src_backend_nodes_nodeFuncs_c["nodeFuncs.c"]
    end
    subgraph "parser"
        src_backend_parser_analyze_c["analyze.c"]
        src_backend_parser_parse_coerce_c["parse_coerce.c"]
        src_backend_parser_parse_collate_c["parse_collate.c"]
        src_backend_parser_parse_func_c["parse_func.c"]
        src_backend_parser_parse_graphtable_c["parse_graphtable.c"]
        src_backend_parser_parse_node_c["parse_node.c"]
        src_backend_parser_parse_oper_c["parse_oper.c"]
        src_backend_parser_parse_relation_c["parse_relation.c"]
        src_backend_parser_parse_utilcmd_c["parse_utilcmd.c"]
    end
    subgraph "rewrite"
        src_backend_rewrite_rewriteDefine_c["rewriteDefine.c"]
        src_backend_rewrite_rewriteGraphTable_c["rewriteGraphTable.c"]
        src_backend_rewrite_rewriteHandler_c["rewriteHandler.c"]
        src_backend_rewrite_rewriteManip_c["rewriteManip.c"]
        src_backend_rewrite_rewriteRemove_c["rewriteRemove.c"]
        src_backend_rewrite_rewriteSearchCycle_c["rewriteSearchCycle.c"]
        src_backend_rewrite_rewriteSupport_c["rewriteSupport.c"]
        src_backend_rewrite_rowsecurity_c["rowsecurity.c"]
    end
    subgraph "utils"
        src_backend_utils_adt_acl_c["adt/acl.c"]
        src_backend_utils_adt_ruleutils_c["adt/ruleutils.c"]
        src_backend_utils_cache_inval_c["cache/inval.c"]
        src_backend_utils_cache_relcache_c["cache/relcache.c"]
        src_backend_utils_misc_rls_c["misc/rls.c"]
    end
    src_backend_rewrite_rewriteDefine_c --> src_backend_access_table_table_c
    src_backend_rewrite_rewriteDefine_c --> src_backend_catalog_catalog_c
    src_backend_rewrite_rewriteDefine_c --> src_backend_catalog_dependency_c
    src_backend_rewrite_rewriteDefine_c --> src_backend_catalog_indexing_c
    src_backend_rewrite_rewriteDefine_c --> src_backend_catalog_namespace_c
    src_backend_rewrite_rewriteDefine_c --> src_backend_catalog_objectaccess_c
    src_backend_rewrite_rewriteDefine_c --> src_backend_catalog_objectaddress_c
    src_backend_rewrite_rewriteDefine_c --> src_backend_nodes_nodeFuncs_c
    src_backend_rewrite_rewriteDefine_c --> src_backend_parser_parse_utilcmd_c
    src_backend_rewrite_rewriteDefine_c --> src_backend_rewrite_rewriteManip_c
    src_backend_rewrite_rewriteDefine_c --> src_backend_rewrite_rewriteSupport_c
    src_backend_rewrite_rewriteDefine_c --> src_backend_utils_adt_acl_c
    src_backend_rewrite_rewriteDefine_c --> src_backend_utils_cache_inval_c
    src_backend_rewrite_rewriteDefine_c --> src_backend_utils_cache_relcache_c
    src_backend_rewrite_rewriteDefine_c --> src_include_access_relation_h
    src_backend_rewrite_rewriteDefine_c --> src_include_catalog_pg_rewrite_h
    src_backend_rewrite_rewriteDefine_c --> src_include_nodes_parsenodes_h
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_access_index_genam_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_access_table_table_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_catalog_pg_operator_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_nodes_makefuncs_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_nodes_nodeFuncs_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_parser_analyze_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_parser_parse_collate_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_parser_parse_func_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_parser_parse_graphtable_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_parser_parse_node_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_parser_parse_oper_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_parser_parse_relation_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_rewrite_rewriteHandler_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_rewrite_rewriteManip_c
    src_backend_rewrite_rewriteGraphTable_c --> src_backend_utils_adt_ruleutils_c
    src_backend_rewrite_rewriteGraphTable_c --> src_include_access_sysattr_h
    src_backend_rewrite_rewriteGraphTable_c --> src_include_catalog_pg_propgraph_element_h
    src_backend_rewrite_rewriteGraphTable_c --> src_include_catalog_pg_propgraph_element_label_h
    src_backend_rewrite_rewriteGraphTable_c --> src_include_catalog_pg_propgraph_label_h
    src_backend_rewrite_rewriteGraphTable_c --> src_include_catalog_pg_propgraph_label_property_h
    src_backend_rewrite_rewriteGraphTable_c --> src_include_catalog_pg_propgraph_property_h
    src_backend_rewrite_rewriteGraphTable_c --> src_include_nodes_parsenodes_h
    src_backend_rewrite_rewriteGraphTable_c --> src_include_optimizer_optimizer_h
    src_backend_rewrite_rewriteGraphTable_c --> src_include_parser_parsetree_h
    src_backend_rewrite_rewriteGraphTable_c --> src_include_utils_array_h
    src_backend_rewrite_rewriteHandler_c --> src_backend_access_table_table_c
    src_backend_rewrite_rewriteHandler_c --> src_backend_catalog_dependency_c
    src_backend_rewrite_rewriteHandler_c --> src_backend_commands_trigger_c
    src_backend_rewrite_rewriteHandler_c --> src_backend_nodes_makefuncs_c
    src_backend_rewrite_rewriteHandler_c --> src_backend_nodes_nodeFuncs_c
    src_backend_rewrite_rewriteHandler_c --> src_backend_parser_analyze_c
    src_backend_rewrite_rewriteHandler_c --> src_backend_parser_parse_coerce_c
    src_backend_rewrite_rewriteHandler_c --> src_backend_parser_parse_relation_c
    src_backend_rewrite_rewriteHandler_c --> src_backend_rewrite_rewriteDefine_c
    src_backend_rewrite_rewriteHandler_c --> src_backend_rewrite_rewriteGraphTable_c
    src_backend_rewrite_rewriteHandler_c --> src_backend_rewrite_rewriteManip_c
    src_backend_rewrite_rewriteHandler_c --> src_backend_rewrite_rewriteSearchCycle_c
    src_backend_rewrite_rewriteHandler_c --> src_backend_rewrite_rowsecurity_c
    src_backend_rewrite_rewriteHandler_c --> src_backend_utils_cache_relcache_c
    src_backend_rewrite_rewriteHandler_c --> src_include_access_relation_h
    src_backend_rewrite_rewriteHandler_c --> src_include_access_sysattr_h
    src_backend_rewrite_rewriteHandler_c --> src_include_executor_executor_h
    src_backend_rewrite_rewriteHandler_c --> src_include_foreign_fdwapi_h
    src_backend_rewrite_rewriteHandler_c --> src_include_nodes_parsenodes_h
    src_backend_rewrite_rewriteHandler_c --> src_include_optimizer_optimizer_h
    src_backend_rewrite_rewriteHandler_c --> src_include_parser_parsetree_h
    src_backend_rewrite_rewriteHandler_c --> src_include_tcop_tcopprot_h
    src_backend_rewrite_rewriteManip_c --> src_backend_access_common_attmap_c
    src_backend_rewrite_rewriteManip_c --> src_backend_nodes_makefuncs_c
    src_backend_rewrite_rewriteManip_c --> src_backend_nodes_nodeFuncs_c
    src_backend_rewrite_rewriteManip_c --> src_backend_parser_parse_coerce_c
    src_backend_rewrite_rewriteManip_c --> src_backend_parser_parse_relation_c
    src_backend_rewrite_rewriteManip_c --> src_include_nodes_parsenodes_h
    src_backend_rewrite_rewriteManip_c --> src_include_nodes_pathnodes_h
    src_backend_rewrite_rewriteManip_c --> src_include_nodes_plannodes_h
    src_backend_rewrite_rewriteManip_c --> src_include_parser_parsetree_h
    src_backend_rewrite_rewriteRemove_c --> src_backend_access_index_genam_c
    src_backend_rewrite_rewriteRemove_c --> src_backend_access_table_table_c
    src_backend_rewrite_rewriteRemove_c --> src_backend_catalog_catalog_c
    src_backend_rewrite_rewriteRemove_c --> src_backend_catalog_indexing_c
    src_backend_rewrite_rewriteRemove_c --> src_backend_utils_cache_inval_c
    src_backend_rewrite_rewriteRemove_c --> src_include_catalog_pg_rewrite_h
    src_backend_rewrite_rewriteRemove_c --> src_include_nodes_parsenodes_h
    src_backend_rewrite_rewriteSearchCycle_c --> src_backend_nodes_makefuncs_c
    src_backend_rewrite_rewriteSearchCycle_c --> src_backend_parser_analyze_c
    src_backend_rewrite_rewriteSearchCycle_c --> src_backend_rewrite_rewriteManip_c
    src_backend_rewrite_rewriteSearchCycle_c --> src_include_nodes_parsenodes_h
    src_backend_rewrite_rewriteSearchCycle_c --> src_include_nodes_pg_list_h
    src_backend_rewrite_rewriteSearchCycle_c --> src_include_nodes_primnodes_h
    src_backend_rewrite_rewriteSearchCycle_c --> src_include_parser_parsetree_h
    src_backend_rewrite_rewriteSupport_c --> src_backend_access_table_table_c
    src_backend_rewrite_rewriteSupport_c --> src_backend_catalog_indexing_c
    src_backend_rewrite_rewriteSupport_c --> src_backend_catalog_pg_class_c
    src_backend_rewrite_rewriteSupport_c --> src_backend_utils_cache_inval_c
    src_backend_rewrite_rewriteSupport_c --> src_include_catalog_pg_rewrite_h
    src_backend_rewrite_rowsecurity_c --> src_backend_access_table_table_c
    src_backend_rewrite_rowsecurity_c --> src_backend_catalog_pg_class_c
    src_backend_rewrite_rowsecurity_c --> src_backend_nodes_makefuncs_c
    src_backend_rewrite_rowsecurity_c --> src_backend_parser_parse_relation_c
    src_backend_rewrite_rowsecurity_c --> src_backend_rewrite_rewriteDefine_c
    src_backend_rewrite_rowsecurity_c --> src_backend_rewrite_rewriteManip_c
    src_backend_rewrite_rowsecurity_c --> src_backend_utils_adt_acl_c
    src_backend_rewrite_rowsecurity_c --> src_backend_utils_cache_relcache_c
    src_backend_rewrite_rowsecurity_c --> src_backend_utils_misc_rls_c
    src_backend_rewrite_rowsecurity_c --> src_include_nodes_parsenodes_h
    src_backend_rewrite_rowsecurity_c --> src_include_nodes_pg_list_h
    src_backend_rewrite_rowsecurity_c --> src_include_utils_array_h
```
