import axios from "axios";

// Flask backend base URL
const API = axios.create({
    baseURL: "http://127.0.0.1:5000",
});

// Upload a PDF
export async function uploadPDF(file) {
    const formData = new FormData();
    formData.append("file", file);

    const response = await API.post("/upload", formData, {
        headers: {
            "Content-Type": "multipart/form-data",
        },
    });

    return response.data;
}

// Search a question
export async function searchQuestion(query) {
    const response = await API.post("/search", {
        query: query,
    });

    return response.data;
}