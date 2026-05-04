import shutil
import os
from datetime import datetime

def run_backup():
    source_dir = "source_folder"
    backup_base_dir = "backup_folder"

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    target_dir = os.path.join(backup_base_dir, f"backup_{timestamp}")

    try:
        if not os.path.exists(backup_base_dir):
            os.makedirs(backup_base_dir)
            print(f"Directory created: {backup_base_dir}")

        shutil.copytree(source_dir, target_dir)
        print(f"Success: Backup created at {target_dir}")

        with open("backup_log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"[{datetime.now()}] SUCCESS: {target_dir}\n")

    except FileNotFoundError:
        print("ERROR: Source directory not found! Please create 'source_dir'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        with open("backup_log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"[{datetime.now()}] FAILED: {str(e)}\n")

if __name__ == "__main__":
    run_backup()