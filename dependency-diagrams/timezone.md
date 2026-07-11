# `timezone` — file-level dependencies

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
        src_common_file_utils_c["file_utils.c"]
    end
    subgraph "include/port"
        src_include_port_win32_msvc_sys_time_h["win32_msvc/sys/time.h"]
        src_include_port_win32_msvc_unistd_h["win32_msvc/unistd.h"]
    end
    subgraph "include/top"
        src_include_c_h["c.h"]
        src_include_pg_getopt_h["pg_getopt.h"]
        src_include_pgtime_h["pgtime.h"]
        src_include_postgres_fe_h["postgres_fe.h"]
    end
    subgraph "include/utils"
        src_include_utils_hsearch_h["hsearch.h"]
    end
    subgraph "storage"
        src_backend_storage_file_fd_c["file/fd.c"]
    end
    subgraph "timezone"
        src_timezone_localtime_c["localtime.c"]
        src_timezone_pgtz_c["pgtz.c"]
        src_timezone_private_h["private.h"]
        src_timezone_strftime_c["strftime.c"]
        src_timezone_tzfile_h["tzfile.h"]
        src_timezone_zic_c["zic.c"]
    end
    subgraph "utils"
        src_backend_utils_adt_timestamp_c["adt/timestamp.c"]
    end
    src_timezone_localtime_c --> src_backend_utils_adt_timestamp_c
    src_timezone_localtime_c --> src_include_c_h
    src_timezone_localtime_c --> src_timezone_pgtz_c
    src_timezone_localtime_c --> src_timezone_private_h
    src_timezone_localtime_c --> src_timezone_tzfile_h
    src_timezone_pgtz_c --> src_backend_storage_file_fd_c
    src_timezone_pgtz_c --> src_backend_utils_adt_timestamp_c
    src_timezone_pgtz_c --> src_common_file_utils_c
    src_timezone_pgtz_c --> src_include_pgtime_h
    src_timezone_pgtz_c --> src_include_port_win32_msvc_sys_time_h
    src_timezone_pgtz_c --> src_include_utils_hsearch_h
    src_timezone_pgtz_c --> src_timezone_tzfile_h
    src_timezone_private_h --> src_backend_commands_wait_c
    src_timezone_private_h --> src_include_pgtime_h
    src_timezone_private_h --> src_include_port_win32_msvc_unistd_h
    src_timezone_strftime_c --> src_timezone_private_h
    src_timezone_zic_c --> src_include_pg_getopt_h
    src_timezone_zic_c --> src_include_port_win32_msvc_sys_time_h
    src_timezone_zic_c --> src_include_postgres_fe_h
    src_timezone_zic_c --> src_timezone_private_h
    src_timezone_zic_c --> src_timezone_tzfile_h
```
