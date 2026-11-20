# shutil Example 3: CHECK SPACE, ZIP the result, CLEAN UP
#
# USED IN THE PROJECT -> STEP 6 main():
#     total, used, free = shutil.disk_usage(BASE)        (enough room for a backup + zip?)
#     zip_path = shutil.make_archive(ZIP_NAME, "zip", DOWNLOADS)
#     shutil.rmtree(DOWNLOADS) ... at the end (reset the demo)
#
# Functions: shutil.disk_usage(), shutil.make_archive(), shutil.rmtree()
import os
import shutil


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
    elif size < 1024 ** 3:
        return f"{size / (1024 * 1024):.1f} MB"
    return f"{size / 1024 ** 3:.1f} GB"


base = os.path.dirname(os.path.abspath(__file__))
playground = os.path.join(base, "playground")
sorted_folder = os.path.join(playground, "Sorted_Downloads")

# --- Setup: an already-sorted folder ---
for folder, name, size in [("Images", "cat.jpg", 3000), ("Documents", "notes.txt", 300),
                           ("Music", "lofi_beats.mp3", 6000)]:
    os.makedirs(os.path.join(sorted_folder, folder), exist_ok=True)
    with open(os.path.join(sorted_folder, folder, name), "w") as file:
        file.write("x" * size)

# 1. Is there enough free disk space? (we plan for about 3 times the folder size)
total, used, free = shutil.disk_usage(base)
needed = folder_size(sorted_folder) * 3
print(f"Free disk space : {readable(free)}")
print(f"Space needed    : {readable(needed)}")
if free < needed:
    print("Not enough space. Stopping.")
else:
    print("Enough space, continuing.")

    # 2. Zip the whole folder (write the name WITHOUT .zip, it is added for you)
    zip_path = shutil.make_archive(os.path.join(playground, "Sorted_Downloads"), "zip", sorted_folder)
    print("\nZip created :", os.path.basename(zip_path))
    print("Zip size    :", readable(os.path.getsize(zip_path)))

    # 3. Cleanup: rmtree deletes a folder that is NOT empty (os.rmdir cannot)
    shutil.rmtree(sorted_folder)
    print("Sorted folder deleted? ", not os.path.exists(sorted_folder))
    print("Zip still there?       ", os.path.exists(zip_path))

shutil.rmtree(playground)   # final cleanup
