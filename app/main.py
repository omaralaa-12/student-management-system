from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import engine
from app.database import models

from app.routers.ai import router as ai_router
from app.routers.user import router as user_router
from app.routers.student import router as student_router
from app.routers.course import router as course_router
from app.routers.enrollment import router as enrollment_router


app = FastAPI(
    title="Student Management API",
    description="A FastAPI backend for managing students, courses, users, enrollments, and AI.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(user_router)
app.include_router(student_router)
app.include_router(course_router)
app.include_router(enrollment_router)
app.include_router(ai_router)


@app.get("/")
def home():
    return {
        "message": "Student Management API is running 🚀",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    return {
        "status": "OK",
    }