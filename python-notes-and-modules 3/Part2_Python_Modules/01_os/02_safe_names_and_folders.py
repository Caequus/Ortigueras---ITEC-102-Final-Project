# os Example 2: NEVER OVERWRITE - make folders, check names, delete junk
#
# USED IN THE PROJECT -> STEP 4 safe_destination() (this is the SAME function),
#                        STEP 5 (makedirs for the category folder, remove for junk files)
#
# Functions: os.makedirs(), os.path.exists(), os.path.splitext(), os.path.join(), os.remove()
import os

base = os.path.dirname(os.path.abspath(__file__))
playground = os.path.join(base, "playground")
images = os.path.join(playground, "Images")

# 1. Create the category folder if it is not there yet (exist_ok=True = no crash if it exists)
os.makedirs(images, exist_ok=True)

# Pretend Images already contains a cat.jpg
with open(os.path.join(images, "cat.jpg"), "w") as file:
    file.write("first cat")


# 2. Find a file name that is still FREE
def safe_destination(folder, filename):
    destination = os.path.join(folder, filename)
    if not os.path.exists(destination):          # free name? use it as it is
        return destination

    name, extension = os.path.splitext(filename)  # "cat.jpg" -> "cat" and ".jpg"
    counter = 1
    while True:
        new_name = f"{name} ({counter}){extension}"
        destination = os.path.join(folder, new_name)
        if not os.path.exists(destination):
            return destination
        counter += 1


print("dog.jpg  ->", os.path.basename(safe_destination(images, "dog.jpg")))
print("cat.jpg  ->", os.path.basename(safe_destination(images, "cat.jpg")))

# Take that free name, then ask again: the answer moves on to the next number
with open(safe_destination(images, "cat.jpg"), "w") as file:
    file.write("second cat")
print("cat.jpg again ->", os.path.basename(safe_destination(images, "cat.jpg")))
print("Files in Images:", sorted(os.listdir(images)))

# 3. Deleting junk: os.remove (check first, it crashes on a missing file)
junk = os.path.join(playground, "download123.tmp")
with open(junk, "w") as file:
    file.write("half-finished download")
print("\nJunk exists before remove?", os.path.exists(junk))
if os.path.exists(junk):
    os.remove(junk)
print("Junk exists after remove? ", os.path.exists(junk))

# --- Cleanup (os only) ---
for root, folders, files in os.walk(playground, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    os.rmdir(root)
