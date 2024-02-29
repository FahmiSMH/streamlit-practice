#this is for reading microsoft word or google docs format
from docx import Document

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

file_path = 'your_document.docx'
text = extract_text_from_docx(file_path)
print(text)
