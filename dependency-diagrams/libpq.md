# `libpq` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "access"
        src_backend_access_transam_parallel_c["transam/parallel.c"]
        src_backend_access_transam_xlog_c["transam/xlog.c"]
    end
    subgraph "catalog"
        src_backend_catalog_pg_collation_c["pg_collation.c"]
        src_backend_catalog_pg_largeobject_c["pg_largeobject.c"]
    end
    subgraph "commands"
        src_backend_commands_repack_c["repack.c"]
        src_backend_commands_user_c["user.c"]
    end
    subgraph "common"
        src_common_base64_c["base64.c"]
        src_common_hashfn_c["hashfn.c"]
        src_common_hmac_c["hmac.c"]
        src_common_ip_c["ip.c"]
        src_common_md5_c["md5.c"]
        src_common_percentrepl_c["percentrepl.c"]
        src_common_saslprep_c["saslprep.c"]
        src_common_scram_common_c["scram-common.c"]
        src_common_sha2_c["sha2.c"]
        src_common_string_c["string.c"]
        src_common_stringinfo_c["stringinfo.c"]
    end
    subgraph "include/catalog"
        src_include_catalog_pg_authid_h["pg_authid.h"]
        src_include_catalog_pg_control_h["pg_control.h"]
    end
    subgraph "include/common"
        src_include_common_oauth_common_h["oauth-common.h"]
        src_include_common_openssl_h["openssl.h"]
    end
    subgraph "include/lib"
        src_include_lib_simplehash_h["simplehash.h"]
    end
    subgraph "include/libpq"
        src_include_libpq_libpq_be_h["libpq-be.h"]
        src_include_libpq_libpq_fs_h["libpq-fs.h"]
        src_include_libpq_libpq_h["libpq.h"]
        src_include_libpq_oauth_h["oauth.h"]
        src_include_libpq_pg_gssapi_h["pg-gssapi.h"]
        src_include_libpq_protocol_h["protocol.h"]
        src_include_libpq_sasl_h["sasl.h"]
        src_include_libpq_scram_h["scram.h"]
    end
    subgraph "include/mb"
        src_include_mb_pg_wchar_h["pg_wchar.h"]
    end
    subgraph "include/nodes"
        src_include_nodes_pg_list_h["pg_list.h"]
    end
    subgraph "include/port"
        src_include_port_pg_bswap_h["pg_bswap.h"]
        src_include_port_win32_arpa_inet_h["win32/arpa/inet.h"]
        src_include_port_win32_grp_h["win32/grp.h"]
        src_include_port_win32_netdb_h["win32/netdb.h"]
        src_include_port_win32_netinet_in_h["win32/netinet/in.h"]
        src_include_port_win32_netinet_tcp_h["win32/netinet/tcp.h"]
        src_include_port_win32_pwd_h["win32/pwd.h"]
        src_include_port_win32_sys_select_h["win32/sys/select.h"]
        src_include_port_win32_sys_socket_h["win32/sys/socket.h"]
        src_include_port_win32_sys_un_h["win32/sys/un.h"]
        src_include_port_win32_msvc_sys_file_h["win32_msvc/sys/file.h"]
        src_include_port_win32_msvc_sys_param_h["win32_msvc/sys/param.h"]
        src_include_port_win32_msvc_sys_time_h["win32_msvc/sys/time.h"]
        src_include_port_win32_msvc_unistd_h["win32_msvc/unistd.h"]
        src_include_port_win32_msvc_utime_h["win32_msvc/utime.h"]
    end
    subgraph "include/regex"
        src_include_regex_regex_h["regex.h"]
    end
    subgraph "include/replication"
        src_include_replication_logicalworker_h["logicalworker.h"]
    end
    subgraph "include/storage"
        src_include_storage_large_object_h["large_object.h"]
        src_include_storage_procnumber_h["procnumber.h"]
    end
    subgraph "include/tcop"
        src_include_tcop_tcopprot_h["tcopprot.h"]
    end
    subgraph "include/top"
        src_include_varatt_h["varatt.h"]
    end
    subgraph "include/utils"
        src_include_utils_guc_hooks_h["guc_hooks.h"]
    end
    subgraph "libpq"
        src_backend_libpq_auth_oauth_c["auth-oauth.c"]
        src_backend_libpq_auth_sasl_c["auth-sasl.c"]
        src_backend_libpq_auth_scram_c["auth-scram.c"]
        src_backend_libpq_auth_c["auth.c"]
        src_backend_libpq_be_fsstubs_c["be-fsstubs.c"]
        src_backend_libpq_be_gssapi_common_c["be-gssapi-common.c"]
        src_backend_libpq_be_secure_common_c["be-secure-common.c"]
        src_backend_libpq_be_secure_gssapi_c["be-secure-gssapi.c"]
        src_backend_libpq_be_secure_openssl_c["be-secure-openssl.c"]
        src_backend_libpq_be_secure_c["be-secure.c"]
        src_backend_libpq_crypt_c["crypt.c"]
        src_backend_libpq_hba_c["hba.c"]
        src_backend_libpq_ifaddr_c["ifaddr.c"]
        src_backend_libpq_pqcomm_c["pqcomm.c"]
        src_backend_libpq_pqformat_c["pqformat.c"]
        src_backend_libpq_pqmq_c["pqmq.c"]
    end
    subgraph "postmaster"
        src_backend_postmaster_postmaster_c["postmaster.c"]
    end
    subgraph "replication"
        src_backend_replication_walsender_c["walsender.c"]
    end
    subgraph "storage"
        src_backend_storage_file_fd_c["file/fd.c"]
        src_backend_storage_ipc_ipc_c["ipc/ipc.c"]
        src_backend_storage_ipc_latch_c["ipc/latch.c"]
        src_backend_storage_ipc_shm_mq_c["ipc/shm_mq.c"]
    end
    subgraph "tcop"
        src_backend_tcop_backend_startup_c["backend_startup.c"]
    end
    subgraph "utils"
        src_backend_utils_activity_wait_event_c["activity/wait_event.c"]
        src_backend_utils_adt_acl_c["adt/acl.c"]
        src_backend_utils_adt_json_c["adt/json.c"]
        src_backend_utils_adt_timestamp_c["adt/timestamp.c"]
        src_backend_utils_adt_varlena_c["adt/varlena.c"]
        src_backend_utils_fmgr_fmgr_c["fmgr/fmgr.c"]
        src_backend_utils_misc_conffiles_c["misc/conffiles.c"]
        src_backend_utils_misc_guc_c["misc/guc.c"]
        src_backend_utils_misc_injection_point_c["misc/injection_point.c"]
        src_backend_utils_time_snapmgr_c["time/snapmgr.c"]
    end
    src_backend_libpq_auth_oauth_c --> src_backend_libpq_auth_c
    src_backend_libpq_auth_oauth_c --> src_backend_libpq_hba_c
    src_backend_libpq_auth_oauth_c --> src_backend_storage_file_fd_c
    src_backend_libpq_auth_oauth_c --> src_backend_storage_ipc_ipc_c
    src_backend_libpq_auth_oauth_c --> src_backend_utils_adt_json_c
    src_backend_libpq_auth_oauth_c --> src_backend_utils_adt_varlena_c
    src_backend_libpq_auth_oauth_c --> src_backend_utils_fmgr_fmgr_c
    src_backend_libpq_auth_oauth_c --> src_common_stringinfo_c
    src_backend_libpq_auth_oauth_c --> src_include_common_oauth_common_h
    src_backend_libpq_auth_oauth_c --> src_include_libpq_oauth_h
    src_backend_libpq_auth_oauth_c --> src_include_libpq_sasl_h
    src_backend_libpq_auth_oauth_c --> src_include_port_win32_msvc_unistd_h
    src_backend_libpq_auth_sasl_c --> src_backend_libpq_auth_c
    src_backend_libpq_auth_sasl_c --> src_backend_libpq_pqformat_c
    src_backend_libpq_auth_sasl_c --> src_include_libpq_libpq_h
    src_backend_libpq_auth_sasl_c --> src_include_libpq_sasl_h
    src_backend_libpq_auth_scram_c --> src_backend_access_transam_xlog_c
    src_backend_libpq_auth_scram_c --> src_backend_libpq_crypt_c
    src_backend_libpq_auth_scram_c --> src_common_base64_c
    src_backend_libpq_auth_scram_c --> src_common_hmac_c
    src_backend_libpq_auth_scram_c --> src_common_saslprep_c
    src_backend_libpq_auth_scram_c --> src_common_scram_common_c
    src_backend_libpq_auth_scram_c --> src_common_sha2_c
    src_backend_libpq_auth_scram_c --> src_include_catalog_pg_control_h
    src_backend_libpq_auth_scram_c --> src_include_libpq_sasl_h
    src_backend_libpq_auth_scram_c --> src_include_libpq_scram_h
    src_backend_libpq_auth_scram_c --> src_include_port_win32_msvc_unistd_h
    src_backend_libpq_auth_c --> src_backend_commands_user_c
    src_backend_libpq_auth_c --> src_backend_libpq_be_gssapi_common_c
    src_backend_libpq_auth_c --> src_backend_libpq_crypt_c
    src_backend_libpq_auth_c --> src_backend_libpq_pqformat_c
    src_backend_libpq_auth_c --> src_backend_postmaster_postmaster_c
    src_backend_libpq_auth_c --> src_backend_replication_walsender_c
    src_backend_libpq_auth_c --> src_backend_storage_ipc_ipc_c
    src_backend_libpq_auth_c --> src_backend_tcop_backend_startup_c
    src_backend_libpq_auth_c --> src_common_ip_c
    src_backend_libpq_auth_c --> src_common_md5_c
    src_backend_libpq_auth_c --> src_include_libpq_libpq_be_h
    src_backend_libpq_auth_c --> src_include_libpq_libpq_h
    src_backend_libpq_auth_c --> src_include_libpq_oauth_h
    src_backend_libpq_auth_c --> src_include_libpq_sasl_h
    src_backend_libpq_auth_c --> src_include_libpq_scram_h
    src_backend_libpq_auth_c --> src_include_port_pg_bswap_h
    src_backend_libpq_auth_c --> src_include_port_win32_netdb_h
    src_backend_libpq_auth_c --> src_include_port_win32_netinet_in_h
    src_backend_libpq_auth_c --> src_include_port_win32_pwd_h
    src_backend_libpq_auth_c --> src_include_port_win32_sys_select_h
    src_backend_libpq_auth_c --> src_include_port_win32_sys_socket_h
    src_backend_libpq_auth_c --> src_include_port_win32_msvc_sys_param_h
    src_backend_libpq_auth_c --> src_include_port_win32_msvc_unistd_h
    src_backend_libpq_be_fsstubs_c --> src_backend_catalog_pg_largeobject_c
    src_backend_libpq_be_fsstubs_c --> src_backend_storage_file_fd_c
    src_backend_libpq_be_fsstubs_c --> src_backend_utils_adt_acl_c
    src_backend_libpq_be_fsstubs_c --> src_backend_utils_time_snapmgr_c
    src_backend_libpq_be_fsstubs_c --> src_include_libpq_libpq_fs_h
    src_backend_libpq_be_fsstubs_c --> src_include_port_win32_msvc_unistd_h
    src_backend_libpq_be_fsstubs_c --> src_include_storage_large_object_h
    src_backend_libpq_be_fsstubs_c --> src_include_varatt_h
    src_backend_libpq_be_gssapi_common_c --> src_include_libpq_pg_gssapi_h
    src_backend_libpq_be_secure_common_c --> src_backend_storage_file_fd_c
    src_backend_libpq_be_secure_common_c --> src_backend_utils_misc_guc_c
    src_backend_libpq_be_secure_common_c --> src_common_percentrepl_c
    src_backend_libpq_be_secure_common_c --> src_common_string_c
    src_backend_libpq_be_secure_common_c --> src_include_libpq_libpq_h
    src_backend_libpq_be_secure_common_c --> src_include_port_win32_msvc_unistd_h
    src_backend_libpq_be_secure_gssapi_c --> src_backend_libpq_auth_c
    src_backend_libpq_be_secure_gssapi_c --> src_backend_libpq_be_gssapi_common_c
    src_backend_libpq_be_secure_gssapi_c --> src_backend_storage_ipc_latch_c
    src_backend_libpq_be_secure_gssapi_c --> src_backend_utils_activity_wait_event_c
    src_backend_libpq_be_secure_gssapi_c --> src_backend_utils_misc_injection_point_c
    src_backend_libpq_be_secure_gssapi_c --> src_include_libpq_libpq_h
    src_backend_libpq_be_secure_gssapi_c --> src_include_port_pg_bswap_h
    src_backend_libpq_be_secure_gssapi_c --> src_include_port_win32_msvc_unistd_h
    src_backend_libpq_be_secure_openssl_c --> src_backend_storage_file_fd_c
    src_backend_libpq_be_secure_openssl_c --> src_backend_storage_ipc_latch_c
    src_backend_libpq_be_secure_openssl_c --> src_backend_utils_activity_wait_event_c
    src_backend_libpq_be_secure_openssl_c --> src_backend_utils_misc_guc_c
    src_backend_libpq_be_secure_openssl_c --> src_common_hashfn_c
    src_backend_libpq_be_secure_openssl_c --> src_common_string_c
    src_backend_libpq_be_secure_openssl_c --> src_include_common_openssl_h
    src_backend_libpq_be_secure_openssl_c --> src_include_lib_simplehash_h
    src_backend_libpq_be_secure_openssl_c --> src_include_libpq_libpq_h
    src_backend_libpq_be_secure_openssl_c --> src_include_port_win32_arpa_inet_h
    src_backend_libpq_be_secure_openssl_c --> src_include_port_win32_netdb_h
    src_backend_libpq_be_secure_openssl_c --> src_include_port_win32_netinet_in_h
    src_backend_libpq_be_secure_openssl_c --> src_include_port_win32_netinet_tcp_h
    src_backend_libpq_be_secure_openssl_c --> src_include_port_win32_sys_socket_h
    src_backend_libpq_be_secure_openssl_c --> src_include_port_win32_msvc_unistd_h
    src_backend_libpq_be_secure_c --> src_backend_storage_ipc_latch_c
    src_backend_libpq_be_secure_c --> src_backend_utils_activity_wait_event_c
    src_backend_libpq_be_secure_c --> src_backend_utils_misc_injection_point_c
    src_backend_libpq_be_secure_c --> src_include_libpq_libpq_h
    src_backend_libpq_be_secure_c --> src_include_port_win32_arpa_inet_h
    src_backend_libpq_be_secure_c --> src_include_port_win32_netdb_h
    src_backend_libpq_be_secure_c --> src_include_port_win32_netinet_in_h
    src_backend_libpq_be_secure_c --> src_include_port_win32_netinet_tcp_h
    src_backend_libpq_be_secure_c --> src_include_port_win32_sys_socket_h
    src_backend_libpq_be_secure_c --> src_include_tcop_tcopprot_h
    src_backend_libpq_crypt_c --> src_backend_utils_adt_timestamp_c
    src_backend_libpq_crypt_c --> src_common_md5_c
    src_backend_libpq_crypt_c --> src_common_scram_common_c
    src_backend_libpq_crypt_c --> src_include_catalog_pg_authid_h
    src_backend_libpq_crypt_c --> src_include_libpq_scram_h
    src_backend_libpq_crypt_c --> src_include_port_win32_msvc_unistd_h
    src_backend_libpq_hba_c --> src_backend_catalog_pg_collation_c
    src_backend_libpq_hba_c --> src_backend_libpq_ifaddr_c
    src_backend_libpq_hba_c --> src_backend_libpq_pqcomm_c
    src_backend_libpq_hba_c --> src_backend_postmaster_postmaster_c
    src_backend_libpq_hba_c --> src_backend_replication_walsender_c
    src_backend_libpq_hba_c --> src_backend_storage_file_fd_c
    src_backend_libpq_hba_c --> src_backend_utils_adt_acl_c
    src_backend_libpq_hba_c --> src_backend_utils_adt_varlena_c
    src_backend_libpq_hba_c --> src_backend_utils_misc_conffiles_c
    src_backend_libpq_hba_c --> src_backend_utils_misc_guc_c
    src_backend_libpq_hba_c --> src_common_ip_c
    src_backend_libpq_hba_c --> src_common_string_c
    src_backend_libpq_hba_c --> src_include_libpq_libpq_be_h
    src_backend_libpq_hba_c --> src_include_libpq_oauth_h
    src_backend_libpq_hba_c --> src_include_nodes_pg_list_h
    src_backend_libpq_hba_c --> src_include_port_win32_arpa_inet_h
    src_backend_libpq_hba_c --> src_include_port_win32_netdb_h
    src_backend_libpq_hba_c --> src_include_port_win32_netinet_in_h
    src_backend_libpq_hba_c --> src_include_port_win32_pwd_h
    src_backend_libpq_hba_c --> src_include_port_win32_sys_socket_h
    src_backend_libpq_hba_c --> src_include_port_win32_msvc_sys_param_h
    src_backend_libpq_hba_c --> src_include_port_win32_msvc_unistd_h
    src_backend_libpq_hba_c --> src_include_regex_regex_h
    src_backend_libpq_ifaddr_c --> src_backend_libpq_pqcomm_c
    src_backend_libpq_ifaddr_c --> src_include_port_pg_bswap_h
    src_backend_libpq_ifaddr_c --> src_include_port_win32_netdb_h
    src_backend_libpq_ifaddr_c --> src_include_port_win32_netinet_in_h
    src_backend_libpq_ifaddr_c --> src_include_port_win32_netinet_tcp_h
    src_backend_libpq_ifaddr_c --> src_include_port_win32_sys_socket_h
    src_backend_libpq_ifaddr_c --> src_include_port_win32_msvc_sys_file_h
    src_backend_libpq_ifaddr_c --> src_include_port_win32_msvc_unistd_h
    src_backend_libpq_pqcomm_c --> src_backend_postmaster_postmaster_c
    src_backend_libpq_pqcomm_c --> src_backend_storage_ipc_ipc_c
    src_backend_libpq_pqcomm_c --> src_backend_storage_ipc_latch_c
    src_backend_libpq_pqcomm_c --> src_common_ip_c
    src_backend_libpq_pqcomm_c --> src_include_libpq_libpq_h
    src_backend_libpq_pqcomm_c --> src_include_libpq_protocol_h
    src_backend_libpq_pqcomm_c --> src_include_port_pg_bswap_h
    src_backend_libpq_pqcomm_c --> src_include_port_win32_grp_h
    src_backend_libpq_pqcomm_c --> src_include_port_win32_netdb_h
    src_backend_libpq_pqcomm_c --> src_include_port_win32_netinet_in_h
    src_backend_libpq_pqcomm_c --> src_include_port_win32_netinet_tcp_h
    src_backend_libpq_pqcomm_c --> src_include_port_win32_sys_socket_h
    src_backend_libpq_pqcomm_c --> src_include_port_win32_sys_un_h
    src_backend_libpq_pqcomm_c --> src_include_port_win32_msvc_sys_file_h
    src_backend_libpq_pqcomm_c --> src_include_port_win32_msvc_sys_time_h
    src_backend_libpq_pqcomm_c --> src_include_port_win32_msvc_unistd_h
    src_backend_libpq_pqcomm_c --> src_include_port_win32_msvc_utime_h
    src_backend_libpq_pqcomm_c --> src_include_utils_guc_hooks_h
    src_backend_libpq_pqformat_c --> src_common_stringinfo_c
    src_backend_libpq_pqformat_c --> src_include_libpq_libpq_h
    src_backend_libpq_pqformat_c --> src_include_mb_pg_wchar_h
    src_backend_libpq_pqformat_c --> src_include_port_pg_bswap_h
    src_backend_libpq_pqformat_c --> src_include_port_win32_msvc_sys_param_h
    src_backend_libpq_pqformat_c --> src_include_varatt_h
    src_backend_libpq_pqmq_c --> src_backend_access_transam_parallel_c
    src_backend_libpq_pqmq_c --> src_backend_commands_repack_c
    src_backend_libpq_pqmq_c --> src_backend_libpq_pqformat_c
    src_backend_libpq_pqmq_c --> src_backend_storage_ipc_latch_c
    src_backend_libpq_pqmq_c --> src_backend_storage_ipc_shm_mq_c
    src_backend_libpq_pqmq_c --> src_backend_utils_activity_wait_event_c
    src_backend_libpq_pqmq_c --> src_common_stringinfo_c
    src_backend_libpq_pqmq_c --> src_include_libpq_libpq_h
    src_backend_libpq_pqmq_c --> src_include_replication_logicalworker_h
    src_backend_libpq_pqmq_c --> src_include_storage_procnumber_h
    src_backend_libpq_pqmq_c --> src_include_tcop_tcopprot_h
```
