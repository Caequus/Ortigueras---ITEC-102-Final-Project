# `fnmatch` Module Notes

> **One-line idea:** `fnmatch` checks whether a **file name matches a wildcard pattern** such as `*.txt`. It is the "is this the kind of file I want?" detector.
> Built-in module: `import fnmatch`

## Why do we need it?
You rarely want "one file". You want **all the `.jpg` files**, or **every `report_` file**. `fnmatch` gives you pattern matching without learning regular expressions.

**Important:** `fnmatch` only compares **text**. It never opens or looks for a real file. That's why it is used together with `os`.

## The 4 wildcard symbols
| Symbol | Meaning | Example pattern | Matches | Does not match |
|---|---|---|---|---|
| `*` | any characters (even none) | `*.txt` | `a.txt`, `my notes.txt` | `a.pdf` |
| `?` | exactly **one** character | `file?.py` | `file1.py` | `file10.py` |
| `[abc]` | one character from the list/range | `img[0-9].png` | `img5.png` | `imgX.png` |
| `[!abc]` | one character **not** in the list | `img[!0-9].png` | `imgX.png` | `img5.png` |

## Function cheat sheet
| Tool | What it does | Example |
|---|---|---|
| `fnmatch.fnmatch(name, pattern)` | `True/False`; case rules follow your OS | `fnmatch.fnmatch("a.py", "*.py")` -> `True` |
| `fnmatch.fnmatchcase(name, pattern)` | Same, but **always case-sensitive** | `fnmatchcase("A.PY", "*.py")` -> `False` |
| `fnmatch.filter(names, pattern)` | Keep only matching names from a list | `filter(files, "*.txt")` |
| `fnmatch.translate(pattern)` | Turns the wildcard into a regular expression (advanced / bonus) | `fnmatch.translate("*.py")` |

## Case sensitivity (the sneaky one)
| Function | Windows | Linux / Mac |
|---|---|---|
| `fnmatch()` | ignores capitals | capitals matter |
| `fnmatchcase()` | capitals matter | capitals matter |

For the **same behavior everywhere**, use `fnmatchcase(name.lower(), "*.jpg")` with lower-case patterns. The project does exactly this.

## Patterns for several types at once
`fnmatch` accepts **one** pattern at a time. For several, loop over them:
```python
for pattern in ("*.jpg", "*.png"):
    if fnmatch.fnmatchcase(name.lower(), pattern):
        ...
```

## fnmatch is NOT the same as regex
`*` in fnmatch means "anything". In regular expressions `*` means "repeat the previous thing". If you want complex rules (like "3 digits then a letter") you need `re`. For file names, fnmatch is simpler and usually enough.

## Common mistakes
1. Writing `.txt` instead of `*.txt` -> only matches a file literally named `.txt`.
2. Forgetting capitals: `PHOTO.JPG` vs `*.jpg` (see the table above).
3. Expecting `fnmatch` to search folders. It does not; combine it with `os.listdir()` or `os.walk()`.
4. `*` also matches `/` and `\` in the text, so it is for **file names**, not for whole paths with structure.

## Examples in this folder (3 examples, each one prepares a step of the project)
| # | File | Skill | Used in the project |
|---|---|---|---|
| 1 | `01_wildcards.py` | `*`, `?`, `[ ]`, `[! ]`, `filter()` | STEP 0: the `RULES` and `JUNK_PATTERNS` are wildcard patterns |
| 2 | `02_case_sensitivity.py` | `fnmatch` vs `fnmatchcase`, `lower()`, `matches_any()` | STEP 3: same answer on Windows, Mac and Linux |
| 3 | `03_first_match_wins.py` | rule order, `find_category()`, `is_junk()` | STEP 0 and STEP 3: the first matching rule wins |

## Role of `fnmatch` in the combined project
`fnmatch` is the **brain**. `RULES` is a list of `(folder, patterns)`; for every file, `find_category()` tests the patterns in order and the **first match wins** (so `screenshot_*.png` is checked before `*.png`). `JUNK_PATTERNS` uses the same trick to spot `*.tmp`, `*.crdownload` and `~$*` files.
