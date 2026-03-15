import joblib
from text_extractor import extract_text_from_file

# load AI model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


def classify_document(text):

    # if text extraction fails
    if not text:
        return "Documents"

    # convert text into vector
    text_vector = vectorizer.transform([text])

    # predict category
    prediction = model.predict(text_vector)

    result = prediction[0]

    # safety fallback
    if result not in ["Resume", "Invoice", "Notes"]:
        return "Documents"

    return result


def classify_file(file_path):

    # get extension
    extension = file_path.split(".")[-1].lower()

    # image files
    if extension in ["jpg", "jpeg", "png", "gif"]:
        return "Images"

    # video files
    elif extension in ["mp4", "mkv", "avi"]:
        return "Videos"

    # compressed files
    elif extension in ["zip", "rar"]:
        return "Archives"

    # document files → AI classification
    elif extension in ["pdf", "docx", "doc", "txt", "ppt", "pptx"]:

        # extract text
        text = extract_text_from_file(file_path)

        # classify using AI
        return classify_document(text)

    # other files
    else:
        return "Others"