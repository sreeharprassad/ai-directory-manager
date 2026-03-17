import os
import time

import config   
from classifier import classify_file
from file_operations import move_file
from file_operations import log_action

processed_files = set()

# control flag for GUI
running = False


def monitor_directory():

    log_action("----- New Session Started -----")
    
    global running

    print("Monitoring folder...")

    running = True

    processed_files.clear()

    while running:

        try:
            # use dynamic path
            files = os.listdir(config.WATCHED_DIRECTORY)

            for file in files:

                full_path = os.path.join(config.WATCHED_DIRECTORY, file)

                # process only new files
                if full_path not in processed_files:

                    # classify file
                    category = classify_file(full_path)

                    # destination folder
                    destination = os.path.join(config.OUTPUT_DIRECTORY, category)

                    # move file
                    move_file(full_path, destination)

                    processed_files.add(full_path)

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(3)


def stop_monitor():
    log_action("----- Session Ended -----")
    global running
    running = False
    print("Monitoring stopped.")


if __name__ == "__main__":
    monitor_directory()