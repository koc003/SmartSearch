from pypdf import PdfReader
from google import genai
from config import GEMINI_API_KEY, TOP_K

import faiss
import pickle
import numpy as np

from config import (
    FAISS_INDEX_PATH,
    CHUNKS_PATH
)

client = genai.Client(api_key=GEMINI_API_KEY)

def extract_text_from_pdf(filepath):
    # Parameters -> filepath (str): Path to the uploaded PDF.

    # Returns -> str: Complete extracted text.
    reader = PdfReader(filepath)

    pages = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            pages.append(page_text)

    return "\n".join(pages)



import re


def clean_text(text):
    
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def chunk_text(text, chunk_size=400, overlap=50):
    # Split text into overlapping word chunks.

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def get_embeddings(chunks, batch_size=20):

    embeddings = []

    for i in range(0, len(chunks), batch_size):

        batch = chunks[i:i + batch_size]

        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=batch
        )

        for embedding in response.embeddings:
            embeddings.append(embedding.values)

    return embeddings

def build_faiss_index(embeddings, chunks):

    embeddings = np.array(
        embeddings,
        dtype=np.float32
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(
        index,
        FAISS_INDEX_PATH
    )

    with open(CHUNKS_PATH, "wb") as file:
        pickle.dump(
            chunks,
            file
        )
    return index

def retrieve_chunks(query):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=query
    )

    query_embedding = np.array(
        [response.embeddings[0].values],
        dtype=np.float32
    )

    index = faiss.read_index(
        FAISS_INDEX_PATH
    )

    with open(CHUNKS_PATH, "rb") as file:
        chunks = pickle.load(file)

    distances, indices = index.search(
        query_embedding,
        TOP_K
    )

    retrieved_chunks = []

    for distance, idx in zip(distances[0], indices[0]):
        
        if idx == -1:
            continue
        
        retrieved_chunks.append({
            "chunk": chunks[idx],
            "distance": float(distance)
        })

    return retrieved_chunks