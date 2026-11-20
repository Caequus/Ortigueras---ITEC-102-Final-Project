# `shutil` Module Notes

> **One-line idea:** `shutil` ("shell utilities") does the **big jobs** that `os` cannot do easily: copy files, copy or delete whole folders, move things, make zip files.
> Built-in module: `import shutil`

## `os` vs `shutil`
| Task | `os` | `shutil` |
|---|---|---|
| Rename a file | `os.rename()` | `shutil.move()` |
| Delete a file | `os.remove()` | (use `os.remove`) |
| Delete an **empty** folder | `os.rmdir()` | |
| Delete a folder **with stuff inside** | no | **`shutil.rmtree()`** |
| Copy a file | no | **`shutil.copy()`** |
| Copy a whole folder | no | **`shutil.copytree()`** |
| Make / open zip files | no | **`make_archive()` / `unpack_archive()`** |

Rule of thumb: `os` = small, single actions. `shutil` = copying, moving, bulk actions and archives.

## Function cheat sheet
| Tool | What it does | Notes |
|---|---|---|
| `shutil.copy(src, dst)` | Copy a file's **content** | `dst` can be a new name or a folder |
| `shutil.copy2(src, dst)` | Copy content **+ metadata** (dates) | Best for backups |
| `shutil.move(src, dst)` | Move a file/folder; also renames | Works across drives |
| `shutil.copytree(src, dst)` | Copy a whole folder and everything inside | Crashes if `dst` exists unless `dirs_exist_ok=True` |
| `shutil.copytree(..., ignore=...)` | Copy but **skip** some files | Use with `ignore_patterns()` |
| `shutil.ignore_patterns("*.tmp", ...)` | Build a "skip list" with wildcards | Same wildcard style as `fnmatch` |
| `shutil.rmtree(path)` | Delete a folder and **everything** inside | **No recycle bin!** `ignore_errors=True` avoids crashes |
| `shutil.disk_usage(path)` | `(total, used, free)` in bytes | |
| `shutil.which("name")` | Full path of a program, or `None` | e.g. `which("git")` |
| `shutil.get_terminal_size()` | Width and height of the terminal | `.columns`, `.lines` |
| `shutil.make_archive(name, "zip", folder)` | Zip a folder | Do **not** write `.zip` in `name`, it is added for you; returns the zip path |
| `shutil.unpack_archive(file, folder)` | Extract a zip | |

## `copy` vs `copy2`
```python
shutil.copy(a, b)    # new "last modified" date = right now
shutil.copy2(a, b)   # keeps the ORIGINAL dates
```

## Safety rules
1. `rmtree` and `move` can destroy work. **Test on a practice folder first.**
2. **Backup before big changes:** `copytree` first, then change things (the combined project does this).
3. Check free space with `disk_usage` before copying a lot of data.
4. `move()` will **overwrite** a file with the same name in some cases. Check `os.path.exists()` before moving (the project's `safe_destination()` does this).

## Common mistakes
1. Writing `.zip` inside the name given to `make_archive` -> you get `file.zip.zip`.
2. Running `copytree` twice without `dirs_exist_ok=True` -> `FileExistsError`.
3. Using `os.rmdir` on a folder that is not empty -> use `shutil.rmtree`.
4. Forgetting the destination can be a **folder** (keeps the name) or a **file name** (renames).

## Examples in this folder (3 examples, each one prepares a step of the project)
| # | File | Skill | Used in the project |
|---|---|---|---|
| 1 | `01_backup_with_copytree.py` | `copytree`, `rmtree` | STEP 6 backup and STEP 1 fresh start |
| 2 | `02_move_files.py` | `move` (into a folder, with rename, and when the name is taken) | STEP 5: put each file in its category folder |
| 3 | `03_zip_space_and_cleanup.py` | `disk_usage`, `make_archive`, `rmtree` | STEP 6: check space, zip the result, clean up |

## Role of `shutil` in the combined project
`shutil` does all the **heavy actions**: `disk_usage` (is there enough space?), `copytree` (backup before touching anything), `move` (put each file into its category folder), `make_archive` (zip the sorted result), and `rmtree` (reset or clean up the demo folders).
