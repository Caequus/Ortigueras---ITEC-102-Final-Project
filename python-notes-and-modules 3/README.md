# Python Notes and Modules

**Final Project:** Python for Complete Beginners - *Structured Notes and Modules Assignment*

| | |
|---|---|
| **Group members** | Ortigueras, Collarina, Dela Cruz, [Member 4] |
| **Section / Course** | [BSCS 1A] |
| **Uploaded by** | Ortigueras, Charles Jeymel Y. |

## What is in this repository
- **Part 1: Structured Python Notes.** One folder per core Python topic, each with **8+ examples** that go from Easy to Intermediate to Hard (no OOP or Data Structures topics).
- **Part 2: Python Modules.** `os`, `shutil` and `fnmatch` used together in **one combined project** (Smart Downloads Organizer), with notes that explain what each module does in the project.

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
    └── 04_combined_project_file_organizer/     (smart_organizer.py + PROJECT_NOTES.md)
```

## How to run the code
1. Install **Python 3.10 or newer** (the `match / case` topic needs 3.10; everything else runs on 3.8+).
2. Open a terminal inside the folder you want, for example a Part 1 topic:
   ```
   cd Part1_Core_Topics/01_Basics/01_variables_and_data_types
   python3 01_first_variables.py        (use "python" on Windows)
   ```
3. Part 1 examples are numbered, so run them in order: they get harder as the numbers go up.
4. For the Part 2 project, see `Part2_Python_Modules/README.md`.

## Notes
- The demo videos are **not** included in this repository (they are submitted separately through Google Drive / YouTube).
- The Part 2 project creates `Messy_Downloads` and `Deleted_Backup` folders next to the script when you run it. Git ignores them.
- Part 1 file examples (`12_file_streaming`) create `demo_*` files, `diary.txt` and `gradebook.txt` in the folder you run them from. Git ignores them.
