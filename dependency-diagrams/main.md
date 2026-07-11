# `main` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "bootstrap"
        src_backend_bootstrap_bootstrap_c["bootstrap.c"]
    end
    subgraph "common"
        src_common_username_c["username.c"]
    end
    subgraph "include/port"
        src_include_port_win32_msvc_sys_param_h["win32_msvc/sys/param.h"]
        src_include_port_win32_msvc_unistd_h["win32_msvc/unistd.h"]
    end
    subgraph "include/tcop"
        src_include_tcop_tcopprot_h["tcopprot.h"]
    end
    subgraph "main"
        src_backend_main_main_c["main.c"]
    end
    subgraph "postmaster"
        src_backend_postmaster_postmaster_c["postmaster.c"]
    end
    subgraph "utils"
        src_backend_utils_adt_pg_locale_c["adt/pg_locale.c"]
        src_backend_utils_misc_help_config_c["misc/help_config.c"]
        src_backend_utils_misc_ps_status_c["misc/ps_status.c"]
    end
    src_backend_main_main_c --> src_backend_bootstrap_bootstrap_c
    src_backend_main_main_c --> src_backend_postmaster_postmaster_c
    src_backend_main_main_c --> src_backend_utils_adt_pg_locale_c
    src_backend_main_main_c --> src_backend_utils_misc_help_config_c
    src_backend_main_main_c --> src_backend_utils_misc_ps_status_c
    src_backend_main_main_c --> src_common_username_c
    src_backend_main_main_c --> src_include_port_win32_msvc_sys_param_h
    src_backend_main_main_c --> src_include_port_win32_msvc_unistd_h
    src_backend_main_main_c --> src_include_tcop_tcopprot_h
```
