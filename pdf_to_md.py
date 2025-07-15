import subprocess
import pymupdf4llm
from pathlib import Path
import pathlib
import re

    
def create_markdown_file(file_path : str, output=False):
    c = [word for word in file_path.split("/") if re.search(".pdf", word)]
    file_name = c[0].replace(".pdf", ".md")
    markdown_text = pymupdf4llm.to_markdown(file_path)
    if not file_name.endswith('.md'):
        file_name += '.md'
    Path(file_name).write_text(markdown_text, encoding="utf-8")
    if output:
        subprocess.run(["open", file_name], check=True)
        return file_name
    return "f{file_name} was created"

def read_md(file_path):
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"Dosya bulunamadı: {file_name}")
    encodings = ['utf-8', 'latin-1', 'windows-1252']
    for encoding in encodings:
        try:
            return Path(file_path).read_text(encoding=encoding)
        except UnicodeDecodeError:
            print(f"{encoding} ile dekode edilemedi, bir sonraki encoding deneniyor...")
            
    return None

file_path_md = "/Users/ugurekinci/Documents/Naive_RAG_Pipeline/Naive-RAG-Pipeline/microsoft-annual-report.md"

# create_markdown_doc = create_markdown_file(file_path, output=True)

read_markdown_doc = read_md(file_path_md)
print(read_markdown_doc)