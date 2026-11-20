# shutil Example 1: BACKUP FIRST - copy a whole folder before changing anything
#
# USED IN THE PROJECT -> STEP 6 main(): shutil.copytree(DOWNLOADS, BACKUP)
#                        STEP 1: shutil.rmtree() wipes the old demo folder so every run starts fresh
#
# Functions: shutil.copytree(), shutil.rmtree()  (os is used to build and count)
import os
import shutil

base = os.path.dirname(os.path.abspath(__file__))
playground = os.path.join(base, "playground")
downloads = os.path.join(playground, "Messy_Downloads")
backup = os.path.join(playground, "Backup_Before_Sorting")

# --- Setup: a messy folder with a sub-folder ---
os.makedirs(os.path.join(downloads, "Images"), exist_ok=True)
for relative_path in ["cat.jpg", "notes.txt", "song.mp3", os.path.join("Images", "old_cat.jpg")]:
    with open(os.path.join(downloads, relative_path), "w") as file:
        file.write("sample content")


def count_files(folder):
    total = 0
    for root, folders, files in os.walk(folder):
        total += len(files)
    return total


# copytree crashes if the destination already exists, so remove an old backup first
if os.path.exists(backup):
    shutil.rmtree(backup)
shutil.copytree(downloads, backup)       # copies folders, sub-folders and files

print("Files in Messy_Downloads :", count_files(downloads))
print("Files in the backup      :", count_files(backup))

# Prove it is a REAL copy: delete a file from the original, the backup still has it
os.remove(os.path.join(downloads, "notes.txt"))
print("\nAfter deleting notes.txt from the original:")
print("Files in Messy_Downloads :", count_files(downloads))
print("Files in the backup      :", count_files(backup))
print("notes.txt still in backup?", os.path.exists(os.path.join(backup, "notes.txt")))

shutil.rmtree(playground)                # cleanup: deletes the folder AND everything inside
