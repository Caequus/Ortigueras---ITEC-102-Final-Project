"""
SMART DOWNLOADS ORGANIZER (os + fnmatch + shutil)

Put files in Messy_Downloads next to this script and run the program. It plans
to sort every file directly inside that folder, then asks before applying the
plan. Temporary files are listed for deletion in the plan.
"""
import os
import fnmatch
import shutil


# BASE is the folder containing this script. The organizer only reads files
# directly inside DOWNLOADS and moves them into category subfolders there.
BASE = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS = os.path.join(BASE, "Messy_Downloads")

# The first matching category rule wins. Names are lower-cased before matching.
RULES = [
    ("School_Work", ["assessment_task_*", "activity_*", "module_[0-9]*"]),
    ("Screenshots", ["screenshot_*.png", "screenshot *.png"]),
    ("Images",      ["*.jpg", "*.jpeg", "*.png", "*.gif"]),
    ("Documents",   ["*.pdf", "*.docx", "*.txt", "*.pptx"]),
    ("Videos",      ["*.mp4", "*.mkv"]),
    ("Music",       ["*.mp3", "*.wav"]),
    ("Code",        ["*.py", "*.js", "*.html"]),
    ("Archives",    ["*.zip", "*.rar"]),
]
JUNK_PATTERNS = ["*.tmp", "*.crdownload", "~$*"]


def matches_any(filename, patterns):
    """Return True if a lower-case filename matches one of the patterns."""
    return any(fnmatch.fnmatchcase(filename.lower(), pattern) for pattern in patterns)


def find_category(filename):
    """Choose the first matching category, or Others if none matches."""
    for folder_name, patterns in RULES:
        if matches_any(filename, patterns):
            return folder_name
    return "Others"


def is_junk(filename):
    return matches_any(filename, JUNK_PATTERNS)


def safe_destination(folder, filename):
    """Choose an unused destination name so an existing file is not overwritten."""
    destination = os.path.join(folder, filename)
    if not os.path.exists(destination):
        return destination

    name, extension = os.path.splitext(filename)
    counter = 1
    while True:
        new_name = f"{name} ({counter}){extension}"
        destination = os.path.join(folder, new_name)
        if not os.path.exists(destination):
            return destination
        counter += 1


def organize_folder(dry_run):
    """Plan or perform actions on files directly inside DOWNLOADS."""
    moved = 0
    deleted = 0

    for filename in sorted(os.listdir(DOWNLOADS)):
        source = os.path.join(DOWNLOADS, filename)
        if not os.path.isfile(source):
            continue  # Leave category folders and other directories alone.

        if is_junk(filename):
            print(f"  DELETE  {filename}")
            if not dry_run:
                os.remove(source)
            deleted += 1
            continue

        category = find_category(filename)
        target_folder = os.path.join(DOWNLOADS, category)
        destination = safe_destination(target_folder, filename)
        print(f"  MOVE    {filename:<28} -> {category}/{os.path.basename(destination)}")
        if not dry_run:
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(source, destination)
        moved += 1

    return moved, deleted


def main():
    # Create an empty input folder if needed. Existing contents are preserved.
    os.makedirs(DOWNLOADS, exist_ok=True)
    print("=== SMART DOWNLOADS ORGANIZER ===")
    print(f"Organizing files directly inside: {DOWNLOADS}\n")

    files = [
        name for name in os.listdir(DOWNLOADS)
        if os.path.isfile(os.path.join(DOWNLOADS, name))
    ]
    if not files:
        print("No files to organize. Put files in this folder and run again.")
        return

    print("PLAN:")
    planned_moved, planned_deleted = organize_folder(dry_run=True)
    print(f"\nPlanned moves: {planned_moved} | Planned deletions: {planned_deleted}")

    answer = input("Apply this plan? (y/n): ").strip().lower()
    if answer != "y":
        print("Cancelled. No files were changed.")
        return

    print("\nWORKING:")
    moved, deleted = organize_folder(dry_run=False)
    print(f"\nFinished. Files moved: {moved} | Junk files deleted: {deleted}")


if __name__ == "__main__":
    main()
