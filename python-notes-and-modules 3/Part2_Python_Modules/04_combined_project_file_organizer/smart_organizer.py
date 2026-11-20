"""
SMART DOWNLOADS ORGANIZER (os + fnmatch + shutil)

Put files in Messy_Downloads next to this script and run the program. It plans
to sort every file directly inside that folder, then asks before applying the
plan. Temporary files are moved into Deleted_Backup so they can be restored.
"""
import os
import fnmatch
import shutil


# BASE is the folder containing this script. The organizer only reads files
# directly inside DOWNLOADS and moves them into category subfolders there.
BASE = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS = os.path.join(BASE, "Messy_Downloads")
RECOVERY_BACKUP = os.path.join(BASE, "Deleted_Backup")

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
    backed_up = 0

    for filename in sorted(os.listdir(DOWNLOADS)):
        source = os.path.join(DOWNLOADS, filename)
        if not os.path.isfile(source):
            continue  # Leave category folders and other directories alone.

        if is_junk(filename):
            backup_destination = safe_destination(RECOVERY_BACKUP, filename)
            print(
                f"  BACKUP  {filename:<28} -> "
                f"Deleted_Backup/{os.path.basename(backup_destination)}"
            )
            if not dry_run:
                os.makedirs(RECOVERY_BACKUP, exist_ok=True)
                shutil.move(source, backup_destination)
            backed_up += 1
            continue

        category = find_category(filename)
        target_folder = os.path.join(DOWNLOADS, category)
        destination = safe_destination(target_folder, filename)
        print(f"  MOVE    {filename:<28} -> {category}/{os.path.basename(destination)}")
        if not dry_run:
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(source, destination)
        moved += 1

    return moved, backed_up


def organize_downloads():
    """Preview and organize the files directly inside DOWNLOADS."""
    files = [
        name for name in os.listdir(DOWNLOADS)
        if os.path.isfile(os.path.join(DOWNLOADS, name))
    ]
    if not files:
        print("No files to organize. Put files in this folder and run again.")
        return

    print("PLAN:")
    planned_moved, planned_backed_up = organize_folder(dry_run=True)
    print(f"\nPlanned moves: {planned_moved} | Files to back up: {planned_backed_up}")

    answer = input("Apply this plan? (y/n): ").strip().lower()
    if answer != "y":
        print("Cancelled. No files were changed.")
        return

    print("\nWORKING:")
    moved, backed_up = organize_folder(dry_run=False)
    print(f"\nFinished. Files moved: {moved} | Files backed up: {backed_up}")


def restore_from_backup():
    """Let the user choose one backed-up file to restore to DOWNLOADS."""
    if not os.path.isdir(RECOVERY_BACKUP):
        print("There are no backed-up files yet.")
        return

    backup_files = sorted(
        name for name in os.listdir(RECOVERY_BACKUP)
        if os.path.isfile(os.path.join(RECOVERY_BACKUP, name))
    )
    if not backup_files:
        print("There are no backed-up files yet.")
        return

    print("Backed-up files:")
    for number, filename in enumerate(backup_files, start=1):
        print(f"  {number}. {filename}")

    choice = input("Enter a number to restore, or q to cancel: ").strip().lower()
    if choice == "q":
        print("Restore cancelled.")
        return

    try:
        index = int(choice) - 1
    except ValueError:
        print("Please enter a listed number or q.")
        return

    if index < 0 or index >= len(backup_files):
        print("That number is not in the list.")
        return

    filename = backup_files[index]
    source = os.path.join(RECOVERY_BACKUP, filename)
    destination = safe_destination(DOWNLOADS, filename)
    shutil.move(source, destination)
    print(f"Restored to Messy_Downloads/{os.path.basename(destination)}")


def main():
    # Create an empty input folder if needed. Existing contents are preserved.
    os.makedirs(DOWNLOADS, exist_ok=True)
    print("=== SMART DOWNLOADS ORGANIZER ===")
    print(f"Input folder: {DOWNLOADS}")
    print(f"Recovery folder: {RECOVERY_BACKUP}\n")
    print("1. Organize files")
    print("2. Restore a backed-up file")

    choice = input("Choose an option (1 or 2): ").strip()
    if choice == "1":
        organize_downloads()
    elif choice == "2":
        restore_from_backup()
    else:
        print("Please choose 1 or 2.")


if __name__ == "__main__":
    main()
