from pypdf import PdfReader
import re
from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

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

def clean_text(text):
    
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
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

