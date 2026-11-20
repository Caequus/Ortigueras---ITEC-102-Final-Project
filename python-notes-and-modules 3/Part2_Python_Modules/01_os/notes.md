# `os` Module Notes

> **One-line idea:** `os` lets your Python program talk to the **operating system**: look at folders, build paths, create, rename and delete things.
> Built-in module (no install needed): `import os`

## Why do we need it?
Without `os`, Python can only work with data inside your program. With `os`, your scripts can **see and manage real files and folders** on the computer: organizers, backups, cleaners, batch renamers.

## The 3 jobs of `os`
| Job | Question it answers | Main tools |
|---|---|---|
| **Where am I?** | Which folder? Which OS? | `getcwd()`, `name`, `sep`, `getenv()` |
| **Look around** | What is in here? How big? Is it a file or folder? | `listdir()`, `walk()`, `os.path.*` |
| **Change things** | Create, rename, delete | `mkdir()`, `makedirs()`, `rename()`, `remove()`, `rmdir()` |

## Function cheat sheet

### Information
| Tool | What it does | Example |
|---|---|---|
| `os.getcwd()` | Folder your program is currently running in | `os.getcwd()` -> `'C:\\Users\\Yuri'` |
| `os.name` | `'nt'` on Windows, `'posix'` on Linux/Mac | `if os.name == "nt":` |
| `os.sep` | The folder separator for your OS | `'\\'` or `'/'` |
| `os.getenv("NAME")` | Read an environment variable (returns `None` if missing) | `os.getenv("USERNAME")` |
| `os.cpu_count()` | Number of CPU cores | `8` |

### Folders and files
| Tool | What it does | Watch out |
|---|---|---|
| `os.listdir(path)` | Names of everything inside a folder | Gives **names only**, not full paths |
| `os.mkdir(path)` | Create ONE folder | Crashes if it already exists |
| `os.makedirs(path, exist_ok=True)` | Create folder + all missing parents | `exist_ok=True` = no crash if it exists |
| `os.rmdir(path)` | Delete an **empty** folder | Crashes if folder has anything inside |
| `os.remove(path)` | Delete a file | Permanent! No recycle bin |
| `os.rename(old, new)` | Rename (or move) a file/folder | Crashes if `new` already exists on Windows |
| `os.stat(path)` | Many facts: `.st_size`, `.st_mtime` | |
| `os.walk(top)` | Visit **every** folder in a tree | Gives `(root, folders, files)` each time |

### `os.path` (working with path text)
| Tool | What it does | Example result |
|---|---|---|
| `os.path.join(a, b, ...)` | Build a path with the right separator | `Documents\\School\\a.txt` |
| `os.path.exists(p)` | Does it exist? | `True/False` |
| `os.path.isfile(p)` / `isdir(p)` | File or folder? | `True/False` |
| `os.path.abspath(p)` | Make the path absolute (full) | `C:\\Users\\...` |
| `os.path.basename(p)` | The last part (file name) | `report.docx` |
| `os.path.dirname(p)` | Everything before the last part | `C:\\Users\\Yuri` |
| `os.path.split(p)` | `(dirname, basename)` together | |
| `os.path.splitext(p)` | `(name, extension)` | `('report', '.docx')` |
| `os.path.getsize(p)` | Size in bytes | `2048` |
| `os.path.getmtime(p)` | Last-modified time (seconds since 1970) | |
| `os.path.relpath(p, start)` | Path shown relative to `start` | `photos\\cat.jpg` |
| `os.path.expanduser("~")` | Your home folder | `C:\\Users\\Yuri` |

## How `os.walk()` works
```python
for root, folders, files in os.walk("playground"):
    # root    -> the folder we are in right now
    # folders -> names of sub-folders inside root
    # files   -> names of files inside root
```
- It automatically goes into every sub-folder, so you never write the nested loops yourself.
- `topdown=False` visits the **deepest** folders first (needed to delete a tree with `rmdir`).

## Common mistakes
1. **Gluing paths with `+` and `\`.** Use `os.path.join()`.
2. **Backslashes in Windows strings.** `"C:\new"` has a hidden newline (`\n`)! Use `os.path.join()` or raw strings `r"C:\new"`.
3. **Using `rmdir` on a folder with files.** It only deletes empty folders (use `shutil.rmtree`, see the `shutil` notes).
4. **Deleting without checking.** `os.remove()` on a missing file crashes. Check `os.path.exists()` first.
5. **Forgetting `listdir` returns names only.** Join with the folder before checking `isfile()` / `getsize()`.
6. **Confusing "where the script is" with "where I ran it from".** `os.getcwd()` can differ from the script's folder. For the script's folder use `os.path.dirname(os.path.abspath(__file__))`.

## Examples in this folder (3 examples, each one prepares a step of the project)
| # | File | Skill | Used in the project |
|---|---|---|---|
| 1 | `01_look_around.py` | `listdir`, `join`, `isdir`, `splitext`, `getsize` | STEP 0 and STEP 5: scan the folder, skip sub-folders |
| 2 | `02_safe_names_and_folders.py` | `makedirs`, `exists`, `splitext`, `remove` | STEP 4 `safe_destination()` and STEP 5: never overwrite, delete junk |
| 3 | `03_walk_and_measure.py` | `walk`, `basename`, `sep`, `getsize` | STEP 2: draw the folder tree and measure its size |

## Role of `os` in the combined project
`os` is the project's **eyes and hands for small jobs**: it lists the messy folder (`listdir`), skips sub-folders (`isfile`), builds every path (`join`), keeps file extensions (`splitext`), checks for name clashes (`exists`), measures size (`getsize`), draws the folder tree (`walk`), and deletes junk files (`remove`).
