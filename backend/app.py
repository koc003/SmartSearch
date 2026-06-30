from flask import Flask, jsonify
from flask_cors import CORS
import os

from config import (
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


if __name__ == "__main__":
    app.run(debug=True)