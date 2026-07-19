# 🎓 Student Management System

A full-stack Student Management System built with **FastAPI** and **React**, featuring secure JWT authentication, CRUD operations, course and enrollment management, and AI-powered assistance using Google Gemini.

---

## 🚀 Features

- 🔐 JWT Authentication
- 👨‍🎓 Student CRUD Operations
- 📚 Course Management
- 📝 Enrollment Management
- 🔍 Search Students
- 🤖 AI Assistant powered by Google Gemini
- 📖 Interactive Swagger Documentation
- 🎨 Responsive React Frontend

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Pydantic
- Google Gemini API

### Frontend
- React
- Vite
- Axios
- Tailwind CSS

---

## 📂 Project Structure

```text
student-management-system/
│
├── app/
│   ├── ai/
│   ├── core/
│   ├── database/
│   ├── routers/
│   ├── schemas/
│   └── services/
│
├── frontend/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Backend

```bash
git clone <repository-url>

cd student-management-system

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 📚 API Documentation

After running the backend:

```
http://127.0.0.1:8000/docs
```

---

## 🤖 AI Integration

The application integrates **Google Gemini AI** to provide an AI-powered assistant through the frontend.

---

## 👨‍💻 Author

**Omar Alaa**

Computer Engineering Graduate — The British University in Egypt (BUE)

Interested in:
- Artificial Intelligence
- Machine Learning
- Backend Development
- Full Stack Development