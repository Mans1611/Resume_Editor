import PyPDF2
import docx
from IPython.core.display import HTML


def extract_text_from_word(docx_path):
    doc = docx.Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text


def write_html_file(resume_html: HTML, filepath: str = "new_resume.html"):
    with open(filepath, "w") as f:
        f.write(resume_html.data)
    
    return filepath