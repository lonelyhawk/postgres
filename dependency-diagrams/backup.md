# `backup` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "access"
        src_backend_access_common_tupdesc_c["common/tupdesc.c"]
        src_backend_access_transam_timeline_c["transam/timeline.c"]
        src_backend_access_transam_xlog_c["transam/xlog.c"]
        src_backend_access_transam_xlogbackup_c["transam/xlogbackup.c"]
    end
    subgraph "backup"
        src_backend_backup_backup_manifest_c["backup_manifest.c"]
        src_backend_backup_basebackup_c["basebackup.c"]
        src_backend_backup_basebackup_copy_c["basebackup_copy.c"]
        src_backend_backup_basebackup_gzip_c["basebackup_gzip.c"]
        src_backend_backup_basebackup_incremental_c["basebackup_incremental.c"]
        src_backend_backup_basebackup_lz4_c["basebackup_lz4.c"]
        src_backend_backup_basebackup_progress_c["basebackup_progress.c"]
        src_backend_backup_basebackup_server_c["basebackup_server.c"]
        src_backend_backup_basebackup_sink_c["basebackup_sink.c"]
        src_backend_backup_basebackup_target_c["basebackup_target.c"]
        src_backend_backup_basebackup_throttle_c["basebackup_throttle.c"]
        src_backend_backup_basebackup_zstd_c["basebackup_zstd.c"]
        src_backend_backup_walsummary_c["walsummary.c"]
        src_backend_backup_walsummaryfuncs_c["walsummaryfuncs.c"]
    end
    subgraph "common"
        src_common_blkreftable_c["blkreftable.c"]
        src_common_checksum_helper_c["checksum_helper.c"]
        src_common_compression_c["compression.c"]
        src_common_file_perm_c["file_perm.c"]
        src_common_file_utils_c["file_utils.c"]
        src_common_hashfn_c["hashfn.c"]
        src_common_parse_manifest_c["parse_manifest.c"]
        src_common_relpath_c["relpath.c"]
        src_common_stringinfo_c["stringinfo.c"]
    end
    subgraph "include/access"
        src_include_access_xlog_internal_h["xlog_internal.h"]
        src_include_access_xlogdefs_h["xlogdefs.h"]
    end
    subgraph "include/catalog"
        src_include_catalog_pg_authid_h["pg_authid.h"]
    end
    subgraph "include/commands"
        src_include_commands_defrem_h["defrem.h"]
        src_include_commands_progress_h["progress.h"]
    end
    subgraph "include/executor"
        src_include_executor_executor_h["executor.h"]
    end
    subgraph "include/lib"
        src_include_lib_simplehash_h["simplehash.h"]
    end
    subgraph "include/libpq"
        src_include_libpq_libpq_h["libpq.h"]
    end
    subgraph "include/mb"
        src_include_mb_pg_wchar_h["pg_wchar.h"]
    end
    subgraph "include/nodes"
        src_include_nodes_pg_list_h["pg_list.h"]
        src_include_nodes_replnodes_h["replnodes.h"]
    end
    subgraph "include/port"
        src_include_port_win32_msvc_sys_time_h["win32_msvc/sys/time.h"]
        src_include_port_win32_msvc_unistd_h["win32_msvc/unistd.h"]
    end
    subgraph "include/replication"
        src_include_replication_walsender_private_h["walsender_private.h"]
    end
    subgraph "include/storage"
        src_include_storage_block_h["block.h"]
    end
    subgraph "include/top"
        src_include_pgtar_h["pgtar.h"]
        src_include_pgtime_h["pgtime.h"]
    end
    subgraph "include/utils"
        src_include_utils_palloc_h["palloc.h"]
    end
    subgraph "libpq"
        src_backend_libpq_pqformat_c["pqformat.c"]
    end
    subgraph "postmaster"
        src_backend_postmaster_syslogger_c["syslogger.c"]
        src_backend_postmaster_walsummarizer_c["walsummarizer.c"]
    end
    subgraph "replication"
        src_backend_replication_slot_c["slot.c"]
        src_backend_replication_walsender_c["walsender.c"]
    end
    subgraph "storage"
        src_backend_storage_file_buffile_c["file/buffile.c"]
        src_backend_storage_file_fd_c["file/fd.c"]
        src_backend_storage_file_reinit_c["file/reinit.c"]
        src_backend_storage_ipc_dsm_impl_c["ipc/dsm_impl.c"]
        src_backend_storage_ipc_ipc_c["ipc/ipc.c"]
        src_backend_storage_ipc_latch_c["ipc/latch.c"]
        src_backend_storage_page_bufpage_c["page/bufpage.c"]
        src_backend_storage_page_checksum_c["page/checksum.c"]
    end
    subgraph "tcop"
        src_backend_tcop_dest_c["dest.c"]
    end
    subgraph "utils"
        src_backend_utils_activity_wait_event_c["activity/wait_event.c"]
        src_backend_utils_adt_acl_c["adt/acl.c"]
        src_backend_utils_adt_int_c["adt/int.c"]
        src_backend_utils_adt_json_c["adt/json.c"]
        src_backend_utils_adt_pg_lsn_c["adt/pg_lsn.c"]
        src_backend_utils_adt_timestamp_c["adt/timestamp.c"]
        src_backend_utils_cache_relcache_c["cache/relcache.c"]
        src_backend_utils_fmgr_funcapi_c["fmgr/funcapi.c"]
        src_backend_utils_misc_guc_c["misc/guc.c"]
        src_backend_utils_misc_ps_status_c["misc/ps_status.c"]
        src_backend_utils_resowner_resowner_c["resowner/resowner.c"]
        src_backend_utils_sort_tuplestore_c["sort/tuplestore.c"]
    end
    src_backend_backup_backup_manifest_c --> src_backend_access_transam_timeline_c
    src_backend_backup_backup_manifest_c --> src_backend_access_transam_xlog_c
    src_backend_backup_backup_manifest_c --> src_backend_backup_basebackup_sink_c
    src_backend_backup_backup_manifest_c --> src_backend_storage_file_buffile_c
    src_backend_backup_backup_manifest_c --> src_backend_utils_adt_json_c
    src_backend_backup_backup_manifest_c --> src_common_checksum_helper_c
    src_backend_backup_backup_manifest_c --> src_common_relpath_c
    src_backend_backup_backup_manifest_c --> src_include_mb_pg_wchar_h
    src_backend_backup_backup_manifest_c --> src_include_pgtime_h
    src_backend_backup_basebackup_c --> src_backend_access_transam_xlogbackup_c
    src_backend_backup_basebackup_c --> src_backend_backup_backup_manifest_c
    src_backend_backup_basebackup_c --> src_backend_backup_basebackup_incremental_c
    src_backend_backup_basebackup_c --> src_backend_backup_basebackup_sink_c
    src_backend_backup_basebackup_c --> src_backend_backup_basebackup_target_c
    src_backend_backup_basebackup_c --> src_backend_postmaster_syslogger_c
    src_backend_backup_basebackup_c --> src_backend_postmaster_walsummarizer_c
    src_backend_backup_basebackup_c --> src_backend_replication_slot_c
    src_backend_backup_basebackup_c --> src_backend_replication_walsender_c
    src_backend_backup_basebackup_c --> src_backend_storage_file_reinit_c
    src_backend_backup_basebackup_c --> src_backend_storage_ipc_dsm_impl_c
    src_backend_backup_basebackup_c --> src_backend_storage_ipc_ipc_c
    src_backend_backup_basebackup_c --> src_backend_storage_page_bufpage_c
    src_backend_backup_basebackup_c --> src_backend_storage_page_checksum_c
    src_backend_backup_basebackup_c --> src_backend_utils_activity_wait_event_c
    src_backend_backup_basebackup_c --> src_backend_utils_cache_relcache_c
    src_backend_backup_basebackup_c --> src_backend_utils_misc_guc_c
    src_backend_backup_basebackup_c --> src_backend_utils_misc_ps_status_c
    src_backend_backup_basebackup_c --> src_backend_utils_resowner_resowner_c
    src_backend_backup_basebackup_c --> src_common_compression_c
    src_backend_backup_basebackup_c --> src_common_file_perm_c
    src_backend_backup_basebackup_c --> src_common_file_utils_c
    src_backend_backup_basebackup_c --> src_common_stringinfo_c
    src_backend_backup_basebackup_c --> src_include_access_xlog_internal_h
    src_backend_backup_basebackup_c --> src_include_commands_defrem_h
    src_backend_backup_basebackup_c --> src_include_nodes_pg_list_h
    src_backend_backup_basebackup_c --> src_include_nodes_replnodes_h
    src_backend_backup_basebackup_c --> src_include_pgtar_h
    src_backend_backup_basebackup_c --> src_include_port_win32_msvc_sys_time_h
    src_backend_backup_basebackup_c --> src_include_port_win32_msvc_unistd_h
    src_backend_backup_basebackup_c --> src_include_replication_walsender_private_h
    src_backend_backup_basebackup_copy_c --> src_backend_access_common_tupdesc_c
    src_backend_backup_basebackup_copy_c --> src_backend_backup_basebackup_c
    src_backend_backup_basebackup_copy_c --> src_backend_backup_basebackup_sink_c
    src_backend_backup_basebackup_copy_c --> src_backend_libpq_pqformat_c
    src_backend_backup_basebackup_copy_c --> src_backend_tcop_dest_c
    src_backend_backup_basebackup_copy_c --> src_backend_utils_adt_timestamp_c
    src_backend_backup_basebackup_copy_c --> src_include_executor_executor_h
    src_backend_backup_basebackup_copy_c --> src_include_libpq_libpq_h
    src_backend_backup_basebackup_gzip_c --> src_backend_backup_basebackup_sink_c
    src_backend_backup_basebackup_incremental_c --> src_backend_access_transam_timeline_c
    src_backend_backup_basebackup_incremental_c --> src_backend_access_transam_xlog_c
    src_backend_backup_basebackup_incremental_c --> src_backend_access_transam_xlogbackup_c
    src_backend_backup_basebackup_incremental_c --> src_backend_backup_walsummary_c
    src_backend_backup_basebackup_incremental_c --> src_backend_postmaster_walsummarizer_c
    src_backend_backup_basebackup_incremental_c --> src_backend_utils_adt_int_c
    src_backend_backup_basebackup_incremental_c --> src_common_blkreftable_c
    src_backend_backup_basebackup_incremental_c --> src_common_hashfn_c
    src_backend_backup_basebackup_incremental_c --> src_common_parse_manifest_c
    src_backend_backup_basebackup_incremental_c --> src_common_relpath_c
    src_backend_backup_basebackup_incremental_c --> src_include_lib_simplehash_h
    src_backend_backup_basebackup_incremental_c --> src_include_storage_block_h
    src_backend_backup_basebackup_incremental_c --> src_include_utils_palloc_h
    src_backend_backup_basebackup_lz4_c --> src_backend_backup_basebackup_sink_c
    src_backend_backup_basebackup_progress_c --> src_backend_backup_basebackup_sink_c
    src_backend_backup_basebackup_progress_c --> src_include_commands_progress_h
    src_backend_backup_basebackup_server_c --> src_backend_backup_basebackup_sink_c
    src_backend_backup_basebackup_server_c --> src_backend_storage_file_fd_c
    src_backend_backup_basebackup_server_c --> src_backend_utils_activity_wait_event_c
    src_backend_backup_basebackup_server_c --> src_backend_utils_adt_acl_c
    src_backend_backup_basebackup_server_c --> src_include_catalog_pg_authid_h
    src_backend_backup_basebackup_sink_c --> src_common_compression_c
    src_backend_backup_basebackup_sink_c --> src_include_access_xlogdefs_h
    src_backend_backup_basebackup_sink_c --> src_include_nodes_pg_list_h
    src_backend_backup_basebackup_target_c --> src_backend_backup_basebackup_sink_c
    src_backend_backup_basebackup_throttle_c --> src_backend_backup_basebackup_sink_c
    src_backend_backup_basebackup_throttle_c --> src_backend_storage_ipc_latch_c
    src_backend_backup_basebackup_throttle_c --> src_backend_utils_activity_wait_event_c
    src_backend_backup_basebackup_throttle_c --> src_backend_utils_adt_timestamp_c
    src_backend_backup_basebackup_zstd_c --> src_backend_backup_basebackup_sink_c
    src_backend_backup_walsummary_c --> src_backend_storage_file_fd_c
    src_backend_backup_walsummary_c --> src_backend_utils_activity_wait_event_c
    src_backend_backup_walsummary_c --> src_backend_utils_adt_int_c
    src_backend_backup_walsummary_c --> src_include_access_xlog_internal_h
    src_backend_backup_walsummary_c --> src_include_access_xlogdefs_h
    src_backend_backup_walsummary_c --> src_include_nodes_pg_list_h
    src_backend_backup_walsummary_c --> src_include_port_win32_msvc_sys_time_h
    src_backend_backup_walsummary_c --> src_include_port_win32_msvc_unistd_h
    src_backend_backup_walsummaryfuncs_c --> src_backend_backup_walsummary_c
    src_backend_backup_walsummaryfuncs_c --> src_backend_postmaster_walsummarizer_c
    src_backend_backup_walsummaryfuncs_c --> src_backend_utils_adt_pg_lsn_c
    src_backend_backup_walsummaryfuncs_c --> src_backend_utils_fmgr_funcapi_c
    src_backend_backup_walsummaryfuncs_c --> src_backend_utils_sort_tuplestore_c
    src_backend_backup_walsummaryfuncs_c --> src_common_blkreftable_c
```
