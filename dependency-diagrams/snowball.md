# `snowball` — file-level dependencies

Arrows point from the file that does the `#include` to the file
it needs.  Ubiquitous modules (see [README](README.md)) are
omitted.  Node names are relative to the subsystem directory;
external nodes are grouped by their subsystem.

## All dependencies

```mermaid
graph LR
    subgraph "include/commands"
        src_include_commands_defrem_h["defrem.h"]
    end
    subgraph "include/mb"
        src_include_mb_pg_wchar_h["pg_wchar.h"]
    end
    subgraph "include/snowball"
        src_include_snowball_libstemmer_snowball_runtime_h["libstemmer/snowball_runtime.h"]
    end
    subgraph "include/tsearch"
        src_include_tsearch_ts_public_h["ts_public.h"]
    end
    subgraph "snowball"
        src_backend_snowball_dict_snowball_c["dict_snowball.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_basque_c["libstemmer/stem_ISO_8859_1_basque.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_catalan_c["libstemmer/stem_ISO_8859_1_catalan.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_danish_c["libstemmer/stem_ISO_8859_1_danish.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_dutch_c["libstemmer/stem_ISO_8859_1_dutch.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_dutch_porter_c["libstemmer/stem_ISO_8859_1_dutch_porter.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_english_c["libstemmer/stem_ISO_8859_1_english.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_finnish_c["libstemmer/stem_ISO_8859_1_finnish.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_french_c["libstemmer/stem_ISO_8859_1_french.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_german_c["libstemmer/stem_ISO_8859_1_german.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_indonesian_c["libstemmer/stem_ISO_8859_1_indonesian.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_irish_c["libstemmer/stem_ISO_8859_1_irish.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_italian_c["libstemmer/stem_ISO_8859_1_italian.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_norwegian_c["libstemmer/stem_ISO_8859_1_norwegian.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_porter_c["libstemmer/stem_ISO_8859_1_porter.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_portuguese_c["libstemmer/stem_ISO_8859_1_portuguese.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_spanish_c["libstemmer/stem_ISO_8859_1_spanish.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_1_swedish_c["libstemmer/stem_ISO_8859_1_swedish.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_2_hungarian_c["libstemmer/stem_ISO_8859_2_hungarian.c"]
        src_backend_snowball_libstemmer_stem_ISO_8859_2_polish_c["libstemmer/stem_ISO_8859_2_polish.c"]
        src_backend_snowball_libstemmer_stem_KOI8_R_russian_c["libstemmer/stem_KOI8_R_russian.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_arabic_c["libstemmer/stem_UTF_8_arabic.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_armenian_c["libstemmer/stem_UTF_8_armenian.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_basque_c["libstemmer/stem_UTF_8_basque.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_catalan_c["libstemmer/stem_UTF_8_catalan.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_danish_c["libstemmer/stem_UTF_8_danish.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_dutch_c["libstemmer/stem_UTF_8_dutch.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_dutch_porter_c["libstemmer/stem_UTF_8_dutch_porter.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_english_c["libstemmer/stem_UTF_8_english.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_esperanto_c["libstemmer/stem_UTF_8_esperanto.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_estonian_c["libstemmer/stem_UTF_8_estonian.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_finnish_c["libstemmer/stem_UTF_8_finnish.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_french_c["libstemmer/stem_UTF_8_french.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_german_c["libstemmer/stem_UTF_8_german.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_greek_c["libstemmer/stem_UTF_8_greek.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_hindi_c["libstemmer/stem_UTF_8_hindi.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_hungarian_c["libstemmer/stem_UTF_8_hungarian.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_indonesian_c["libstemmer/stem_UTF_8_indonesian.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_irish_c["libstemmer/stem_UTF_8_irish.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_italian_c["libstemmer/stem_UTF_8_italian.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_lithuanian_c["libstemmer/stem_UTF_8_lithuanian.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_nepali_c["libstemmer/stem_UTF_8_nepali.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_norwegian_c["libstemmer/stem_UTF_8_norwegian.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_polish_c["libstemmer/stem_UTF_8_polish.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_porter_c["libstemmer/stem_UTF_8_porter.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_portuguese_c["libstemmer/stem_UTF_8_portuguese.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_romanian_c["libstemmer/stem_UTF_8_romanian.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_russian_c["libstemmer/stem_UTF_8_russian.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_serbian_c["libstemmer/stem_UTF_8_serbian.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_spanish_c["libstemmer/stem_UTF_8_spanish.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_swedish_c["libstemmer/stem_UTF_8_swedish.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_tamil_c["libstemmer/stem_UTF_8_tamil.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_turkish_c["libstemmer/stem_UTF_8_turkish.c"]
        src_backend_snowball_libstemmer_stem_UTF_8_yiddish_c["libstemmer/stem_UTF_8_yiddish.c"]
    end
    subgraph "utils"
        src_backend_utils_adt_formatting_c["adt/formatting.c"]
    end
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_basque_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_catalan_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_danish_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_dutch_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_dutch_porter_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_english_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_finnish_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_french_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_german_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_indonesian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_irish_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_italian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_norwegian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_porter_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_portuguese_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_spanish_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_1_swedish_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_2_hungarian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_ISO_8859_2_polish_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_KOI8_R_russian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_arabic_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_armenian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_basque_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_catalan_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_danish_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_dutch_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_dutch_porter_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_english_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_esperanto_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_estonian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_finnish_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_french_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_german_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_greek_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_hindi_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_hungarian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_indonesian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_irish_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_italian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_lithuanian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_nepali_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_norwegian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_polish_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_porter_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_portuguese_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_romanian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_russian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_serbian_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_spanish_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_swedish_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_tamil_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_turkish_c
    src_backend_snowball_dict_snowball_c --> src_backend_snowball_libstemmer_stem_UTF_8_yiddish_c
    src_backend_snowball_dict_snowball_c --> src_backend_utils_adt_formatting_c
    src_backend_snowball_dict_snowball_c --> src_include_commands_defrem_h
    src_backend_snowball_dict_snowball_c --> src_include_mb_pg_wchar_h
    src_backend_snowball_dict_snowball_c --> src_include_snowball_libstemmer_snowball_runtime_h
    src_backend_snowball_dict_snowball_c --> src_include_tsearch_ts_public_h
```
