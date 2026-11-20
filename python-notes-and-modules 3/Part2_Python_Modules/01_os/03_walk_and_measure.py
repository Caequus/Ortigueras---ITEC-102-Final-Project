# os Example 3: WALK a folder tree, draw it, and MEASURE it
#
# USED IN THE PROJECT -> STEP 2: show_tree(), folder_size() and readable()
#                        (the BEFORE / AFTER pictures and the size check before the backup)
#
# Functions: os.walk(), os.path.basename(), os.sep, os.path.getsize(), os.path.join()
import os


def show_tree(path):
    for root, folders, files in os.walk(path):
        folders.sort()                                  # keep the output in a nice order
        level = root.replace(path, "").count(os.sep)    # how deep are we?
        indent = "    " * level
        print(f"{indent}{os.path.basename(root)}/")
        for name in sorted(files):
            print(f"{indent}    {name}")


def folder_size(path):
    total = 0
    for root, folders, files in os.walk(path):
        for name in files:
            total += os.path.getsize(os.path.join(root, name))
    return total


def readable(size):
    if size < 1024:
        return f"{size} B"
    elif size < 1024 * 1024:
        return f"{size / 1024:.1f} KB"
    return f"{size / (1024 * 1024):.1f} MB"


base = os.path.dirname(os.path.abspath(__file__))
top = os.path.join(base, "playground", "Downloads")

# --- Setup: a tree with files of different sizes (folder, file name, size) ---
sample = [
    ("", "notes.txt", 300),
    ("", "setup.exe", 1500),
    ("Images", "cat.jpg", 3000),
    ("Images", "family_photo.jpg", 4200),
    ("Music", "lofi_beats.mp3", 6000),
]
for folder, name, size in sample:
    os.makedirs(os.path.join(top, folder), exist_ok=True)
    with open(os.path.join(top, folder, name), "w") as file:
        file.write("x" * size)

# --- Draw it and measure it ---
print("TREE:")
show_tree(top)

print("\nSIZES:")
print("Whole folder :", readable(folder_size(top)))
print("Images only  :", readable(folder_size(os.path.join(top, "Images"))))
print("Music only   :", readable(folder_size(os.path.join(top, "Music"))))

# --- Cleanup (os only) ---
for root, folders, files in os.walk(os.path.join(base, "playground"), topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    os.rmdir(root)
