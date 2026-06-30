from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import uuid
import os

from rag import (
    extract_text_from_pdf,
    clean_text,
    chunk_text,
    get_embeddings,
    build_faiss_index,
    retrieve_chunks
)

from config import (
    ALLOWED_EXTENSIONS,
    GEMINI_API_KEY,
    UPLOAD_FOLDER,
    DATA_FOLDER,
)

app = Flask(__name__)
CORS(app)

# Create required folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DATA_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return jsonify({
        "message": "SmartSearch Backend Running...",
        "status": "success"
    })


@app.route("/health")
def health():
    return jsonify({
        "backend": "running",
        "gemini_api_configured": bool(GEMINI_API_KEY),
        "upload_folder": UPLOAD_FOLDER,
        "data_folder": DATA_FOLDER
    })


def allowed_file(filename):
    
    # Check whether the uploaded file has an allowed extension.

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

@app.route("/upload", methods=["POST"])
def upload_file():

    # Check if a file exists in the request
    if "file" not in request.files:
        return jsonify({
            "error": "No file provided."
        }), 400

    file = request.files["file"]

    # Check for empty filename
    if file.filename == "":
        return jsonify({
            "error": "No file selected."
        }), 400

    # Validate extension
    if not allowed_file(file.filename):
        return jsonify({
            "error": "Only PDF files are allowed."
        }), 400

    # Secure filename
    extension = file.filename.rsplit(".", 1)[1].lower()
    filename = f"{uuid.uuid4().hex}.{extension}"

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(filepath)

    # Extract text from PDF
    text = extract_text_from_pdf(filepath)

# Clean the extracted text
    text = clean_text(text)

# Split into chunks
    chunks = chunk_text(text)

# Generate embeddings
    try:
        embeddings = get_embeddings(chunks)

        build_faiss_index(
        embeddings,
        chunks
        )

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

    return jsonify({
    "message": "File processed successfully.",
    "filename": filename,
    "chunks": len(chunks),
    "embeddings": len(embeddings),
    "embedding_dimension": len(embeddings[0]) if embeddings else 0 #,
    # "faiss_index" : index
    }), 200

@app.route("/search", methods=["POST"])
def search():

    data = request.get_json()

    if not data or "query" not in data:
        return jsonify({
            "error": "Query is required."
        }), 400

    query = data["query"]

    try:
        retrieved_chunks = retrieve_chunks(query)

        return jsonify({
            "query": query,
            "retrieved_chunks": retrieved_chunks
        }), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)