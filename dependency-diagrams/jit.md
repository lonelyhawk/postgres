# `jit` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "access"
        src_backend_access_common_tupdesc_c["common/tupdesc.c"]
        src_backend_access_nbtree_nbtree_c["nbtree/nbtree.c"]
    end
    subgraph "catalog"
        src_backend_catalog_objectaccess_c["objectaccess.c"]
    end
    subgraph "common"
        src_common_instr_time_c["instr_time.c"]
    end
    subgraph "executor"
        src_backend_executor_execExpr_c["execExpr.c"]
        src_backend_executor_instrument_c["instrument.c"]
        src_backend_executor_nodeAgg_c["nodeAgg.c"]
        src_backend_executor_nodeSubplan_c["nodeSubplan.c"]
    end
    subgraph "include/access"
        src_include_access_htup_h["htup.h"]
        src_include_access_tupdesc_details_h["tupdesc_details.h"]
    end
    subgraph "include/catalog"
        src_include_catalog_pg_attribute_h["pg_attribute.h"]
    end
    subgraph "include/executor"
        src_include_executor_execdebug_h["execdebug.h"]
        src_include_executor_tuptable_h["tuptable.h"]
    end
    subgraph "include/jit"
        src_include_jit_llvmjit_backport_h["llvmjit_backport.h"]
        src_include_jit_llvmjit_emit_h["llvmjit_emit.h"]
    end
    subgraph "include/nodes"
        src_include_nodes_execnodes_h["execnodes.h"]
        src_include_nodes_memnodes_h["memnodes.h"]
        src_include_nodes_pg_list_h["pg_list.h"]
    end
    subgraph "include/parser"
        src_include_parser_parsetree_h["parsetree.h"]
    end
    subgraph "include/port"
        src_include_port_win32_msvc_unistd_h["win32_msvc/unistd.h"]
    end
    subgraph "include/utils"
        src_include_utils_fmgrtab_h["fmgrtab.h"]
        src_include_utils_palloc_h["palloc.h"]
    end
    subgraph "jit"
        src_backend_jit_jit_c["jit.c"]
        src_backend_jit_llvm_llvmjit_c["llvm/llvmjit.c"]
        src_backend_jit_llvm_llvmjit_deform_c["llvm/llvmjit_deform.c"]
        src_backend_jit_llvm_llvmjit_expr_c["llvm/llvmjit_expr.c"]
        src_backend_jit_llvm_llvmjit_types_c["llvm/llvmjit_types.c"]
    end
    subgraph "nodes"
        src_backend_nodes_makefuncs_c["makefuncs.c"]
        src_backend_nodes_nodeFuncs_c["nodeFuncs.c"]
    end
    subgraph "parser"
        src_backend_parser_parse_coerce_c["parse_coerce.c"]
    end
    subgraph "storage"
        src_backend_storage_file_fd_c["file/fd.c"]
        src_backend_storage_ipc_ipc_c["ipc/ipc.c"]
    end
    subgraph "utils"
        src_backend_utils_adt_acl_c["adt/acl.c"]
        src_backend_utils_adt_date_c["adt/date.c"]
        src_backend_utils_adt_expandeddatum_c["adt/expandeddatum.c"]
        src_backend_utils_adt_timestamp_c["adt/timestamp.c"]
        src_backend_utils_adt_xml_c["adt/xml.c"]
        src_backend_utils_cache_typcache_c["cache/typcache.c"]
        src_backend_utils_fmgr_fmgr_c["fmgr/fmgr.c"]
        src_backend_utils_fmgr_funcapi_c["fmgr/funcapi.c"]
        src_backend_utils_resowner_resowner_c["resowner/resowner.c"]
    end
    src_backend_jit_jit_c --> src_backend_executor_instrument_c
    src_backend_jit_jit_c --> src_backend_storage_file_fd_c
    src_backend_jit_jit_c --> src_backend_utils_fmgr_fmgr_c
    src_backend_jit_jit_c --> src_backend_utils_resowner_resowner_c
    src_backend_jit_jit_c --> src_common_instr_time_c
    src_backend_jit_jit_c --> src_include_nodes_execnodes_h
    src_backend_jit_jit_c --> src_include_port_win32_msvc_unistd_h
    src_backend_jit_llvm_llvmjit_c --> src_backend_access_common_tupdesc_c
    src_backend_jit_llvm_llvmjit_c --> src_backend_jit_jit_c
    src_backend_jit_llvm_llvmjit_c --> src_backend_storage_ipc_ipc_c
    src_backend_jit_llvm_llvmjit_c --> src_backend_utils_fmgr_fmgr_c
    src_backend_jit_llvm_llvmjit_c --> src_backend_utils_resowner_resowner_c
    src_backend_jit_llvm_llvmjit_c --> src_common_instr_time_c
    src_backend_jit_llvm_llvmjit_c --> src_include_jit_llvmjit_backport_h
    src_backend_jit_llvm_llvmjit_c --> src_include_jit_llvmjit_emit_h
    src_backend_jit_llvm_llvmjit_c --> src_include_nodes_pg_list_h
    src_backend_jit_llvm_llvmjit_deform_c --> src_backend_jit_llvm_llvmjit_c
    src_backend_jit_llvm_llvmjit_deform_c --> src_include_access_tupdesc_details_h
    src_backend_jit_llvm_llvmjit_deform_c --> src_include_executor_tuptable_h
    src_backend_jit_llvm_llvmjit_deform_c --> src_include_jit_llvmjit_emit_h
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_access_nbtree_nbtree_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_catalog_objectaccess_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_executor_execExpr_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_executor_nodeAgg_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_executor_nodeSubplan_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_jit_llvm_llvmjit_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_nodes_makefuncs_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_nodes_nodeFuncs_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_parser_parse_coerce_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_utils_adt_acl_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_utils_adt_date_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_utils_adt_timestamp_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_utils_adt_xml_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_utils_cache_typcache_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_backend_utils_fmgr_funcapi_c
    src_backend_jit_llvm_llvmjit_expr_c --> src_include_executor_execdebug_h
    src_backend_jit_llvm_llvmjit_expr_c --> src_include_jit_llvmjit_emit_h
    src_backend_jit_llvm_llvmjit_expr_c --> src_include_parser_parsetree_h
    src_backend_jit_llvm_llvmjit_expr_c --> src_include_utils_fmgrtab_h
    src_backend_jit_llvm_llvmjit_types_c --> src_backend_access_common_tupdesc_c
    src_backend_jit_llvm_llvmjit_types_c --> src_backend_executor_execExpr_c
    src_backend_jit_llvm_llvmjit_types_c --> src_backend_executor_nodeAgg_c
    src_backend_jit_llvm_llvmjit_types_c --> src_backend_utils_adt_expandeddatum_c
    src_backend_jit_llvm_llvmjit_types_c --> src_backend_utils_fmgr_fmgr_c
    src_backend_jit_llvm_llvmjit_types_c --> src_include_access_htup_h
    src_backend_jit_llvm_llvmjit_types_c --> src_include_catalog_pg_attribute_h
    src_backend_jit_llvm_llvmjit_types_c --> src_include_executor_tuptable_h
    src_backend_jit_llvm_llvmjit_types_c --> src_include_nodes_execnodes_h
    src_backend_jit_llvm_llvmjit_types_c --> src_include_nodes_memnodes_h
    src_backend_jit_llvm_llvmjit_types_c --> src_include_utils_palloc_h
```
