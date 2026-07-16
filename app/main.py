from fastapi import FastAPI

from app.database.database import engine
from app.database import models

from app.routers.student import router as student_router
from app.routers.user import router as user_router
from app.routers.course import router as course_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(student_router)
app.include_router(user_router)
app.include_router(course_router)


@app.get("/")
def home():
    return {
        "message": "Student API is running 🚀"
    }