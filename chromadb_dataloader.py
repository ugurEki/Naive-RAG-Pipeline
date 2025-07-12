from pypdf import PdfReader
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import chromadb
import pandas as pd

file_path = "/Users/ugurekinci/Documents/Naive_RAG_Pipeline/Naive-RAG-Pipeline/microsoft-annual-report.pdf"
embedding_model = SentenceTransformerEmbeddingFunction()

def extract_text_from_pdf(file_path):
    text = []
    with open(file_path, "rb") as f:
        pdf = PdfReader(f)
        for page_num in range(pdf.get_num_pages()):
            page = pdf.get_page(page_num)
            text.append(page.extract_text())
    return "/n".join(text)


def embedding_data(text):
    chunks = text.split("/n/n")
    embedding_function = SentenceTransformerEmbeddingFunction()
    embeddings = [embedding_function(chunk) for chunk in chunks]
    return embeddings

def chromadb_setup(collection_name):
    chroma_client = chromadb.Client()
    chroma_collection = chroma_client.create_collection(name = collection_name, embedding_function = embedding_model)
    return chroma_collection

def create_df(text, embeddings):
    df_dictionary = {"text": text, "embeddings": embeddings}
    df = pd.DataFrame(df_dictionary)
    return df

def data_loader(pdf_file, chroma_collection):
    text = extract_text_from_pdf(file_name)
    embeddings = embedding_data(text)
    df = create_df(text, embeddings)
    collection = chromadb_setup(chroma_collection)
    for index, row in df.iterrows():
        collection.add(ids = index, documents=row["text"], embeddings=row["embeddings"])
    return collection