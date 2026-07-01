# 🔍 SmartSearch

SmartSearch is an AI-powered PDF Question Answering application that enables users to upload PDF documents and ask natural language questions about their content. The application uses Retrieval-Augmented Generation (RAG) with Google Gemini embeddings, FAISS vector search, and Gemini 2.5 Flash to generate accurate, context-aware answers.

---

## ✨ Features

- 📄 Upload PDF documents
- 🔍 Ask natural language questions
- 🤖 AI-generated answers using Gemini 2.5 Flash
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ Fast semantic search using FAISS
- 📝 Markdown-formatted AI responses
- 📋 One-click answer copy
- 📚 Expandable retrieved source cards
- 🔄 Loading spinner during inference
- 🎨 Modern React frontend

---

## 🏗️ Tech Stack

### Backend

- Flask
- Google GenAI SDK
- Gemini 2.5 Flash
- Gemini Embedding 001
- FAISS
- PyPDF
- Pickle

### Frontend

- React
- Vite
- Axios
- React Markdown
- CSS

---

## 📂 Project Structure

```
smartsearch/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   │
│   ├── services/
│   │   ├── pdf_processing.py
│   │   ├── embedding.py
│   │   ├── vectorstore.py
│   │   └── rag.py
│   │
│   ├── uploads/
│   └── data/
│       ├── faiss.index
│       └── chunks.pkl
│
└── frontend/
    ├── src/
    │   ├── components/
    │   ├── services/
    │   └── styles/
    │
    └── public/
```

---

## ⚙️ How It Works

1. User uploads a PDF.
2. Text is extracted using PyPDF.
3. The extracted text is cleaned and split into overlapping chunks.
4. Gemini Embedding 001 converts every chunk into vector embeddings.
5. FAISS indexes all embeddings.
6. User submits a question.
7. The question is embedded using the same embedding model.
8. FAISS retrieves the most relevant chunks.
9. Gemini 2.5 Flash receives the retrieved context and generates the final answer.
10. The frontend displays the answer along with the retrieved source passages.

---

## 🧠 RAG Pipeline

```
PDF
 │
 ▼
Text Extraction
 │
 ▼
Text Cleaning
 │
 ▼
Chunking
 │
 ▼
Gemini Embeddings
 │
 ▼
FAISS Index
 │
 ▼
User Question
 │
 ▼
Question Embedding
 │
 ▼
Top-K Retrieval
 │
 ▼
Prompt Engineering
 │
 ▼
Gemini 2.5 Flash
 │
 ▼
Final Answer
```

---

## 🚀 Getting Started

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

## 📸 Screenshots

### Home Page

> <img width="1918" height="933" alt="Screenshot 2026-07-01 121744" src="https://github.com/user-attachments/assets/d0b0551f-4b3b-46e9-8a25-691ac2d8cccb" />


---

### Upload PDF

> <img width="1906" height="935" alt="Screenshot 2026-07-01 121814" src="https://github.com/user-attachments/assets/93914108-048b-48a5-b8dd-432f3c26c856" />


---

### AI Answer

> <img width="1116" height="833" alt="Screenshot 2026-07-01 121908" src="https://github.com/user-attachments/assets/1e379b2b-a34d-4bcf-999a-f27d9de836cc" />


---

### Retrieved Sources

> <img width="1151" height="623" alt="Screenshot 2026-07-01 121921" src="https://github.com/user-attachments/assets/e9d08c4f-698e-42a0-98d9-ed88d9890fef" />


---

## 🎯 Current Features

- Single PDF indexing
- Semantic retrieval
- Gemini-powered question answering
- Modern React interface
- Markdown rendering
- Copy answer
- Loading spinner
- Expandable retrieved sources
- Toast notifications

---

## 🔮 Planned Improvements

- Multi-PDF support
- Conversation memory
- Streaming AI responses
- Authentication
- Docker support
- Cloud deployment
- Improved retrieval strategies
- Hybrid search
- Response citations
- Search history

---

## 📖 Learning Outcomes

This project was built to explore production-oriented AI application development and covers:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Prompt Engineering
- REST APIs
- React Component Architecture
- Flask Backend Development
- AI System Design

---

## 👨‍💻 Author

**M P Sabarish**

CSE'28 Undergraduate  
Indian Institute of Technology (IIT) Mandi

---

## 📄 License

This project is intended for educational and portfolio purposes.
