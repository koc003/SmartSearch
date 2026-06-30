from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import uuid
import os

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

    return jsonify({
        "message": "File uploaded successfully.",
        "filename": filename
    }), 200

if __name__ == "__main__":
    app.run(debug=True)