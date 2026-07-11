# `port` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "include/lib"
        src_include_lib_sort_template_h["sort_template.h"]
    end
    subgraph "include/mb"
        src_include_mb_pg_wchar_h["pg_wchar.h"]
    end
    subgraph "include/port"
        src_include_port_atomics_arch_arm_h["atomics/arch-arm.h"]
        src_include_port_atomics_arch_ppc_h["atomics/arch-ppc.h"]
        src_include_port_atomics_arch_x86_h["atomics/arch-x86.h"]
        src_include_port_atomics_fallback_h["atomics/fallback.h"]
        src_include_port_atomics_generic_gcc_h["atomics/generic-gcc.h"]
        src_include_port_atomics_generic_msvc_h["atomics/generic-msvc.h"]
        src_include_port_atomics_generic_h["atomics/generic.h"]
        src_include_port_pg_bswap_h["pg_bswap.h"]
        src_include_port_pg_cpu_h["pg_cpu.h"]
        src_include_port_pg_crc32c_h["pg_crc32c.h"]
        src_include_port_pg_pthread_h["pg_pthread.h"]
        src_include_port_win32_arpa_inet_h["win32/arpa/inet.h"]
        src_include_port_win32_netinet_in_h["win32/netinet/in.h"]
        src_include_port_win32_pwd_h["win32/pwd.h"]
        src_include_port_win32_sys_socket_h["win32/sys/socket.h"]
        src_include_port_win32_sys_un_h["win32/sys/un.h"]
        src_include_port_win32_msvc_sys_file_h["win32_msvc/sys/file.h"]
        src_include_port_win32_msvc_sys_param_h["win32_msvc/sys/param.h"]
        src_include_port_win32_msvc_sys_time_h["win32_msvc/sys/time.h"]
        src_include_port_win32_msvc_unistd_h["win32_msvc/unistd.h"]
        src_include_port_win32ntdll_h["win32ntdll.h"]
    end
    subgraph "include/portability"
        src_include_portability_mem_h["mem.h"]
    end
    subgraph "include/storage"
        src_include_storage_pg_sema_h["pg_sema.h"]
        src_include_storage_pg_shmem_h["pg_shmem.h"]
        src_include_storage_spin_h["spin.h"]
    end
    subgraph "include/top"
        src_include_c_h["c.h"]
        src_include_pg_getopt_h["pg_getopt.h"]
        src_include_pgtar_h["pgtar.h"]
        src_include_postgres_fe_h["postgres_fe.h"]
    end
    subgraph "include/utils"
        src_include_utils_guc_hooks_h["guc_hooks.h"]
        src_include_utils_inet_h["inet.h"]
        src_include_utils_pidfile_h["pidfile.h"]
    end
    subgraph "libpq"
        src_backend_libpq_pqsignal_c["pqsignal.c"]
    end
    subgraph "port"
        src_backend_port_atomics_c["atomics.c"]
        src_backend_port_posix_sema_c["posix_sema.c"]
        src_backend_port_sysv_sema_c["sysv_sema.c"]
        src_backend_port_sysv_shmem_c["sysv_shmem.c"]
        src_port_bsearch_arg_c["bsearch_arg.c"]
        src_port_chklocale_c["chklocale.c"]
        src_port_dirent_c["dirent.c"]
        src_port_dirmod_c["dirmod.c"]
        src_port_explicit_bzero_c["explicit_bzero.c"]
        src_port_getopt_c["getopt.c"]
        src_port_getopt_long_c["getopt_long.c"]
        src_port_getpeereid_c["getpeereid.c"]
        src_port_inet_aton_c["inet_aton.c"]
        src_port_inet_net_ntop_c["inet_net_ntop.c"]
        src_port_kill_c["kill.c"]
        src_port_mkdtemp_c["mkdtemp.c"]
        src_port_noblock_c["noblock.c"]
        src_port_open_c["open.c"]
        src_port_path_c["path.c"]
        src_port_pg_bitutils_c["pg_bitutils.c"]
        src_port_pg_cpu_x86_c["pg_cpu_x86.c"]
        src_port_pg_crc32c_armv8_c["pg_crc32c_armv8.c"]
        src_port_pg_crc32c_armv8_choose_c["pg_crc32c_armv8_choose.c"]
        src_port_pg_crc32c_loongarch_c["pg_crc32c_loongarch.c"]
        src_port_pg_crc32c_sb8_c["pg_crc32c_sb8.c"]
        src_port_pg_crc32c_sse42_c["pg_crc32c_sse42.c"]
        src_port_pg_getopt_ctx_c["pg_getopt_ctx.c"]
        src_port_pg_localeconv_r_c["pg_localeconv_r.c"]
        src_port_pg_numa_c["pg_numa.c"]
        src_port_pg_popcount_aarch64_c["pg_popcount_aarch64.c"]
        src_port_pg_popcount_x86_c["pg_popcount_x86.c"]
        src_port_pg_strong_random_c["pg_strong_random.c"]
        src_port_pgcheckdir_c["pgcheckdir.c"]
        src_port_pgmkdirp_c["pgmkdirp.c"]
        src_port_pgsleep_c["pgsleep.c"]
        src_port_pgstrcasecmp_c["pgstrcasecmp.c"]
        src_port_pgstrsignal_c["pgstrsignal.c"]
        src_port_pqsignal_c["pqsignal.c"]
        src_port_pthread_barrier_wait_c["pthread_barrier_wait.c"]
        src_port_qsort_c["qsort.c"]
        src_port_qsort_arg_c["qsort_arg.c"]
        src_port_quotes_c["quotes.c"]
        src_port_snprintf_c["snprintf.c"]
        src_port_strerror_c["strerror.c"]
        src_port_strlcat_c["strlcat.c"]
        src_port_strlcpy_c["strlcpy.c"]
        src_port_strsep_c["strsep.c"]
        src_port_strtof_c["strtof.c"]
        src_port_system_c["system.c"]
        src_port_tar_c["tar.c"]
        src_port_timingsafe_bcmp_c["timingsafe_bcmp.c"]
    end
    subgraph "storage"
        src_backend_storage_file_fd_c["file/fd.c"]
        src_backend_storage_ipc_dsm_c["ipc/dsm.c"]
        src_backend_storage_ipc_ipc_c["ipc/ipc.c"]
        src_backend_storage_ipc_shmem_c["ipc/shmem.c"]
    end
    subgraph "utils"
        src_backend_utils_adt_float_c["adt/float.c"]
        src_backend_utils_misc_guc_c["misc/guc.c"]
    end
    src_backend_port_atomics_c --> src_include_port_atomics_arch_arm_h
    src_backend_port_atomics_c --> src_include_port_atomics_arch_ppc_h
    src_backend_port_atomics_c --> src_include_port_atomics_arch_x86_h
    src_backend_port_atomics_c --> src_include_port_atomics_fallback_h
    src_backend_port_atomics_c --> src_include_port_atomics_generic_gcc_h
    src_backend_port_atomics_c --> src_include_port_atomics_generic_msvc_h
    src_backend_port_atomics_c --> src_include_port_atomics_generic_h
    src_backend_port_atomics_c --> src_include_storage_spin_h
    src_backend_port_posix_sema_c --> src_backend_storage_ipc_ipc_c
    src_backend_port_posix_sema_c --> src_backend_storage_ipc_shmem_c
    src_backend_port_posix_sema_c --> src_include_port_win32_msvc_unistd_h
    src_backend_port_posix_sema_c --> src_include_storage_pg_sema_h
    src_backend_port_sysv_sema_c --> src_backend_storage_ipc_ipc_c
    src_backend_port_sysv_sema_c --> src_backend_storage_ipc_shmem_c
    src_backend_port_sysv_sema_c --> src_include_port_win32_msvc_sys_file_h
    src_backend_port_sysv_sema_c --> src_include_port_win32_msvc_unistd_h
    src_backend_port_sysv_sema_c --> src_include_storage_pg_sema_h
    src_backend_port_sysv_shmem_c --> src_backend_storage_file_fd_c
    src_backend_port_sysv_shmem_c --> src_backend_storage_ipc_dsm_c
    src_backend_port_sysv_shmem_c --> src_backend_storage_ipc_ipc_c
    src_backend_port_sysv_shmem_c --> src_backend_storage_ipc_shmem_c
    src_backend_port_sysv_shmem_c --> src_backend_utils_misc_guc_c
    src_backend_port_sysv_shmem_c --> src_include_port_win32_msvc_sys_file_h
    src_backend_port_sysv_shmem_c --> src_include_port_win32_msvc_unistd_h
    src_backend_port_sysv_shmem_c --> src_include_portability_mem_h
    src_backend_port_sysv_shmem_c --> src_include_storage_pg_shmem_h
    src_backend_port_sysv_shmem_c --> src_include_utils_guc_hooks_h
    src_backend_port_sysv_shmem_c --> src_include_utils_pidfile_h
    src_backend_port_sysv_shmem_c --> src_port_pg_bitutils_c
    src_port_bsearch_arg_c --> src_include_c_h
    src_port_chklocale_c --> src_include_mb_pg_wchar_h
    src_port_chklocale_c --> src_include_postgres_fe_h
    src_port_dirent_c --> src_include_postgres_fe_h
    src_port_dirmod_c --> src_include_port_win32_msvc_unistd_h
    src_port_dirmod_c --> src_include_port_win32ntdll_h
    src_port_dirmod_c --> src_include_postgres_fe_h
    src_port_explicit_bzero_c --> src_include_c_h
    src_port_getopt_c --> src_include_c_h
    src_port_getopt_c --> src_include_pg_getopt_h
    src_port_getopt_c --> src_port_pg_getopt_ctx_c
    src_port_getopt_long_c --> src_include_c_h
    src_port_getopt_long_c --> src_include_pg_getopt_h
    src_port_getpeereid_c --> src_include_c_h
    src_port_getpeereid_c --> src_include_port_win32_sys_socket_h
    src_port_getpeereid_c --> src_include_port_win32_sys_un_h
    src_port_getpeereid_c --> src_include_port_win32_msvc_sys_param_h
    src_port_getpeereid_c --> src_include_port_win32_msvc_unistd_h
    src_port_inet_aton_c --> src_include_c_h
    src_port_inet_aton_c --> src_include_port_pg_bswap_h
    src_port_inet_aton_c --> src_include_port_win32_netinet_in_h
    src_port_inet_net_ntop_c --> src_include_port_win32_arpa_inet_h
    src_port_inet_net_ntop_c --> src_include_port_win32_netinet_in_h
    src_port_inet_net_ntop_c --> src_include_port_win32_sys_socket_h
    src_port_inet_net_ntop_c --> src_include_postgres_fe_h
    src_port_inet_net_ntop_c --> src_include_utils_inet_h
    src_port_kill_c --> src_include_c_h
    src_port_mkdtemp_c --> src_include_c_h
    src_port_mkdtemp_c --> src_include_port_win32_msvc_unistd_h
    src_port_noblock_c --> src_include_c_h
    src_port_open_c --> src_include_port_win32ntdll_h
    src_port_open_c --> src_include_postgres_fe_h
    src_port_path_c --> src_include_mb_pg_wchar_h
    src_port_path_c --> src_include_port_win32_pwd_h
    src_port_path_c --> src_include_port_win32_msvc_unistd_h
    src_port_path_c --> src_include_postgres_fe_h
    src_port_pg_bitutils_c --> src_include_c_h
    src_port_pg_cpu_x86_c --> src_include_port_pg_cpu_h
    src_port_pg_cpu_x86_c --> src_include_postgres_fe_h
    src_port_pg_crc32c_armv8_c --> src_include_c_h
    src_port_pg_crc32c_armv8_c --> src_include_port_pg_crc32c_h
    src_port_pg_crc32c_armv8_choose_c --> src_include_port_pg_crc32c_h
    src_port_pg_crc32c_armv8_choose_c --> src_include_postgres_fe_h
    src_port_pg_crc32c_loongarch_c --> src_include_c_h
    src_port_pg_crc32c_loongarch_c --> src_include_port_pg_crc32c_h
    src_port_pg_crc32c_sb8_c --> src_include_c_h
    src_port_pg_crc32c_sb8_c --> src_include_port_pg_crc32c_h
    src_port_pg_crc32c_sse42_c --> src_include_c_h
    src_port_pg_crc32c_sse42_c --> src_include_port_pg_cpu_h
    src_port_pg_crc32c_sse42_c --> src_include_port_pg_crc32c_h
    src_port_pg_getopt_ctx_c --> src_include_c_h
    src_port_pg_localeconv_r_c --> src_include_c_h
    src_port_pg_numa_c --> src_include_c_h
    src_port_pg_numa_c --> src_include_port_win32_msvc_unistd_h
    src_port_pg_popcount_aarch64_c --> src_include_c_h
    src_port_pg_popcount_aarch64_c --> src_port_pg_bitutils_c
    src_port_pg_popcount_x86_c --> src_include_c_h
    src_port_pg_popcount_x86_c --> src_include_port_pg_cpu_h
    src_port_pg_popcount_x86_c --> src_port_pg_bitutils_c
    src_port_pg_strong_random_c --> src_include_c_h
    src_port_pg_strong_random_c --> src_include_port_win32_msvc_sys_time_h
    src_port_pg_strong_random_c --> src_include_port_win32_msvc_unistd_h
    src_port_pgcheckdir_c --> src_include_c_h
    src_port_pgcheckdir_c --> src_port_dirent_c
    src_port_pgmkdirp_c --> src_include_c_h
    src_port_pgsleep_c --> src_include_c_h
    src_port_pgsleep_c --> src_include_port_win32_msvc_sys_time_h
    src_port_pgstrcasecmp_c --> src_include_c_h
    src_port_pgstrsignal_c --> src_include_c_h
    src_port_pqsignal_c --> src_backend_libpq_pqsignal_c
    src_port_pqsignal_c --> src_include_c_h
    src_port_pqsignal_c --> src_include_port_win32_msvc_unistd_h
    src_port_pthread_barrier_wait_c --> src_include_c_h
    src_port_pthread_barrier_wait_c --> src_include_port_pg_pthread_h
    src_port_qsort_c --> src_include_c_h
    src_port_qsort_c --> src_include_lib_sort_template_h
    src_port_qsort_arg_c --> src_include_c_h
    src_port_qsort_arg_c --> src_include_lib_sort_template_h
    src_port_quotes_c --> src_include_c_h
    src_port_snprintf_c --> src_include_c_h
    src_port_strerror_c --> src_include_c_h
    src_port_strlcat_c --> src_include_c_h
    src_port_strlcpy_c --> src_include_c_h
    src_port_strsep_c --> src_include_c_h
    src_port_strtof_c --> src_backend_utils_adt_float_c
    src_port_strtof_c --> src_include_c_h
    src_port_system_c --> src_include_postgres_fe_h
    src_port_tar_c --> src_include_c_h
    src_port_tar_c --> src_include_pgtar_h
    src_port_timingsafe_bcmp_c --> src_include_c_h
```
