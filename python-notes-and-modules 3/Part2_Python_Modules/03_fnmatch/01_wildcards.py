# fnmatch Example 1: The WILDCARDS - does this file name match my pattern?
#   *      anything (even nothing)          ?      exactly ONE character
#   [abc]  one character from the list      [!abc] one character NOT in the list
#
# USED IN THE PROJECT -> STEP 0: the RULES and JUNK_PATTERNS are just wildcard patterns
#     ("School_Work", ["assessment_task_*", "activity_*", "module_[0-9]*"])
#     JUNK_PATTERNS = ["*.tmp", "*.crdownload", "~$*"]
#
# Functions: fnmatch.fnmatch(), fnmatch.filter()
import fnmatch

tests = [
    # the 4 symbols
    ("notes.txt", "*.txt"),
    ("a.txt", "?.txt"),
    ("ab.txt", "?.txt"),
    ("report_A.pdf", "report_[ABC].pdf"),
    ("img5.png", "img[0-9].png"),
    ("imgX.png", "img[!0-9].png"),
    # the patterns the project really uses
    ("module_11_reviewer.pdf", "module_[0-9]*"),
    ("screenshot_2026-11-10.png", "screenshot_*.png"),
    ("~$report.docx", "~$*"),
    ("download123.tmp", "*.tmp"),
]

print(f"{'NAME':<28}{'PATTERN':<20}MATCH?")
print("-" * 56)
for name, pattern in tests:
    print(f"{name:<28}{pattern:<20}{fnmatch.fnmatch(name, pattern)}")

# filter() keeps only the matching names from a whole list
files = ["cat.jpg", "notes.txt", "selfie.jpg", "song.mp3", "essay.txt"]
print("\nAll files :", files)
print("*.jpg     :", fnmatch.filter(files, "*.jpg"))
print("*.txt     :", fnmatch.filter(files, "*.txt"))
