import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Gemini Configuration

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Upload Configuration


UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}


# RAG Configuration

CHUNK_SIZE = 400
CHUNK_OVERLAP = 50
TOP_K = 3


# Storage


DATA_FOLDER = "data"

FAISS_INDEX_PATH = os.path.join(
    DATA_FOLDER,
    "faiss.index"
)

CHUNKS_PATH = os.path.join(
    DATA_FOLDER,
    "chunks.pkl"
)