import os
import shutil

EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".ts", ".html", ".css", ".json", ".java", ".cpp"],
}

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    moved_count = 0

    for entry in os.listdir(folder_path):
        source_path = os.path.join(folder_path, entry)

        # Skip directories
        if os.path.isdir(source_path):
            continue

        _, ext = os.path.splitext(entry)
        ext = ext.lower()

        target_category = "Others"
        for category, extensions in EXTENSION_MAP.items():
            if ext in extensions:
                target_category = category
                break

        target_dir = os.path.join(folder_path, target_category)
        os.makedirs(target_dir, exist_ok=True)

        dest_path = os.path.join(target_dir, entry)
        if not os.path.exists(dest_path):
            shutil.move(source_path, dest_path)
            moved_count += 1
            print(f"Moved: {entry} -> {target_category}/")
        else:
            print(f"Skipped (already exists): {entry}")

    print(f"\nDone! Organized {moved_count} file(s).")

if __name__ == "__main__":
    target = input("Enter folder path to organize (or press Enter for current folder): ").strip()
    organize_folder(target if target else ".")
