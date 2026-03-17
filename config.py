# folder where new files will appear
WATCHED_DIRECTORY = "watched_folder"

# folder where files will be organized
OUTPUT_DIRECTORY = "organized"

# log file path
LOG_FILE = "logs/system.log"


# NEW: function to update watched directory dynamically
def set_watched_directory(path):
    global WATCHED_DIRECTORY
    WATCHED_DIRECTORY = path