# 🏥 Medical Assistance – AI-Powered Healthcare Chatbot

🔗 **Live Application:**  
https://medicalassistance-123.streamlit.app/

---

## 📌 Overview

Medical Assistance is a full-stack AI-powered healthcare chatbot that provides general medical information, medication guidance, and responses to common health-related queries.

The application is built using:

- **FastAPI** – Backend API service
- **Streamlit** – Interactive frontend interface
- **LangChain** – Prompt orchestration
- **LLM Integration** – AI-generated medical responses

This project demonstrates full-stack AI deployment with a cloud-hosted backend and frontend.

---

## 🏗️ Architecture
```
User (Browser)
    ↓
Streamlit Frontend (Public URL)
    ↓
FastAPI Backend (Render Cloud)
    ↓
LLM Service (via LangChain)
```


### Deployment Stack

- **Backend Hosted On:** Render  
- **Frontend Hosted On:** Streamlit Community Cloud  

---

## 📂 Project Structure
```
Medical_Assistance/
│
├── backend/
│ ├── backend.py
│ ├── llm_service.py
│ ├── memory_store.py
│ ├── requirements.txt
│ └── init.py
│
├── frontend/
│ ├── app.py
│ └── requirements.txt
│
├── .env
├── .gitignore
└── README.md
```


---

## ⚙️ Features

- 💊 Medication information
- 🩺 General health query support
- 🧠 AI-based conversational responses
- 💬 Chat-style interface
- ☁️ Fully deployed public application
- 🔐 Environment variable support for API keys
- 🌐 REST API backend with interactive Swagger docs

---

## 🖥️ Backend (FastAPI)

### Main Entry Point

`backend/backend.py`

The FastAPI app exposes endpoints such as:
GET /
POST /ask


Swagger Documentation (Backend API): https://medical-assistance-h1go.onrender.com/docs


---

## 🎨 Frontend (Streamlit)

### Main File

`frontend/app.py`

The frontend:

- Accepts user input
- Sends requests to the backend API
- Displays AI-generated responses

Backend URL configured in production:

```python
BACKEND_URL = "https://medical-assistance-h1go.onrender.com/ask"
```
🚀 Local Setup Guide
```
1️⃣ Clone the Repository
git clone https://github.com/kshivayadav/Medical_Assistance.git
cd Medical_Assistance

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Backend Dependencies
pip install -r backend/requirements.txt

4️⃣ Install Frontend Dependencies
pip install -r frontend/requirements.txt

5️⃣ Run Backend
uvicorn backend.backend:app --reload
Backend runs at:
http://127.0.0.1:8000

6️⃣ Run Frontend
streamlit run frontend/app.py
Frontend runs at: 
http://localhost:8501

🔐 Environment Variables

Create a .env file in the root directory:
GROQ_API_KEY=your_api_key_here
```

In production:

Add environment variables inside Render dashboard

Add secrets inside Streamlit Cloud settings


☁️ Deployment Details
Backend Deployment (Render)

Build Command:
```
pip install -r backend/requirements.txt
```

Start Command:
```
uvicorn backend.backend:app --host 0.0.0.0 --port 10000
```
Frontend Deployment (Streamlit Cloud)

Repository connected via GitHub

Main file path:
```
frontend/app.py
```

### 🛠️ Tech Stack

Python 3.x

FastAPI

Uvicorn

Streamlit

LangChain

OpenAI API (LLM Integration)

Render Cloud

Streamlit Community Cloud

### ⚠️ Disclaimer

This application provides AI-generated general medical information for educational purposes only.

It does not replace professional medical diagnosis or treatment.
Always consult a qualified healthcare provider for medical concerns.

### 📈 Future Improvements

User authentication

Conversation history persistence (database integration)

Role-based medical assistant modes

Improved prompt engineering

Rate limiting and security hardening

Docker containerization

CI/CD pipeline integration

### 👨‍💻 Author

K Shiva Kumar
AI / ML Engineer | Full-Stack AI Developer

### ⭐ If You Like This Project

Consider starring the repository to support development.
