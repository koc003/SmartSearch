import { useState } from "react";
import { uploadPDF } from "../services/api";

import "../styles/UploadSection.css";

function UploadSection({
    onUploadSuccess,
    showToast,
}) {
    const [selectedFile, setSelectedFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState("");

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
        setMessage("");
    };

    const handleUpload = async () => {
        if (!selectedFile) {
            setMessage("Please select a PDF file.");
            return;
        }

        try {
            setLoading(true);

            const response = await uploadPDF(selectedFile);

            setMessage(response.message);

            showToast("PDF uploaded.");

            onUploadSuccess();

        } catch (error) {

            if (error.response?.data?.error) {
                setMessage(error.response.data.error);
                showToast(error.response.data.error, "error");
            } else {
                setMessage("Failed to upload file.");
                showToast("Upload failed.", "error");
            }

        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="upload-card">

            <h2>Upload PDF</h2>

            <input
                id="pdf-upload"
                className="file-input"
                type="file"
                accept=".pdf"
                onChange={handleFileChange}
            />

            <label
                htmlFor="pdf-upload"
                className="file-label"
            >
                📄 Choose PDF
            </label>

            {selectedFile && (
                <p className="file-name">
                    Selected File:
                    <strong> {selectedFile.name}</strong>
                </p>
            )}

            <div className="upload-actions">

                <button
                    className="upload-btn"
                    onClick={handleUpload}
                    disabled={loading}
                >
                    {loading ? "Uploading..." : "Upload"}
                </button>

            </div>

            {message && (
                <p className="upload-message">
                    {message}
                </p>
            )}

        </div>
    );
}

export default UploadSection;