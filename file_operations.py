import os
import shutil
import hashlib
from datetime import datetime
from config import LOG_FILE


def log_action(message):

    # make sure logs folder exists
    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()} - {message}\n")

    print(message)


def get_file_hash(file_path):

    hasher = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()


def move_file(source, destination_folder):

    # create destination folder if needed
    os.makedirs(destination_folder, exist_ok=True)

    filename = os.path.basename(source)
    destination = os.path.join(destination_folder, filename)

    # check if same filename exists
    if os.path.exists(destination):

        source_hash = get_file_hash(source)
        destination_hash = get_file_hash(destination)

        if source_hash == destination_hash:

            # create duplicates folder
            duplicate_folder = os.path.join("organized", "duplicates")
            os.makedirs(duplicate_folder, exist_ok=True)

            duplicate_path = os.path.join(duplicate_folder, filename)

            shutil.move(source, duplicate_path)

            log_action(f"Duplicate detected: {filename} moved to duplicates folder")

            return

    # move normally
    shutil.move(source, destination)

    log_action(f"{filename} moved to {destination_folder}")