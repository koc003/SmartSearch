import faiss
import pickle
import numpy as np
from config import (
    FAISS_INDEX_PATH,
    CHUNKS_PATH,
    TOP_K
)

from services.embedding import get_embeddings

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

    query_embedding = np.array(
        [get_embeddings([query])[0]],
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
            "distance": float(distance),
            "index": int(idx)
        })

    return retrieved_chunks
