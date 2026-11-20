# Project: Smart Downloads Organizer (`os` + `fnmatch` + `shutil`)

**What it does:** sorts the messy files inside a folder into neat category folders. It first shows a **plan** and asks for your OK. Temporary files are **not deleted**: they are moved to a `Deleted_Backup` folder, and a menu option can restore them. Nothing is ever overwritten.

## How to run
1. Put some files inside `Messy_Downloads` (the program creates this folder next to the script the first time you run it).
2. Run the program from the project folder:
   ```
   python3 smart_organizer.py        (use "python" on Windows)
   ```
3. Choose **1** to organize (type `y` to apply the plan) or **2** to restore a backed-up file.

## The team: who does what?
| Module | Job in the project | Think of it as... |
|---|---|---|
| `os` | Finds the folders, lists the files, builds paths, checks names | The **eyes** |
| `fnmatch` | Decides which category each file belongs to | The **brain** |
| `shutil` | Moves the files | The **muscles** |

---

## Module reference: every function the project uses

### `os`: talking to the operating system
| Function | What it does | Where it is used |
|---|---|---|
| `os.path.abspath(__file__)` | Full path of this script (`__file__` is the script's own name) | `BASE` |
| `os.path.dirname(path)` | The folder part of a path | `BASE` (the folder containing the script) |
| `os.path.join(a, b)` | Builds a path with the correct slash for Windows or Mac | everywhere a path is made |
| `os.makedirs(path, exist_ok=True)` | Creates a folder (and parents), no crash if it already exists | `Messy_Downloads`, category folders, `Deleted_Backup` |
| `os.listdir(path)` | Names of everything inside a folder (names only, not full paths) | scanning `Messy_Downloads` and `Deleted_Backup` |
| `os.path.isfile(path)` | Is it a file? | skip folders such as `Images` |
| `os.path.isdir(path)` | Is it a folder? | does `Deleted_Backup` exist yet? |
| `os.path.exists(path)` | Does this path already exist? | `safe_destination()`: is the name taken? |
| `os.path.splitext(name)` | Splits `cat.jpg` into `cat` and `.jpg` | `safe_destination()`: keep the extension in `cat (1).jpg` |
| `os.path.basename(path)` | Just the file name of a path | shorter text in the plan |

### `fnmatch`: matching file names with wildcards
| Function / symbol | What it does |
|---|---|
| `fnmatch.fnmatchcase(name, pattern)` | `True` if the name matches the pattern. Always strict about capital letters, on every computer |
| `*` | any characters, so `*.jpg` matches every JPG |
| `[0-9]` | exactly one digit, so `module_[0-9]*` matches `module_11_reviewer.pdf` |
| `~$*` | `~$` are normal characters here, so it matches Word's temporary `~$report.docx` |

`fnmatch` only compares **text**. It never opens or looks for a real file, so `os` and `fnmatch` work as a pair.

### `shutil`: bigger file jobs
| Function | What it does | Where it is used |
|---|---|---|
| `shutil.move(source, destination)` | Moves a file, and renames it if the destination has a different name | sorting, backing up junk, and restoring (3 places) |

---

## How the program works, step by step

### 1. Settings
```python
BASE = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS = os.path.join(BASE, "Messy_Downloads")
RECOVERY_BACKUP = os.path.join(BASE, "Deleted_Backup")
```
> **`os`:** `BASE` is the folder where the script lives, so the program works no matter where you launch it from. `join` builds the other two paths. `Deleted_Backup` sits **next to** `Messy_Downloads`, not inside it, so the organizer never scans its own backups.

### 2. The rules
```python
RULES = [
    ("School_Work", ["assessment_task_*", "activity_*", "module_[0-9]*"]),
    ("Screenshots", ["screenshot_*.png", "screenshot *.png"]),
    ("Images",      ["*.jpg", "*.jpeg", "*.png", "*.gif"]),
    ...
]
JUNK_PATTERNS = ["*.tmp", "*.crdownload", "~$*"]
```
> **`fnmatch`:** the rules are plain wildcard patterns. **The first matching rule wins**, so `screenshot_*.png` is placed above `*.png`; otherwise screenshots would be filed as ordinary images. Patterns are written in lower-case because file names are lower-cased before matching.

### 3. The decision functions
```python
def matches_any(filename, patterns):
    return any(fnmatch.fnmatchcase(filename.lower(), pattern) for pattern in patterns)

def find_category(filename):
    for folder_name, patterns in RULES:
        if matches_any(filename, patterns):
            return folder_name
    return "Others"
```
> **`fnmatch`:** `fnmatchcase` plus `.lower()` gives the **same answer on Windows, Mac and Linux**, so `family_photo.JPG` still matches `*.jpg`. `matches_any` asks "does at least one pattern match?". `find_category` walks through the rules in order and returns the first category that fits, or `Others` if nothing does. `is_junk` uses the same helper with `JUNK_PATTERNS`.

### 4. Never overwrite a file
```python
def safe_destination(folder, filename):
    destination = os.path.join(folder, filename)
    if not os.path.exists(destination):
        return destination
    name, extension = os.path.splitext(filename)
    counter = 1
    while True:
        new_name = f"{name} ({counter}){extension}"
        ...
```
> **`os`:** `exists` detects a name clash, and `splitext` keeps the extension, so `cat.jpg` becomes `cat (1).jpg` and not `cat.jpg (1)`. It is used for sorting, for the backup folder and for restoring, so no action can replace an existing file.

### 5. The main job: plan first, then do it
```python
def organize_folder(dry_run):
    for filename in sorted(os.listdir(DOWNLOADS)):
        source = os.path.join(DOWNLOADS, filename)
        if not os.path.isfile(source):
            continue
        if is_junk(filename):
            backup_destination = safe_destination(RECOVERY_BACKUP, filename)
            if not dry_run:
                os.makedirs(RECOVERY_BACKUP, exist_ok=True)
                shutil.move(source, backup_destination)
            ...
            continue
        category = find_category(filename)
        ...
        if not dry_run:
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(source, destination)
```
> **`os`:** `listdir` + `isfile` means "look at real files only and skip the category folders". `makedirs` creates the category folder the first time it is needed.
> **`fnmatch`:** `is_junk` and `find_category` make every decision.
> **`shutil`:** `move` puts the file in its new home. Junk goes to `Deleted_Backup` instead of being deleted.
> **One function, two modes:** with `dry_run=True` it only **prints** the plan; with `dry_run=False` it does the same steps for real.

### 6. Ask before acting
```python
print("PLAN:")
organize_folder(dry_run=True)
answer = input("Apply this plan? (y/n): ")
if answer == "y":
    organize_folder(dry_run=False)
```
The user sees exactly what will happen first. Anything other than `y` cancels with no change.

### 7. Restore a backed-up file
```python
backup_files = sorted(name for name in os.listdir(RECOVERY_BACKUP) if os.path.isfile(...))
for number, filename in enumerate(backup_files, start=1):
    print(f"  {number}. {filename}")
...
destination = safe_destination(DOWNLOADS, filename)
shutil.move(source, destination)
```
> **`os`:** `isdir` checks the backup folder exists; `listdir` + `isfile` list the backed-up files.
> **`shutil`:** `move` takes the chosen file back to `Messy_Downloads`.
> The number the user types is converted with `int()` inside `try/except`, so typing letters, `0` or a number that is not in the list only prints a message and never crashes.

### 8. The menu
`main()` makes sure `Messy_Downloads` exists, shows the two options and calls `organize_downloads()` or `restore_from_backup()`. The last two lines of the file, `if __name__ == "__main__": main()`, mean "start the menu only when this file is run directly".

---

## Follow four files through the program
| File | What happens |
|---|---|
| `Screenshot_2026-11-10.png` | `listdir` finds it, `isfile` says it is a file, `is_junk` says no, `find_category` returns **Screenshots** (that rule comes before Images), `makedirs` creates the folder and `shutil.move` moves it |
| `cat.jpg` (and `Images/cat.jpg` already exists) | category is **Images**, `exists` says the name is taken, so `safe_destination` returns `cat (1).jpg` and nothing is overwritten |
| `~$report.docx` | matches the junk pattern `~$*`, so it is moved to `Deleted_Backup` and can be restored |
| `setup.exe` | no rule matches, so it goes to **Others** |

## Where each module appears
| Module | Functions used |
|---|---|
| `os` | `path.abspath`, `path.dirname`, `path.join`, `makedirs`, `listdir`, `path.isfile`, `path.isdir`, `path.exists`, `path.splitext`, `path.basename` |
| `fnmatch` | `fnmatchcase` (used for categories **and** for junk) |
| `shutil` | `move` (sorting, backing up, restoring) |

## Python features used besides the three modules
| Feature | Where | Plain meaning |
|---|---|---|
| f-strings with `:<28` | the plan lines | insert values and pad them so the arrows line up |
| `any(... for ... in ...)` | `matches_any` | "is at least one of these True?" |
| `sorted(...)` | listing files | alphabetical order, so the output is predictable |
| list built with `[name for name in ...]` | `organize_downloads` | a loop and a filter in one line |
| `enumerate(..., start=1)` | restore list | numbers the items 1, 2, 3 |
| `try / except ValueError` | restore | catch bad typing instead of crashing |
| `while True` with `return` | `safe_destination` | keep trying numbers until a free name is found |
| `if __name__ == "__main__":` | end of file | run the menu only when this file is run directly |

## Sample run (shortened)
```
PLAN:
  MOVE    Assessment_Task_6-1.docx     -> School_Work/Assessment_Task_6-1.docx
  MOVE    Screenshot_2026-11-10.png    -> Screenshots/Screenshot_2026-11-10.png
  MOVE    cat.jpg                      -> Images/cat (1).jpg
  BACKUP  download123.tmp              -> Deleted_Backup/download123.tmp
  MOVE    family_photo.JPG             -> Images/family_photo.JPG
  MOVE    setup.exe                    -> Others/setup.exe
  BACKUP  ~$report.docx                -> Deleted_Backup/~$report.docx

Planned moves: 9 | Files to back up: 3
Apply this plan? (y/n): y

Finished. Files moved: 9 | Files backed up: 3
```

## Try it yourself (extension ideas)
- Add a new rule such as `("Presentations", ["*.pptx", "*.ppt"])` above `Documents` and watch the order rule at work.
- Add another junk pattern such as `"*.bak"`.
- Test with a **copy** of a real folder, never your real one first.
