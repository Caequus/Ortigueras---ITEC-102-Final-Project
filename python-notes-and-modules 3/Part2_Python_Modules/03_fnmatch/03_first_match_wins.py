# fnmatch Example 3: THE BRAIN - rules checked in order, FIRST match wins
#
# USED IN THE PROJECT -> STEP 0 (RULES) and STEP 3 (find_category, is_junk)
#   This is a mini version of the organizer's brain. No files are touched: only names.
#
# Functions: fnmatch.fnmatchcase()
import fnmatch

# Order matters! "screenshot_*.png" must come BEFORE the general "*.png"
RULES = [
    ("Screenshots", ["screenshot_*.png"]),
    ("Images", ["*.jpg", "*.jpeg", "*.png", "*.gif"]),
    ("Documents", ["*.pdf", "*.docx", "*.txt"]),
    ("Music", ["*.mp3", "*.wav"]),
]
JUNK_PATTERNS = ["*.tmp", "*.crdownload", "~$*"]


def matches_any(filename, patterns):
    for pattern in patterns:
        if fnmatch.fnmatchcase(filename.lower(), pattern):
            return True
    return False


def find_category(filename, rules):
    for folder_name, patterns in rules:
        if matches_any(filename, patterns):
            return folder_name          # stop at the FIRST rule that matches
    return "Others"                     # nothing matched


def is_junk(filename):
    return matches_any(filename, JUNK_PATTERNS)


names = [
    "Screenshot_2026-11-10.png",
    "cat.jpg",
    "family_photo.JPG",
    "Module_11_Reviewer.pdf",
    "lofi_beats.mp3",
    "setup.exe",
    "download123.tmp",
    "~$report.docx",
]

print("Decisions with the CORRECT rule order:")
for name in names:
    if is_junk(name):
        print(f"  {name:<28} -> DELETE (junk)")
    else:
        print(f"  {name:<28} -> {find_category(name, RULES)}/")

# Now swap the first two rules and watch the screenshot get lost in Images
WRONG_ORDER = [
    ("Images", ["*.jpg", "*.jpeg", "*.png", "*.gif"]),
    ("Screenshots", ["screenshot_*.png"]),
]
print("\nWith the WRONG order (Images first):")
print("  Screenshot_2026-11-10.png ->", find_category("Screenshot_2026-11-10.png", WRONG_ORDER) + "/")
