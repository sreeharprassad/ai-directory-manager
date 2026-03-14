import os
import shutil
from datetime import datetime
from config import LOG_FILE


def log_action(message):

    # make sure logs folder exists
    os.makedirs("logs", exist_ok=True)

    # open log file
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()} - {message}\n")

    print(message)


def move_file(source, destination_folder):

    # create folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # get filename
    filename = os.path.basename(source)

    # destination path
    destination = os.path.join(destination_folder, filename)

    # move file
    shutil.move(source, destination)

    # log action
    log_action(f"{filename} moved to {destination_folder}")