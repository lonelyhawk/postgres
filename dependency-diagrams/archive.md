# `archive` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "access"
        src_backend_access_transam_xlog_c["transam/xlog.c"]
    end
    subgraph "archive"
        src_backend_archive_shell_archive_c["shell_archive.c"]
    end
    subgraph "commands"
        src_backend_commands_wait_c["wait.c"]
    end
    subgraph "common"
        src_common_percentrepl_c["percentrepl.c"]
    end
    subgraph "include/archive"
        src_include_archive_archive_module_h["archive_module.h"]
    end
    subgraph "utils"
        src_backend_utils_activity_wait_event_c["activity/wait_event.c"]
    end
    src_backend_archive_shell_archive_c --> src_backend_access_transam_xlog_c
    src_backend_archive_shell_archive_c --> src_backend_commands_wait_c
    src_backend_archive_shell_archive_c --> src_backend_utils_activity_wait_event_c
    src_backend_archive_shell_archive_c --> src_common_percentrepl_c
    src_backend_archive_shell_archive_c --> src_include_archive_archive_module_h
```
