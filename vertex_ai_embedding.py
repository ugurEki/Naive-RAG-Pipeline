from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
import vertexai
from vertexai.language_models import TextEmbeddingModel


def init_vertex_ai():
    """
    Initializes Vertex AI with credentials and project settings.
    """
    api_key_path = "/Users/ugurekinci/Downloads/vertex-ai-465718-b7ad113c10f1.json"
    credentials = Credentials.from_service_account_file(
        api_key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
    PROJECT_ID = "vertex-ai-465718"
    REGION="us-central1"
    vertexai.init(
    project = PROJECT_ID,
    location = REGION,
    credentials = credentials
)

def vertex_ai_embedding(model: str, text: list[str]):
    """
    Generates text embedding vectors using Vertex AI.
    
    Args:
        model (str): The embedding model to use("text-embedding-005", "text-multilingual-embedding-002")
        texts (list[str]): List of text to generate embedding vectors for.
        
    Returns:
        list: A list of embedding vectors for each text.
    """
    init_vertex_ai()
    
    embedding_model = TextEmbeddingModel.from_pretrained(model)
    
    emd_text = embedding_model.get_embeddings(text)
    
    return emd_text[0].values



