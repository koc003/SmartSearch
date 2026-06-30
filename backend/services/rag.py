from services.vectorstore import retrieve_chunks
from google import genai
from config import GEMINI_API_KEY
client = genai.Client(api_key=GEMINI_API_KEY)


def build_prompt(query, retrieved_chunks):

    context = ""

    for i, item in enumerate(retrieved_chunks, start=1):

        context += f"Source {i}:\n"
        context += item["chunk"]
        context += "\n\n"

    prompt = f"""
You are SmartSearch, an AI assistant that answers questions based ONLY on the uploaded document.

Instructions:
- Answer ONLY using the provided context.
- Do NOT use outside knowledge.
- If the answer is not present in the context, reply exactly:
  "I couldn't find the answer in the uploaded document."
- Keep the answer concise but complete.
- Prefer bullet points when listing information.
- If the answer is descriptive, write it in a short paragraph.
- Do not mention "context", "sources", or "uploaded document" in the answer unless the user explicitly asks.
- Do not copy long sentences verbatim. Summarize naturally while preserving the meaning.

Context:
{context}

Question:
{query}

Answer:
"""

    return prompt

def generate_answer(query):

    retrieved_chunks = retrieve_chunks(query)

    prompt = build_prompt(
        query,
        retrieved_chunks
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "answer": response.text,
        "sources": retrieved_chunks
    }