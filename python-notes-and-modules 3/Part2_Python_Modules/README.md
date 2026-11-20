# Part 2: Python Modules - `os` + `shutil` + `fnmatch`

**Member:** Ortigueras, Charles Jeymel Y.  |  **Modules chosen:** `os`, `shutil`, `fnmatch` (all built-in)

These three modules work as a team for **file and folder automation**, so instead of three unrelated examples, we built **one project** that uses all of them: the **Smart Downloads Organizer**.

| Module | Job in the project |
|---|---|
| `os` | finds folders, lists files, builds paths, checks names |
| `fnmatch` | decides which category each file belongs to |
| `shutil` | moves the files |

## What is inside
| File | What it is |
|---|---|
| `04_combined_project_file_organizer/smart_organizer.py` | the project |
| `04_combined_project_file_organizer/PROJECT_NOTES.md` | notes: a reference of every function used, the code explained step by step, and how the three modules work together |

## How to run
1. Open a terminal inside `Part2_Python_Modules/04_combined_project_file_organizer`.
2. Run:
   ```
   python3 smart_organizer.py        (use "python" on Windows)
   ```
3. The first run creates a `Messy_Downloads` folder next to the script. Put some files in it and run again.
4. Choose **1** to organize (the program shows a plan and asks `y/n`) or **2** to restore a file that was moved to `Deleted_Backup`.

Requires **Python 3.8+**. The program only touches the `Messy_Downloads` and `Deleted_Backup` folders next to the script.
