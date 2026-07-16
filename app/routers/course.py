from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.course import Course, CourseCreate
from app.services import course_service

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.post(
    "/",
    response_model=Course,
    status_code=status.HTTP_201_CREATED
)
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    return course_service.create_course(db, course)


@router.get(
    "/",
    response_model=List[Course]
)
def get_courses(
    db: Session = Depends(get_db)
):
    return course_service.get_courses(db)