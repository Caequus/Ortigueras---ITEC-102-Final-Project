# Part 2: Python Modules - `os` + `shutil` + `fnmatch`

**Member:** [Your Name]  |  **Modules chosen:** `os`, `shutil`, `fnmatch` (all built-in)

These three modules work as a team for **file and folder automation**:
`os` looks around, `fnmatch` decides, `shutil` acts.

| Folder | What is inside |
|---|---|
| `01_os/` | `notes.md` + 3 examples |
| `02_shutil/` | `notes.md` + 3 examples |
| `03_fnmatch/` | `notes.md` + 3 examples |
| `04_combined_project_file_organizer/` | **Smart Downloads Organizer** that uses all 3 modules, with `PROJECT_NOTES.md` explaining each module's role step by step |

## How to run
```
cd Part2_Python_Modules/01_os
python3 01_look_around.py        # use "python" instead of "python3" on Windows
```
Every example is a single file you can run on its own. Examples that create files use a temporary `playground` folder and **delete it when finished**.
Requires **Python 3.8+**.

## How the examples lead into the project
Each of the 9 examples prepares one step of `04_combined_project_file_organizer/smart_organizer.py`. The comment at the top of every example says which step it feeds.

| Project step | What happens | Prepared by |
|---|---|---|
| STEP 0 Settings and rules | build paths, wildcard rules | `os/01`, `fnmatch/01` |
| STEP 1 Messy demo folder | make folders, wipe the old demo | `os/02`, `shutil/01` |
| STEP 2 Show the tree, measure sizes | walk and `getsize` | `os/03` |
| STEP 3 Decide the category | `fnmatchcase`, first match wins | `fnmatch/02`, `fnmatch/03` |
| STEP 4 Never overwrite | `exists` + `splitext` | `os/02` |
| STEP 5 Sort and delete junk | `listdir`, `isfile`, `move`, `remove` | `os/01`, `shutil/02` |
| STEP 6 Backup, zip, clean up | `copytree`, `disk_usage`, `make_archive`, `rmtree` | `shutil/01`, `shutil/03` |
