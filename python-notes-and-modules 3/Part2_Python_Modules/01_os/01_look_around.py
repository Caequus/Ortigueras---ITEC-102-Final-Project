# os Example 1: LOOK AROUND a folder (scan it, skip sub-folders, read extensions and sizes)
#
# USED IN THE PROJECT -> STEP 0 (build every path with join) and STEP 5 (organize):
#     for filename in sorted(os.listdir(DOWNLOADS)):
#         source = os.path.join(DOWNLOADS, filename)
#         if not os.path.isfile(source):      # skip folders such as "Images"
#             continue
#
# Functions: os.path.dirname(), abspath(), join(), os.listdir(), isdir(), splitext(), getsize()
import os

# The folder where THIS script lives, so it works no matter where you run it from
base = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(base, "playground")

# --- Setup: a small messy folder (file name, size in bytes) ---
os.makedirs(os.path.join(target, "Images"), exist_ok=True)
sample = [
    ("cat.jpg", 3000),
    ("notes.txt", 300),
    ("hello_world.py", 120),
    ("old_project.zip", 2000),
    ("download123.tmp", 50),
]
for name, size in sample:
    with open(os.path.join(target, name), "w") as file:
        file.write("x" * size)

# --- The scan ---
print("Scanning:", os.path.basename(target))
print()

file_count = 0
for name in sorted(os.listdir(target)):
    full_path = os.path.join(target, name)       # listdir gives NAMES only, so we build the path

    if os.path.isdir(full_path):
        print(f"  [FOLDER] {name}   (skipped: the organizer only moves files)")
        continue

    extension = os.path.splitext(name)[1]        # ".jpg"
    size = os.path.getsize(full_path)
    print(f"  [FILE]   {name:<16} extension: {extension:<5} size: {size} bytes")
    file_count += 1

print(f"\n{file_count} file(s) found that need sorting")

# --- Cleanup (os only): topdown=False visits the deepest folders first ---
for root, folders, files in os.walk(target, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    os.rmdir(root)
