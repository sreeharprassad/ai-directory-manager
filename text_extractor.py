import docx
from pdfminer.high_level import extract_text

def extract_text_from_file(file_path):

    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        text = []
        for para in doc.paragraphs:
            text.append(para.text)
        return " ".join(text)

    elif file_path.endswith(".pdf"):
        return extract_text(file_path)

    return ""