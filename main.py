from chromadb_dataloader import data_loader
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import chromadb
import re

file_path = "/Users/ugurekinci/Documents/Naive_RAG_Pipeline/Naive-RAG-Pipeline/microsoft-annual-report.pdf"
c = [word for word in file_path.split("/") if re.search(".pdf", word)]
collection_name = c[0].replace(".pdf", "")


# collection = data_loader(file_path)
if __name__ == '__main__':
    query_text = [input("Your Query: ")]
    embedded_func = SentenceTransformerEmbeddingFunction()
    embedded_query = embedded_func(query_text)
    vector_database = data_loader(file_path, collection_name)
    vector_database.query(
        query_embeddings=embedded_query
    )
    
    
