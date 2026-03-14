import os
import time

from config import WATCHED_DIRECTORY, OUTPUT_DIRECTORY
from classifier import classify_file
from file_operations import move_file

processed_files = set()


def monitor_directory():

    print("Monitoring folder...")

    while True:

        # list files in watched folder
        files = os.listdir(WATCHED_DIRECTORY)

        for file in files:

            full_path = os.path.join(WATCHED_DIRECTORY, file)

            # process only new files
            if full_path not in processed_files:

                # classify file
                category = classify_file(file)

                # destination folder
                destination = os.path.join(OUTPUT_DIRECTORY, category)

                # move file
                move_file(full_path, destination)

                processed_files.add(full_path)

        # wait 5 seconds
        time.sleep(5)


if __name__ == "__main__":
    monitor_directory()