# `partitioning` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "access"
        src_backend_access_hash_hash_c["hash/hash.c"]
        src_backend_access_index_genam_c["index/genam.c"]
        src_backend_access_nbtree_nbtree_c["nbtree/nbtree.c"]
        src_backend_access_table_table_c["table/table.c"]
        src_backend_access_table_tableam_c["table/tableam.c"]
    end
    subgraph "catalog"
        src_backend_catalog_namespace_c["namespace.c"]
        src_backend_catalog_partition_c["partition.c"]
        src_backend_catalog_pg_inherits_c["pg_inherits.c"]
        src_backend_catalog_pg_operator_c["pg_operator.c"]
        src_backend_catalog_pg_proc_c["pg_proc.c"]
    end
    subgraph "commands"
        src_backend_commands_tablecmds_c["tablecmds.c"]
    end
    subgraph "common"
        src_common_hashfn_c["hashfn.c"]
    end
    subgraph "include/access"
        src_include_access_relation_h["relation.h"]
    end
    subgraph "include/catalog"
        src_include_catalog_pg_opfamily_h["pg_opfamily.h"]
    end
    subgraph "include/executor"
        src_include_executor_executor_h["executor.h"]
    end
    subgraph "include/nodes"
        src_include_nodes_execnodes_h["execnodes.h"]
        src_include_nodes_pathnodes_h["pathnodes.h"]
    end
    subgraph "include/optimizer"
        src_include_optimizer_cost_h["cost.h"]
        src_include_optimizer_optimizer_h["optimizer.h"]
    end
    subgraph "include/parser"
        src_include_parser_parsetree_h["parsetree.h"]
    end
    subgraph "include/partitioning"
        src_include_partitioning_partdefs_h["partdefs.h"]
    end
    subgraph "include/utils"
        src_include_utils_array_h["array.h"]
        src_include_utils_hsearch_h["hsearch.h"]
    end
    subgraph "nodes"
        src_backend_nodes_makefuncs_c["makefuncs.c"]
        src_backend_nodes_nodeFuncs_c["nodeFuncs.c"]
    end
    subgraph "optimizer"
        src_backend_optimizer_util_appendinfo_c["util/appendinfo.c"]
        src_backend_optimizer_util_pathnode_c["util/pathnode.c"]
        src_backend_optimizer_util_placeholder_c["util/placeholder.c"]
    end
    subgraph "parser"
        src_backend_parser_parse_coerce_c["parse_coerce.c"]
        src_backend_parser_parse_node_c["parse_node.c"]
    end
    subgraph "partitioning"
        src_backend_partitioning_partbounds_c["partbounds.c"]
        src_backend_partitioning_partdesc_c["partdesc.c"]
        src_backend_partitioning_partprune_c["partprune.c"]
    end
    subgraph "utils"
        src_backend_utils_adt_datum_c["adt/datum.c"]
        src_backend_utils_adt_ruleutils_c["adt/ruleutils.c"]
        src_backend_utils_cache_inval_c["cache/inval.c"]
        src_backend_utils_cache_partcache_c["cache/partcache.c"]
        src_backend_utils_cache_relcache_c["cache/relcache.c"]
        src_backend_utils_fmgr_fmgr_c["fmgr/fmgr.c"]
        src_backend_utils_time_snapmgr_c["time/snapmgr.c"]
    end
    src_backend_partitioning_partbounds_c --> src_backend_access_table_table_c
    src_backend_partitioning_partbounds_c --> src_backend_access_table_tableam_c
    src_backend_partitioning_partbounds_c --> src_backend_catalog_namespace_c
    src_backend_partitioning_partbounds_c --> src_backend_catalog_partition_c
    src_backend_partitioning_partbounds_c --> src_backend_catalog_pg_inherits_c
    src_backend_partitioning_partbounds_c --> src_backend_commands_tablecmds_c
    src_backend_partitioning_partbounds_c --> src_backend_nodes_makefuncs_c
    src_backend_partitioning_partbounds_c --> src_backend_nodes_nodeFuncs_c
    src_backend_partitioning_partbounds_c --> src_backend_parser_parse_coerce_c
    src_backend_partitioning_partbounds_c --> src_backend_parser_parse_node_c
    src_backend_partitioning_partbounds_c --> src_backend_partitioning_partdesc_c
    src_backend_partitioning_partbounds_c --> src_backend_utils_adt_datum_c
    src_backend_partitioning_partbounds_c --> src_backend_utils_adt_ruleutils_c
    src_backend_partitioning_partbounds_c --> src_backend_utils_cache_partcache_c
    src_backend_partitioning_partbounds_c --> src_backend_utils_fmgr_fmgr_c
    src_backend_partitioning_partbounds_c --> src_backend_utils_time_snapmgr_c
    src_backend_partitioning_partbounds_c --> src_common_hashfn_c
    src_backend_partitioning_partbounds_c --> src_include_access_relation_h
    src_backend_partitioning_partbounds_c --> src_include_executor_executor_h
    src_backend_partitioning_partbounds_c --> src_include_nodes_pathnodes_h
    src_backend_partitioning_partbounds_c --> src_include_partitioning_partdefs_h
    src_backend_partitioning_partbounds_c --> src_include_utils_array_h
    src_backend_partitioning_partdesc_c --> src_backend_access_index_genam_c
    src_backend_partitioning_partdesc_c --> src_backend_access_table_table_c
    src_backend_partitioning_partdesc_c --> src_backend_catalog_partition_c
    src_backend_partitioning_partdesc_c --> src_backend_catalog_pg_inherits_c
    src_backend_partitioning_partdesc_c --> src_backend_partitioning_partbounds_c
    src_backend_partitioning_partdesc_c --> src_backend_utils_cache_inval_c
    src_backend_partitioning_partdesc_c --> src_backend_utils_cache_partcache_c
    src_backend_partitioning_partdesc_c --> src_backend_utils_cache_relcache_c
    src_backend_partitioning_partdesc_c --> src_backend_utils_time_snapmgr_c
    src_backend_partitioning_partdesc_c --> src_include_partitioning_partdefs_h
    src_backend_partitioning_partdesc_c --> src_include_utils_hsearch_h
    src_backend_partitioning_partprune_c --> src_backend_access_hash_hash_c
    src_backend_partitioning_partprune_c --> src_backend_access_nbtree_nbtree_c
    src_backend_partitioning_partprune_c --> src_backend_catalog_pg_operator_c
    src_backend_partitioning_partprune_c --> src_backend_catalog_pg_proc_c
    src_backend_partitioning_partprune_c --> src_backend_nodes_makefuncs_c
    src_backend_partitioning_partprune_c --> src_backend_nodes_nodeFuncs_c
    src_backend_partitioning_partprune_c --> src_backend_optimizer_util_appendinfo_c
    src_backend_partitioning_partprune_c --> src_backend_optimizer_util_pathnode_c
    src_backend_partitioning_partprune_c --> src_backend_optimizer_util_placeholder_c
    src_backend_partitioning_partprune_c --> src_backend_partitioning_partbounds_c
    src_backend_partitioning_partprune_c --> src_include_catalog_pg_opfamily_h
    src_backend_partitioning_partprune_c --> src_include_executor_executor_h
    src_backend_partitioning_partprune_c --> src_include_nodes_execnodes_h
    src_backend_partitioning_partprune_c --> src_include_optimizer_cost_h
    src_backend_partitioning_partprune_c --> src_include_optimizer_optimizer_h
    src_backend_partitioning_partprune_c --> src_include_parser_parsetree_h
    src_backend_partitioning_partprune_c --> src_include_partitioning_partdefs_h
    src_backend_partitioning_partprune_c --> src_include_utils_array_h
```
