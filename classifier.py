def classify_file(filename):

    # get file extension
    extension = filename.split(".")[-1].lower()

    # image files
    if extension in ["jpg", "jpeg", "png", "gif"]:
        return "Images"

    # documents
    elif extension in ["pdf", "doc", "docx", "txt"]:
        return "Documents"

    # videos
    elif extension in ["mp4", "mkv", "avi"]:
        return "Videos"

    # compressed files
    elif extension in ["zip", "rar"]:
        return "Archives"

    # other files
    else:
        return "Others"