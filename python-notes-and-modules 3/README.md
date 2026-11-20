# Python Notes and Modules

**Final Project:** Python for Complete Beginners - *Structured Notes and Modules Assignment*

| | |
|---|---|
| **Group members** | [Member 1], [Member 2], [Member 3], [Member 4] |
| **Section / Course** | [BSCS 1A] |
| **Uploaded by** | [Your Name] |

## What is in this repository
- **Part 1: Structured Python Notes.** One folder per core Python topic, each with **8+ examples** that go from Easy to Intermediate to Hard (no OOP or Data Structures topics).
- **Part 2: Python Modules.** `os`, `shutil` and `fnmatch`: notes, **3 examples per module** (each one prepares a step of the project), and **one combined project** (Smart Downloads Organizer) that shows what each module does.

## Folder structure
```
python-notes-and-modules/
├── README.md
├── .gitignore
├── Part1_Core_Topics/
│   ├── 01_Basics/
│   │   ├── 01_variables_and_data_types/
│   │   ├── 02_input_and_output/
│   │   └── 03_operators_and_type_casting/
│   ├── 02_Decision_Making/
│   │   ├── 04_if_elif_else/
│   │   └── 05_match_case/
│   ├── 03_Loops/
│   │   ├── 06_while_loops/
│   │   ├── 07_for_loops_and_range/
│   │   └── 08_loop_control_and_nested_loops/
│   ├── 04_Strings/
│   │   └── 09_string_basics_and_methods/
│   ├── 05_Functions/
│   │   ├── 10_functions_basics/
│   │   └── 11_functions_advanced/
│   └── 06_Files/
│       └── 12_file_streaming/
└── Part2_Python_Modules/
    ├── README.md
    ├── 01_os/                                  (notes.md + 3 examples)
    ├── 02_shutil/                              (notes.md + 3 examples)
    ├── 03_fnmatch/                             (notes.md + 3 examples)
    └── 04_combined_project_file_organizer/     (smart_organizer.py + PROJECT_NOTES.md)
```

## How to run any example
1. Install **Python 3.10 or newer** (the `match / case` topic needs 3.10; everything else runs on 3.8+).
2. Open a terminal inside the folder you want, for example:
   ```
   cd Part2_Python_Modules/01_os
   python 01_where_am_i.py
   ```
3. Examples are numbered, so run them in order: they get harder as the numbers go up.

## Notes
- The demo videos are **not** included in this repository (they are submitted separately through Google Drive / YouTube).
- Part 2 examples that create files use a temporary `playground` folder and delete it afterward.
- Part 1 file examples (`12_file_streaming`) create `demo_*` files, `diary.txt` and `gradebook.txt` in the folder you run them from. Git ignores them.
