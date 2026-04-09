import os
import time

def clean_old_files(folder_path, days_threshold):
    # Convert days to seconds
    seconds = days_threshold * 24 * 60 * 60
    current_time = time.time()

    print(f"Cleaning files in {folder_path} older than {days_threshold} days...")
    
    for root, dirs, files in os.walk(folder_path):
        for name in files:
            file_path = os.path.join(root, name)
            file_age = os.stat(file_path).st_mtime
            
            if (current_time - file_age) > seconds:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {name}")
                except Exception as e:
                    print(f"Error deleting {name}: {e}")

# clean_old_files('./temp_logs', 7)