# `tcop` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "access"
        src_backend_access_common_printsimple_c["common/printsimple.c"]
        src_backend_access_common_printtup_c["common/printtup.c"]
        src_backend_access_common_reloptions_c["common/reloptions.c"]
        src_backend_access_transam_parallel_c["transam/parallel.c"]
        src_backend_access_transam_twophase_c["transam/twophase.c"]
        src_backend_access_transam_xlog_c["transam/xlog.c"]
        src_backend_access_transam_xlogrecovery_c["transam/xlogrecovery.c"]
    end
    subgraph "catalog"
        src_backend_catalog_namespace_c["namespace.c"]
        src_backend_catalog_objectaccess_c["objectaccess.c"]
        src_backend_catalog_pg_inherits_c["pg_inherits.c"]
        src_backend_catalog_pg_namespace_c["pg_namespace.c"]
        src_backend_catalog_pg_proc_c["pg_proc.c"]
        src_backend_catalog_toasting_c["toasting.c"]
    end
    subgraph "commands"
        src_backend_commands_alter_c["alter.c"]
        src_backend_commands_async_c["async.c"]
        src_backend_commands_collationcmds_c["collationcmds.c"]
        src_backend_commands_comment_c["comment.c"]
        src_backend_commands_conversioncmds_c["conversioncmds.c"]
        src_backend_commands_copy_c["copy.c"]
        src_backend_commands_createas_c["createas.c"]
        src_backend_commands_dbcommands_c["dbcommands.c"]
        src_backend_commands_discard_c["discard.c"]
        src_backend_commands_event_trigger_c["event_trigger.c"]
        src_backend_commands_explain_c["explain.c"]
        src_backend_commands_explain_dr_c["explain_dr.c"]
        src_backend_commands_explain_state_c["explain_state.c"]
        src_backend_commands_extension_c["extension.c"]
        src_backend_commands_lockcmds_c["lockcmds.c"]
        src_backend_commands_matview_c["matview.c"]
        src_backend_commands_policy_c["policy.c"]
        src_backend_commands_portalcmds_c["portalcmds.c"]
        src_backend_commands_prepare_c["prepare.c"]
        src_backend_commands_proclang_c["proclang.c"]
        src_backend_commands_propgraphcmds_c["propgraphcmds.c"]
        src_backend_commands_publicationcmds_c["publicationcmds.c"]
        src_backend_commands_repack_c["repack.c"]
        src_backend_commands_schemacmds_c["schemacmds.c"]
        src_backend_commands_seclabel_c["seclabel.c"]
        src_backend_commands_sequence_c["sequence.c"]
        src_backend_commands_subscriptioncmds_c["subscriptioncmds.c"]
        src_backend_commands_tablecmds_c["tablecmds.c"]
        src_backend_commands_tablespace_c["tablespace.c"]
        src_backend_commands_trigger_c["trigger.c"]
        src_backend_commands_typecmds_c["typecmds.c"]
        src_backend_commands_user_c["user.c"]
        src_backend_commands_vacuum_c["vacuum.c"]
        src_backend_commands_view_c["view.c"]
        src_backend_commands_wait_c["wait.c"]
    end
    subgraph "common"
        src_common_ip_c["ip.c"]
        src_common_pg_prng_c["pg_prng.c"]
        src_common_string_c["string.c"]
        src_common_stringinfo_c["stringinfo.c"]
    end
    subgraph "executor"
        src_backend_executor_functions_c["functions.c"]
        src_backend_executor_tqueue_c["tqueue.c"]
        src_backend_executor_tstoreReceiver_c["tstoreReceiver.c"]
    end
    subgraph "include/catalog"
        src_include_catalog_pg_authid_h["pg_authid.h"]
    end
    subgraph "include/commands"
        src_include_commands_defrem_h["defrem.h"]
    end
    subgraph "include/executor"
        src_include_executor_executor_h["executor.h"]
        src_include_executor_tuptable_h["tuptable.h"]
    end
    subgraph "include/libpq"
        src_include_libpq_libpq_be_h["libpq-be.h"]
        src_include_libpq_libpq_h["libpq.h"]
        src_include_libpq_protocol_h["protocol.h"]
    end
    subgraph "include/mb"
        src_include_mb_pg_wchar_h["pg_wchar.h"]
    end
    subgraph "include/nodes"
        src_include_nodes_parsenodes_h["parsenodes.h"]
    end
    subgraph "include/optimizer"
        src_include_optimizer_optimizer_h["optimizer.h"]
    end
    subgraph "include/port"
        src_include_port_win32_sys_resource_h["win32/sys/resource.h"]
        src_include_port_win32_sys_socket_h["win32/sys/socket.h"]
        src_include_port_win32_msvc_sys_time_h["win32_msvc/sys/time.h"]
        src_include_port_win32_msvc_unistd_h["win32_msvc/unistd.h"]
    end
    subgraph "include/replication"
        src_include_replication_logicallauncher_h["logicallauncher.h"]
        src_include_replication_logicalworker_h["logicalworker.h"]
    end
    subgraph "include/storage"
        src_include_storage_shmem_internal_h["shmem_internal.h"]
    end
    subgraph "include/tcop"
        src_include_tcop_cmdtaglist_h["cmdtaglist.h"]
        src_include_tcop_tcopprot_h["tcopprot.h"]
    end
    subgraph "include/top"
        src_include_c_h["c.h"]
        src_include_pg_trace_h["pg_trace.h"]
    end
    subgraph "include/utils"
        src_include_utils_guc_hooks_h["guc_hooks.h"]
        src_include_utils_palloc_h["palloc.h"]
        src_include_utils_portal_h["portal.h"]
    end
    subgraph "jit"
        src_backend_jit_jit_c["jit.c"]
    end
    subgraph "libpq"
        src_backend_libpq_pqformat_c["pqformat.c"]
        src_backend_libpq_pqsignal_c["pqsignal.c"]
    end
    subgraph "nodes"
        src_backend_nodes_print_c["print.c"]
    end
    subgraph "parser"
        src_backend_parser_analyze_c["analyze.c"]
        src_backend_parser_parse_utilcmd_c["parse_utilcmd.c"]
        src_backend_parser_parser_c["parser.c"]
    end
    subgraph "port"
        src_port_pg_getopt_ctx_c["pg_getopt_ctx.c"]
    end
    subgraph "postmaster"
        src_backend_postmaster_bgwriter_c["bgwriter.c"]
        src_backend_postmaster_interrupt_c["interrupt.c"]
        src_backend_postmaster_postmaster_c["postmaster.c"]
    end
    subgraph "replication"
        src_backend_replication_logical_slotsync_c["logical/slotsync.c"]
        src_backend_replication_slot_c["slot.c"]
        src_backend_replication_walsender_c["walsender.c"]
    end
    subgraph "rewrite"
        src_backend_rewrite_rewriteDefine_c["rewriteDefine.c"]
        src_backend_rewrite_rewriteHandler_c["rewriteHandler.c"]
    end
    subgraph "storage"
        src_backend_storage_buffer_bufmgr_c["buffer/bufmgr.c"]
        src_backend_storage_file_fd_c["file/fd.c"]
        src_backend_storage_ipc_ipc_c["ipc/ipc.c"]
        src_backend_storage_ipc_pmsignal_c["ipc/pmsignal.c"]
        src_backend_storage_ipc_procsignal_c["ipc/procsignal.c"]
        src_backend_storage_ipc_sinval_c["ipc/sinval.c"]
        src_backend_storage_ipc_standby_c["ipc/standby.c"]
        src_backend_storage_lmgr_proc_c["lmgr/proc.c"]
    end
    subgraph "tcop"
        src_backend_tcop_backend_startup_c["backend_startup.c"]
        src_backend_tcop_cmdtag_c["cmdtag.c"]
        src_backend_tcop_dest_c["dest.c"]
        src_backend_tcop_fastpath_c["fastpath.c"]
        src_backend_tcop_postgres_c["postgres.c"]
        src_backend_tcop_pquery_c["pquery.c"]
        src_backend_tcop_utility_c["utility.c"]
    end
    subgraph "utils"
        src_backend_utils_adt_acl_c["adt/acl.c"]
        src_backend_utils_adt_timestamp_c["adt/timestamp.c"]
        src_backend_utils_adt_varlena_c["adt/varlena.c"]
        src_backend_utils_error_elog_c["error/elog.c"]
        src_backend_utils_mb_stringinfo_mb_c["mb/stringinfo_mb.c"]
        src_backend_utils_misc_guc_c["misc/guc.c"]
        src_backend_utils_misc_injection_point_c["misc/injection_point.c"]
        src_backend_utils_misc_ps_status_c["misc/ps_status.c"]
        src_backend_utils_misc_timeout_c["misc/timeout.c"]
        src_backend_utils_time_snapmgr_c["time/snapmgr.c"]
    end
    src_backend_tcop_backend_startup_c --> src_backend_access_transam_xlog_c
    src_backend_tcop_backend_startup_c --> src_backend_access_transam_xlogrecovery_c
    src_backend_tcop_backend_startup_c --> src_backend_libpq_pqformat_c
    src_backend_tcop_backend_startup_c --> src_backend_libpq_pqsignal_c
    src_backend_tcop_backend_startup_c --> src_backend_postmaster_postmaster_c
    src_backend_tcop_backend_startup_c --> src_backend_replication_walsender_c
    src_backend_tcop_backend_startup_c --> src_backend_storage_file_fd_c
    src_backend_tcop_backend_startup_c --> src_backend_storage_ipc_ipc_c
    src_backend_tcop_backend_startup_c --> src_backend_storage_ipc_procsignal_c
    src_backend_tcop_backend_startup_c --> src_backend_storage_lmgr_proc_c
    src_backend_tcop_backend_startup_c --> src_backend_utils_adt_timestamp_c
    src_backend_tcop_backend_startup_c --> src_backend_utils_adt_varlena_c
    src_backend_tcop_backend_startup_c --> src_backend_utils_misc_injection_point_c
    src_backend_tcop_backend_startup_c --> src_backend_utils_misc_ps_status_c
    src_backend_tcop_backend_startup_c --> src_backend_utils_misc_timeout_c
    src_backend_tcop_backend_startup_c --> src_common_ip_c
    src_backend_tcop_backend_startup_c --> src_common_string_c
    src_backend_tcop_backend_startup_c --> src_include_libpq_libpq_be_h
    src_backend_tcop_backend_startup_c --> src_include_libpq_libpq_h
    src_backend_tcop_backend_startup_c --> src_include_port_win32_msvc_unistd_h
    src_backend_tcop_backend_startup_c --> src_include_tcop_tcopprot_h
    src_backend_tcop_backend_startup_c --> src_include_utils_guc_hooks_h
    src_backend_tcop_cmdtag_c --> src_include_tcop_cmdtaglist_h
    src_backend_tcop_dest_c --> src_backend_access_common_printsimple_c
    src_backend_tcop_dest_c --> src_backend_access_common_printtup_c
    src_backend_tcop_dest_c --> src_backend_commands_copy_c
    src_backend_tcop_dest_c --> src_backend_commands_createas_c
    src_backend_tcop_dest_c --> src_backend_commands_explain_dr_c
    src_backend_tcop_dest_c --> src_backend_commands_matview_c
    src_backend_tcop_dest_c --> src_backend_executor_functions_c
    src_backend_tcop_dest_c --> src_backend_executor_tqueue_c
    src_backend_tcop_dest_c --> src_backend_executor_tstoreReceiver_c
    src_backend_tcop_dest_c --> src_backend_libpq_pqformat_c
    src_backend_tcop_dest_c --> src_backend_tcop_cmdtag_c
    src_backend_tcop_dest_c --> src_include_executor_tuptable_h
    src_backend_tcop_dest_c --> src_include_libpq_libpq_h
    src_backend_tcop_fastpath_c --> src_backend_catalog_objectaccess_c
    src_backend_tcop_fastpath_c --> src_backend_catalog_pg_namespace_c
    src_backend_tcop_fastpath_c --> src_backend_catalog_pg_proc_c
    src_backend_tcop_fastpath_c --> src_backend_libpq_pqformat_c
    src_backend_tcop_fastpath_c --> src_backend_utils_adt_acl_c
    src_backend_tcop_fastpath_c --> src_backend_utils_time_snapmgr_c
    src_backend_tcop_fastpath_c --> src_common_stringinfo_c
    src_backend_tcop_fastpath_c --> src_include_libpq_protocol_h
    src_backend_tcop_fastpath_c --> src_include_mb_pg_wchar_h
    src_backend_tcop_fastpath_c --> src_include_tcop_tcopprot_h
    src_backend_tcop_postgres_c --> src_backend_access_common_printtup_c
    src_backend_tcop_postgres_c --> src_backend_access_transam_parallel_c
    src_backend_tcop_postgres_c --> src_backend_commands_async_c
    src_backend_tcop_postgres_c --> src_backend_commands_event_trigger_c
    src_backend_tcop_postgres_c --> src_backend_commands_explain_state_c
    src_backend_tcop_postgres_c --> src_backend_commands_prepare_c
    src_backend_tcop_postgres_c --> src_backend_commands_repack_c
    src_backend_tcop_postgres_c --> src_backend_jit_jit_c
    src_backend_tcop_postgres_c --> src_backend_libpq_pqformat_c
    src_backend_tcop_postgres_c --> src_backend_libpq_pqsignal_c
    src_backend_tcop_postgres_c --> src_backend_nodes_print_c
    src_backend_tcop_postgres_c --> src_backend_parser_analyze_c
    src_backend_tcop_postgres_c --> src_backend_parser_parser_c
    src_backend_tcop_postgres_c --> src_backend_postmaster_interrupt_c
    src_backend_tcop_postgres_c --> src_backend_postmaster_postmaster_c
    src_backend_tcop_postgres_c --> src_backend_replication_logical_slotsync_c
    src_backend_tcop_postgres_c --> src_backend_replication_slot_c
    src_backend_tcop_postgres_c --> src_backend_replication_walsender_c
    src_backend_tcop_postgres_c --> src_backend_rewrite_rewriteHandler_c
    src_backend_tcop_postgres_c --> src_backend_storage_buffer_bufmgr_c
    src_backend_tcop_postgres_c --> src_backend_storage_file_fd_c
    src_backend_tcop_postgres_c --> src_backend_storage_ipc_ipc_c
    src_backend_tcop_postgres_c --> src_backend_storage_ipc_pmsignal_c
    src_backend_tcop_postgres_c --> src_backend_storage_ipc_procsignal_c
    src_backend_tcop_postgres_c --> src_backend_storage_ipc_sinval_c
    src_backend_tcop_postgres_c --> src_backend_storage_ipc_standby_c
    src_backend_tcop_postgres_c --> src_backend_storage_lmgr_proc_c
    src_backend_tcop_postgres_c --> src_backend_tcop_backend_startup_c
    src_backend_tcop_postgres_c --> src_backend_tcop_fastpath_c
    src_backend_tcop_postgres_c --> src_backend_tcop_pquery_c
    src_backend_tcop_postgres_c --> src_backend_tcop_utility_c
    src_backend_tcop_postgres_c --> src_backend_utils_adt_timestamp_c
    src_backend_tcop_postgres_c --> src_backend_utils_adt_varlena_c
    src_backend_tcop_postgres_c --> src_backend_utils_error_elog_c
    src_backend_tcop_postgres_c --> src_backend_utils_mb_stringinfo_mb_c
    src_backend_tcop_postgres_c --> src_backend_utils_misc_injection_point_c
    src_backend_tcop_postgres_c --> src_backend_utils_misc_ps_status_c
    src_backend_tcop_postgres_c --> src_backend_utils_misc_timeout_c
    src_backend_tcop_postgres_c --> src_backend_utils_time_snapmgr_c
    src_backend_tcop_postgres_c --> src_common_pg_prng_c
    src_backend_tcop_postgres_c --> src_include_c_h
    src_backend_tcop_postgres_c --> src_include_libpq_libpq_h
    src_backend_tcop_postgres_c --> src_include_mb_pg_wchar_h
    src_backend_tcop_postgres_c --> src_include_optimizer_optimizer_h
    src_backend_tcop_postgres_c --> src_include_pg_trace_h
    src_backend_tcop_postgres_c --> src_include_port_win32_sys_resource_h
    src_backend_tcop_postgres_c --> src_include_port_win32_sys_socket_h
    src_backend_tcop_postgres_c --> src_include_port_win32_msvc_sys_time_h
    src_backend_tcop_postgres_c --> src_include_port_win32_msvc_unistd_h
    src_backend_tcop_postgres_c --> src_include_replication_logicallauncher_h
    src_backend_tcop_postgres_c --> src_include_replication_logicalworker_h
    src_backend_tcop_postgres_c --> src_include_storage_shmem_internal_h
    src_backend_tcop_postgres_c --> src_include_tcop_tcopprot_h
    src_backend_tcop_postgres_c --> src_include_utils_guc_hooks_h
    src_backend_tcop_postgres_c --> src_include_utils_palloc_h
    src_backend_tcop_postgres_c --> src_port_pg_getopt_ctx_c
    src_backend_tcop_pquery_c --> src_backend_commands_prepare_c
    src_backend_tcop_pquery_c --> src_backend_executor_tstoreReceiver_c
    src_backend_tcop_pquery_c --> src_backend_tcop_utility_c
    src_backend_tcop_pquery_c --> src_backend_utils_time_snapmgr_c
    src_backend_tcop_pquery_c --> src_include_executor_executor_h
    src_backend_tcop_pquery_c --> src_include_nodes_parsenodes_h
    src_backend_tcop_pquery_c --> src_include_pg_trace_h
    src_backend_tcop_pquery_c --> src_include_utils_portal_h
    src_backend_tcop_utility_c --> src_backend_access_common_reloptions_c
    src_backend_tcop_utility_c --> src_backend_access_transam_twophase_c
    src_backend_tcop_utility_c --> src_backend_access_transam_xlog_c
    src_backend_tcop_utility_c --> src_backend_catalog_namespace_c
    src_backend_tcop_utility_c --> src_backend_catalog_pg_inherits_c
    src_backend_tcop_utility_c --> src_backend_catalog_toasting_c
    src_backend_tcop_utility_c --> src_backend_commands_alter_c
    src_backend_tcop_utility_c --> src_backend_commands_async_c
    src_backend_tcop_utility_c --> src_backend_commands_collationcmds_c
    src_backend_tcop_utility_c --> src_backend_commands_comment_c
    src_backend_tcop_utility_c --> src_backend_commands_conversioncmds_c
    src_backend_tcop_utility_c --> src_backend_commands_copy_c
    src_backend_tcop_utility_c --> src_backend_commands_createas_c
    src_backend_tcop_utility_c --> src_backend_commands_dbcommands_c
    src_backend_tcop_utility_c --> src_backend_commands_discard_c
    src_backend_tcop_utility_c --> src_backend_commands_event_trigger_c
    src_backend_tcop_utility_c --> src_backend_commands_explain_c
    src_backend_tcop_utility_c --> src_backend_commands_extension_c
    src_backend_tcop_utility_c --> src_backend_commands_lockcmds_c
    src_backend_tcop_utility_c --> src_backend_commands_matview_c
    src_backend_tcop_utility_c --> src_backend_commands_policy_c
    src_backend_tcop_utility_c --> src_backend_commands_portalcmds_c
    src_backend_tcop_utility_c --> src_backend_commands_prepare_c
    src_backend_tcop_utility_c --> src_backend_commands_proclang_c
    src_backend_tcop_utility_c --> src_backend_commands_propgraphcmds_c
    src_backend_tcop_utility_c --> src_backend_commands_publicationcmds_c
    src_backend_tcop_utility_c --> src_backend_commands_repack_c
    src_backend_tcop_utility_c --> src_backend_commands_schemacmds_c
    src_backend_tcop_utility_c --> src_backend_commands_seclabel_c
    src_backend_tcop_utility_c --> src_backend_commands_sequence_c
    src_backend_tcop_utility_c --> src_backend_commands_subscriptioncmds_c
    src_backend_tcop_utility_c --> src_backend_commands_tablecmds_c
    src_backend_tcop_utility_c --> src_backend_commands_tablespace_c
    src_backend_tcop_utility_c --> src_backend_commands_trigger_c
    src_backend_tcop_utility_c --> src_backend_commands_typecmds_c
    src_backend_tcop_utility_c --> src_backend_commands_user_c
    src_backend_tcop_utility_c --> src_backend_commands_vacuum_c
    src_backend_tcop_utility_c --> src_backend_commands_view_c
    src_backend_tcop_utility_c --> src_backend_commands_wait_c
    src_backend_tcop_utility_c --> src_backend_parser_parse_utilcmd_c
    src_backend_tcop_utility_c --> src_backend_postmaster_bgwriter_c
    src_backend_tcop_utility_c --> src_backend_rewrite_rewriteDefine_c
    src_backend_tcop_utility_c --> src_backend_storage_file_fd_c
    src_backend_tcop_utility_c --> src_backend_tcop_cmdtag_c
    src_backend_tcop_utility_c --> src_backend_utils_adt_acl_c
    src_backend_tcop_utility_c --> src_backend_utils_misc_guc_c
    src_backend_tcop_utility_c --> src_include_catalog_pg_authid_h
    src_backend_tcop_utility_c --> src_include_commands_defrem_h
    src_backend_tcop_utility_c --> src_include_tcop_tcopprot_h
```
