# shutil Example 2: MOVE files into folders (and why we need safe_destination)
#
# USED IN THE PROJECT -> STEP 5 organize():
#     shutil.move(source, safe_destination(target_folder, filename))
#
# Functions: shutil.move()  (os is used to build paths and check names)
import os
import shutil

base = os.path.dirname(os.path.abspath(__file__))
playground = os.path.join(base, "playground")
downloads = os.path.join(playground, "Downloads")
documents = os.path.join(downloads, "Documents")
images = os.path.join(downloads, "Images")

os.makedirs(images, exist_ok=True)
os.makedirs(documents, exist_ok=True)

# Setup: two loose files, plus a cat.jpg that is ALREADY inside Images
for path in [os.path.join(downloads, "notes.txt"),
             os.path.join(downloads, "cat.jpg"),
             os.path.join(images, "cat.jpg")]:
    with open(path, "w") as file:
        file.write("sample")

# 1. Move a file INTO a folder (it keeps its name)
shutil.move(os.path.join(downloads, "notes.txt"), documents)
print("Documents now contains:", os.listdir(documents))

# 2. Move AND rename in one step: give a new file name as the destination
shutil.move(os.path.join(downloads, "cat.jpg"), os.path.join(images, "cat (1).jpg"))
print("Images now contains   :", sorted(os.listdir(images)))

# 3. What if the name is taken? Make another cat.jpg and try to move it into Images
with open(os.path.join(downloads, "cat.jpg"), "w") as file:
    file.write("a second cat")

try:
    shutil.move(os.path.join(downloads, "cat.jpg"), images)
except shutil.Error:
    print("\nshutil.move REFUSED: Images already has a cat.jpg")
    print("That is why the project asks safe_destination() for a free name first.")

shutil.rmtree(playground)   # cleanup
