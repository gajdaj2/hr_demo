import PyPDF2


def get_text_from_pdf(path: str) -> str:
    text = ""
    reader = PyPDF2.PdfReader(path)
    for x in range(len(reader.pages)):
        filePage = reader.pages[x]
        text += filePage.extract_text(0)
    return text