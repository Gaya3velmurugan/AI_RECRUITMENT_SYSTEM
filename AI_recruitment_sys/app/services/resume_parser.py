import fitz  # PyMuPDF
def extract_resume_text(pdf_path: str):
    text = ""
    document = fitz.open(pdf_path)

    for page in document:
        text += page.get_text()

    document.close()
    return text.strip()