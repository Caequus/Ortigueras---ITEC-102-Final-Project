# Smart Downloads Organizer (`os` + `fnmatch` + `shutil`)

The program scans the files directly inside `Messy_Downloads`, plans a category for each file, and asks once before applying the plan. It does not ask for file names in the terminal.

## Use it

1. Put the files you want to sort directly inside `Messy_Downloads`, next to `smart_organizer.py`.
2. Run `python smart_organizer.py`.
3. Review the plan. Enter `y` to apply it or `n` to leave everything as it is.

If `Messy_Downloads` does not exist, the program creates an empty folder. It does not clear or replace the folder at startup. It handles files directly inside the folder and skips category subfolders when it runs again.

## What the rules do

- `School_Work`: names beginning with `assessment_task_`, `activity_`, or `module_` followed by a number.
- `Screenshots`: `screenshot_*.png` or `screenshot *.png`.
- `Images`, `Documents`, `Videos`, `Music`, `Code`, and `Archives`: selected by file extension.
- `Others`: files that do not match another category.
- Temporary names matching `*.tmp`, `*.crdownload`, or `~$*` are listed for deletion in the plan. They are deleted only if you approve the complete plan.

Matching is case-insensitive because the program lower-cases file names. If a category folder already contains a file with the same name, the program adds a number such as `(1)` rather than overwriting it.

## Modules used

| Module | Use |
|---|---|
| `os` | Builds paths, lists files, checks file types, creates category folders, and removes approved junk files. |
| `fnmatch` | Matches names against the category and temporary-file patterns. |
| `shutil` | Moves files into their category folders. |
