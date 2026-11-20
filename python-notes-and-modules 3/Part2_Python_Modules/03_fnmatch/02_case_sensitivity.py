# fnmatch Example 2: CAPITAL LETTERS - why the project uses fnmatchcase + lower()
#
# USED IN THE PROJECT -> STEP 3: matches_any()
#     if fnmatch.fnmatchcase(filename.lower(), pattern):
#   so "family_photo.JPG" is treated like "family_photo.jpg" on Windows, Mac AND Linux.
#
# Functions: fnmatch.fnmatch(), fnmatch.fnmatchcase(), str.lower()
import fnmatch
import os

name = "family_photo.JPG"

# fnmatch() follows YOUR operating system:
#   Windows -> ignores capitals     Linux and Mac -> capitals matter
print("Your OS code              :", os.name)
print("fnmatch(name, '*.jpg')    :", fnmatch.fnmatch(name, "*.jpg"))

# fnmatchcase() is ALWAYS strict, on every computer
print("fnmatchcase(name, '*.jpg'):", fnmatch.fnmatchcase(name, "*.jpg"))

# The fix: lower-case the name first, and write patterns in lower-case
print("lower() + fnmatchcase     :", fnmatch.fnmatchcase(name.lower(), "*.jpg"))


# The helper from the project: does the name match ANY pattern in a group?
def matches_any(filename, patterns):
    for pattern in patterns:
        if fnmatch.fnmatchcase(filename.lower(), pattern):
            return True
    return False


image_patterns = ["*.jpg", "*.jpeg", "*.png", "*.gif"]

print()
for test in ["family_photo.JPG", "Logo.PNG", "cat.jpg", "notes.txt"]:
    print(f"{test:<18} is an image? {matches_any(test, image_patterns)}")
