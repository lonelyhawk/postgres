# `common` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "commands"
        src_backend_commands_wait_c["wait.c"]
    end
    subgraph "common"
        src_common_archive_c["archive.c"]
        src_common_base64_c["base64.c"]
        src_common_binaryheap_c["binaryheap.c"]
        src_common_blkreftable_c["blkreftable.c"]
        src_common_checksum_helper_c["checksum_helper.c"]
        src_common_compression_c["compression.c"]
        src_common_config_info_c["config_info.c"]
        src_common_controldata_utils_c["controldata_utils.c"]
        src_common_cryptohash_c["cryptohash.c"]
        src_common_cryptohash_openssl_c["cryptohash_openssl.c"]
        src_common_d2s_c["d2s.c"]
        src_common_d2s_full_table_h["d2s_full_table.h"]
        src_common_d2s_intrinsics_h["d2s_intrinsics.h"]
        src_common_digit_table_h["digit_table.h"]
        src_common_encnames_c["encnames.c"]
        src_common_exec_c["exec.c"]
        src_common_f2s_c["f2s.c"]
        src_common_file_perm_c["file_perm.c"]
        src_common_file_utils_c["file_utils.c"]
        src_common_hashfn_c["hashfn.c"]
        src_common_hmac_c["hmac.c"]
        src_common_hmac_openssl_c["hmac_openssl.c"]
        src_common_instr_time_c["instr_time.c"]
        src_common_ip_c["ip.c"]
        src_common_jsonapi_c["jsonapi.c"]
        src_common_keywords_c["keywords.c"]
        src_common_kwlookup_c["kwlookup.c"]
        src_common_link_canary_c["link-canary.c"]
        src_common_md5_c["md5.c"]
        src_common_md5_common_c["md5_common.c"]
        src_common_md5_int_h["md5_int.h"]
        src_common_parse_manifest_c["parse_manifest.c"]
        src_common_percentrepl_c["percentrepl.c"]
        src_common_pg_get_line_c["pg_get_line.c"]
        src_common_pg_lzcompress_c["pg_lzcompress.c"]
        src_common_pg_prng_c["pg_prng.c"]
        src_common_pgfnames_c["pgfnames.c"]
        src_common_psprintf_c["psprintf.c"]
        src_common_relpath_c["relpath.c"]
        src_common_rmtree_c["rmtree.c"]
        src_common_ryu_common_h["ryu_common.h"]
        src_common_saslprep_c["saslprep.c"]
        src_common_scram_common_c["scram-common.c"]
        src_common_sha1_c["sha1.c"]
        src_common_sha1_int_h["sha1_int.h"]
        src_common_sha2_c["sha2.c"]
        src_common_sha2_int_h["sha2_int.h"]
        src_common_string_c["string.c"]
        src_common_stringinfo_c["stringinfo.c"]
        src_common_unicode_case_test_c["unicode/case_test.c"]
        src_common_unicode_category_test_c["unicode/category_test.c"]
        src_common_unicode_norm_test_c["unicode/norm_test.c"]
        src_common_unicode_case_c["unicode_case.c"]
        src_common_unicode_category_c["unicode_category.c"]
        src_common_unicode_norm_c["unicode_norm.c"]
        src_common_username_c["username.c"]
        src_common_wait_error_c["wait_error.c"]
        src_common_wchar_c["wchar.c"]
    end
    subgraph "include/access"
        src_include_access_xlog_internal_h["xlog_internal.h"]
        src_include_access_xlogdefs_h["xlogdefs.h"]
    end
    subgraph "include/catalog"
        src_include_catalog_catversion_h["catversion.h"]
        src_include_catalog_pg_control_h["pg_control.h"]
    end
    subgraph "include/common"
        src_include_common_logging_h["logging.h"]
        src_include_common_shortest_dec_h["shortest_dec.h"]
        src_include_common_unicode_case_table_h["unicode_case_table.h"]
        src_include_common_unicode_category_table_h["unicode_category_table.h"]
        src_include_common_unicode_east_asian_fw_table_h["unicode_east_asian_fw_table.h"]
        src_include_common_unicode_nonspacing_table_h["unicode_nonspacing_table.h"]
        src_include_common_unicode_norm_hashfunc_h["unicode_norm_hashfunc.h"]
        src_include_common_unicode_norm_table_h["unicode_norm_table.h"]
        src_include_common_unicode_normprops_table_h["unicode_normprops_table.h"]
        src_include_common_unicode_version_h["unicode_version.h"]
    end
    subgraph "include/lib"
        src_include_lib_simplehash_h["simplehash.h"]
    end
    subgraph "include/mb"
        src_include_mb_pg_wchar_h["pg_wchar.h"]
    end
    subgraph "include/parser"
        src_include_parser_kwlist_h["kwlist.h"]
    end
    subgraph "include/port"
        src_include_port_pg_bswap_h["pg_bswap.h"]
        src_include_port_pg_cpu_h["pg_cpu.h"]
        src_include_port_pg_crc32c_h["pg_crc32c.h"]
        src_include_port_pg_iovec_h["pg_iovec.h"]
        src_include_port_pg_lfind_h["pg_lfind.h"]
        src_include_port_win32_arpa_inet_h["win32/arpa/inet.h"]
        src_include_port_win32_netdb_h["win32/netdb.h"]
        src_include_port_win32_netinet_in_h["win32/netinet/in.h"]
        src_include_port_win32_netinet_tcp_h["win32/netinet/tcp.h"]
        src_include_port_win32_pwd_h["win32/pwd.h"]
        src_include_port_win32_sys_socket_h["win32/sys/socket.h"]
        src_include_port_win32_msvc_sys_file_h["win32_msvc/sys/file.h"]
        src_include_port_win32_msvc_sys_param_h["win32_msvc/sys/param.h"]
        src_include_port_win32_msvc_sys_time_h["win32_msvc/sys/time.h"]
        src_include_port_win32_msvc_unistd_h["win32_msvc/unistd.h"]
    end
    subgraph "include/storage"
        src_include_storage_block_h["block.h"]
        src_include_storage_procnumber_h["procnumber.h"]
        src_include_storage_relfilelocator_h["relfilelocator.h"]
    end
    subgraph "include/top"
        src_include_c_h["c.h"]
        src_include_postgres_fe_h["postgres_fe.h"]
    end
    subgraph "libpq"
        src_backend_libpq_pqcomm_c["pqcomm.c"]
    end
    subgraph "port"
        src_port_dirent_c["dirent.c"]
        src_port_pg_bitutils_c["pg_bitutils.c"]
    end
    subgraph "storage"
        src_backend_storage_file_fd_c["file/fd.c"]
    end
    subgraph "utils"
        src_backend_utils_activity_wait_event_c["activity/wait_event.c"]
        src_backend_utils_adt_ascii_c["adt/ascii.c"]
        src_backend_utils_resowner_resowner_c["resowner/resowner.c"]
    end
    src_common_archive_c --> src_common_percentrepl_c
    src_common_archive_c --> src_include_postgres_fe_h
    src_common_base64_c --> src_include_postgres_fe_h
    src_common_binaryheap_c --> src_include_common_logging_h
    src_common_binaryheap_c --> src_include_postgres_fe_h
    src_common_blkreftable_c --> src_common_hashfn_c
    src_common_blkreftable_c --> src_include_common_logging_h
    src_common_blkreftable_c --> src_include_lib_simplehash_h
    src_common_blkreftable_c --> src_include_port_pg_crc32c_h
    src_common_blkreftable_c --> src_include_postgres_fe_h
    src_common_blkreftable_c --> src_include_storage_block_h
    src_common_blkreftable_c --> src_include_storage_relfilelocator_h
    src_common_checksum_helper_c --> src_common_cryptohash_c
    src_common_checksum_helper_c --> src_common_sha2_c
    src_common_checksum_helper_c --> src_include_port_pg_crc32c_h
    src_common_checksum_helper_c --> src_include_postgres_fe_h
    src_common_compression_c --> src_include_postgres_fe_h
    src_common_config_info_c --> src_include_postgres_fe_h
    src_common_controldata_utils_c --> src_backend_storage_file_fd_c
    src_common_controldata_utils_c --> src_backend_utils_activity_wait_event_c
    src_common_controldata_utils_c --> src_common_file_perm_c
    src_common_controldata_utils_c --> src_include_access_xlog_internal_h
    src_common_controldata_utils_c --> src_include_catalog_pg_control_h
    src_common_controldata_utils_c --> src_include_common_logging_h
    src_common_controldata_utils_c --> src_include_port_pg_crc32c_h
    src_common_controldata_utils_c --> src_include_port_win32_msvc_sys_time_h
    src_common_controldata_utils_c --> src_include_port_win32_msvc_unistd_h
    src_common_controldata_utils_c --> src_include_postgres_fe_h
    src_common_cryptohash_c --> src_common_md5_int_h
    src_common_cryptohash_c --> src_common_sha1_int_h
    src_common_cryptohash_c --> src_common_sha2_int_h
    src_common_cryptohash_c --> src_include_port_win32_msvc_sys_param_h
    src_common_cryptohash_c --> src_include_postgres_fe_h
    src_common_cryptohash_openssl_c --> src_backend_utils_resowner_resowner_c
    src_common_cryptohash_openssl_c --> src_common_cryptohash_c
    src_common_cryptohash_openssl_c --> src_common_md5_c
    src_common_cryptohash_openssl_c --> src_common_sha1_c
    src_common_cryptohash_openssl_c --> src_common_sha2_c
    src_common_cryptohash_openssl_c --> src_include_postgres_fe_h
    src_common_d2s_c --> src_common_d2s_full_table_h
    src_common_d2s_c --> src_common_d2s_intrinsics_h
    src_common_d2s_c --> src_common_digit_table_h
    src_common_d2s_c --> src_common_ryu_common_h
    src_common_d2s_c --> src_include_common_shortest_dec_h
    src_common_d2s_c --> src_include_postgres_fe_h
    src_common_encnames_c --> src_include_c_h
    src_common_encnames_c --> src_include_mb_pg_wchar_h
    src_common_encnames_c --> src_include_port_win32_msvc_unistd_h
    src_common_exec_c --> src_backend_commands_wait_c
    src_common_exec_c --> src_common_string_c
    src_common_exec_c --> src_include_port_win32_msvc_unistd_h
    src_common_exec_c --> src_include_postgres_fe_h
    src_common_f2s_c --> src_common_digit_table_h
    src_common_f2s_c --> src_common_ryu_common_h
    src_common_f2s_c --> src_include_common_shortest_dec_h
    src_common_f2s_c --> src_include_postgres_fe_h
    src_common_file_perm_c --> src_include_c_h
    src_common_file_utils_c --> src_common_relpath_c
    src_common_file_utils_c --> src_include_common_logging_h
    src_common_file_utils_c --> src_include_port_pg_iovec_h
    src_common_file_utils_c --> src_include_port_win32_msvc_unistd_h
    src_common_file_utils_c --> src_include_postgres_fe_h
    src_common_file_utils_c --> src_port_dirent_c
    src_common_hashfn_c --> src_port_pg_bitutils_c
    src_common_hmac_c --> src_common_cryptohash_c
    src_common_hmac_c --> src_common_md5_c
    src_common_hmac_c --> src_common_sha1_c
    src_common_hmac_c --> src_common_sha2_c
    src_common_hmac_c --> src_include_postgres_fe_h
    src_common_hmac_openssl_c --> src_backend_utils_resowner_resowner_c
    src_common_hmac_openssl_c --> src_common_hmac_c
    src_common_hmac_openssl_c --> src_common_md5_c
    src_common_hmac_openssl_c --> src_common_sha1_c
    src_common_hmac_openssl_c --> src_common_sha2_c
    src_common_hmac_openssl_c --> src_include_postgres_fe_h
    src_common_instr_time_c --> src_include_port_pg_cpu_h
    src_common_instr_time_c --> src_include_port_win32_msvc_sys_time_h
    src_common_instr_time_c --> src_include_postgres_fe_h
    src_common_ip_c --> src_backend_libpq_pqcomm_c
    src_common_ip_c --> src_include_port_win32_arpa_inet_h
    src_common_ip_c --> src_include_port_win32_netdb_h
    src_common_ip_c --> src_include_port_win32_netinet_in_h
    src_common_ip_c --> src_include_port_win32_netinet_tcp_h
    src_common_ip_c --> src_include_port_win32_sys_socket_h
    src_common_ip_c --> src_include_port_win32_msvc_sys_file_h
    src_common_ip_c --> src_include_port_win32_msvc_unistd_h
    src_common_ip_c --> src_include_postgres_fe_h
    src_common_jsonapi_c --> src_common_stringinfo_c
    src_common_jsonapi_c --> src_include_mb_pg_wchar_h
    src_common_jsonapi_c --> src_include_port_pg_lfind_h
    src_common_jsonapi_c --> src_include_postgres_fe_h
    src_common_keywords_c --> src_common_kwlookup_c
    src_common_keywords_c --> src_include_c_h
    src_common_keywords_c --> src_include_parser_kwlist_h
    src_common_kwlookup_c --> src_include_c_h
    src_common_link_canary_c --> src_include_c_h
    src_common_md5_c --> src_common_md5_int_h
    src_common_md5_c --> src_include_postgres_fe_h
    src_common_md5_common_c --> src_common_cryptohash_c
    src_common_md5_common_c --> src_common_md5_c
    src_common_md5_common_c --> src_include_postgres_fe_h
    src_common_md5_int_h --> src_common_md5_c
    src_common_parse_manifest_c --> src_common_checksum_helper_c
    src_common_parse_manifest_c --> src_common_jsonapi_c
    src_common_parse_manifest_c --> src_include_access_xlogdefs_h
    src_common_parse_manifest_c --> src_include_mb_pg_wchar_h
    src_common_parse_manifest_c --> src_include_postgres_fe_h
    src_common_percentrepl_c --> src_common_stringinfo_c
    src_common_percentrepl_c --> src_include_common_logging_h
    src_common_percentrepl_c --> src_include_postgres_fe_h
    src_common_pg_get_line_c --> src_common_string_c
    src_common_pg_get_line_c --> src_common_stringinfo_c
    src_common_pg_get_line_c --> src_include_postgres_fe_h
    src_common_pg_lzcompress_c --> src_include_postgres_fe_h
    src_common_pg_prng_c --> src_include_c_h
    src_common_pg_prng_c --> src_port_pg_bitutils_c
    src_common_pgfnames_c --> src_include_common_logging_h
    src_common_pgfnames_c --> src_include_postgres_fe_h
    src_common_pgfnames_c --> src_port_dirent_c
    src_common_psprintf_c --> src_include_postgres_fe_h
    src_common_relpath_c --> src_include_catalog_catversion_h
    src_common_relpath_c --> src_include_postgres_fe_h
    src_common_relpath_c --> src_include_storage_procnumber_h
    src_common_rmtree_c --> src_backend_storage_file_fd_c
    src_common_rmtree_c --> src_common_file_utils_c
    src_common_rmtree_c --> src_include_common_logging_h
    src_common_rmtree_c --> src_include_port_win32_msvc_unistd_h
    src_common_rmtree_c --> src_include_postgres_fe_h
    src_common_saslprep_c --> src_common_string_c
    src_common_saslprep_c --> src_common_unicode_norm_c
    src_common_saslprep_c --> src_include_mb_pg_wchar_h
    src_common_saslprep_c --> src_include_postgres_fe_h
    src_common_scram_common_c --> src_common_base64_c
    src_common_scram_common_c --> src_common_cryptohash_c
    src_common_scram_common_c --> src_common_hmac_c
    src_common_scram_common_c --> src_common_sha2_c
    src_common_scram_common_c --> src_include_port_pg_bswap_h
    src_common_scram_common_c --> src_include_postgres_fe_h
    src_common_sha1_c --> src_common_sha1_int_h
    src_common_sha1_c --> src_include_port_win32_msvc_sys_param_h
    src_common_sha1_c --> src_include_postgres_fe_h
    src_common_sha1_int_h --> src_common_sha1_c
    src_common_sha2_c --> src_common_sha2_int_h
    src_common_sha2_c --> src_include_postgres_fe_h
    src_common_sha2_int_h --> src_common_sha2_c
    src_common_string_c --> src_include_postgres_fe_h
    src_common_stringinfo_c --> src_include_postgres_fe_h
    src_common_unicode_case_test_c --> src_common_string_c
    src_common_unicode_case_test_c --> src_common_unicode_case_c
    src_common_unicode_case_test_c --> src_common_unicode_category_c
    src_common_unicode_case_test_c --> src_include_common_unicode_version_h
    src_common_unicode_case_test_c --> src_include_mb_pg_wchar_h
    src_common_unicode_case_test_c --> src_include_postgres_fe_h
    src_common_unicode_category_test_c --> src_common_string_c
    src_common_unicode_category_test_c --> src_common_unicode_category_c
    src_common_unicode_category_test_c --> src_include_common_unicode_version_h
    src_common_unicode_category_test_c --> src_include_mb_pg_wchar_h
    src_common_unicode_category_test_c --> src_include_postgres_fe_h
    src_common_unicode_norm_test_c --> src_common_string_c
    src_common_unicode_norm_test_c --> src_common_unicode_norm_c
    src_common_unicode_norm_test_c --> src_include_postgres_fe_h
    src_common_unicode_case_c --> src_common_unicode_category_c
    src_common_unicode_case_c --> src_include_common_unicode_case_table_h
    src_common_unicode_case_c --> src_include_mb_pg_wchar_h
    src_common_unicode_case_c --> src_include_postgres_fe_h
    src_common_unicode_category_c --> src_include_common_unicode_category_table_h
    src_common_unicode_category_c --> src_include_postgres_fe_h
    src_common_unicode_norm_c --> src_include_common_unicode_norm_hashfunc_h
    src_common_unicode_norm_c --> src_include_common_unicode_norm_table_h
    src_common_unicode_norm_c --> src_include_common_unicode_normprops_table_h
    src_common_unicode_norm_c --> src_include_port_pg_bswap_h
    src_common_unicode_norm_c --> src_include_postgres_fe_h
    src_common_username_c --> src_include_port_win32_pwd_h
    src_common_username_c --> src_include_port_win32_msvc_unistd_h
    src_common_username_c --> src_include_postgres_fe_h
    src_common_wait_error_c --> src_backend_commands_wait_c
    src_common_wait_error_c --> src_include_postgres_fe_h
    src_common_wchar_c --> src_backend_utils_adt_ascii_c
    src_common_wchar_c --> src_include_c_h
    src_common_wchar_c --> src_include_common_unicode_east_asian_fw_table_h
    src_common_wchar_c --> src_include_common_unicode_nonspacing_table_h
    src_common_wchar_c --> src_include_mb_pg_wchar_h
```
