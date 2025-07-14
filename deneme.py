from pypdf import PdfReader
import os

def extract_text_from_pdf(file_path, text_name):
    raw_text = []
    with open(file_path, "rb") as f:
        pdf = PdfReader(f)
        for page_num in range(pdf.get_num_pages()):
            page = pdf.get_page(page_num)
            raw_text.append(page.extract_text())
    text = "/n".join(raw_text)
    
    with open(text_name, "w", encoding="utf-8") as f:
        f.write(text)
    

def read_if_text_exist(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            text = f.read()
            return text
    else:
        return "No such file exists."
    
file_path = "/Users/ugurekinci/Documents/Naive_RAG_Pipeline/Naive-RAG-Pipeline/microsoft-annual-report.pdf"
    
extract_text = extract_text_from_pdf(file_path, "microsoft_annual_report.txt")

read_text = read_if_text_exist("microsoft_annual_report.txt")