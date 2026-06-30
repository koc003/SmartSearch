from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

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