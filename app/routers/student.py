from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.course import Course
from app.schemas.student import Student, StudentCreate
from app.services import student_service
from app.core.auth import get_current_user

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# Create Student
@router.post(
    "/",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return student_service.create_student(db, student)


# Get All Students
@router.get(
    "/",
    response_model=List[Student]
)
def get_students(
    db: Session = Depends(get_db)
):
    return student_service.get_students(db)


# Get Student By ID
@router.get(
    "/{student_id}",
    response_model=Student
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = student_service.get_student(
        db,
        student_id
    )

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student


# Update Student
@router.put(
    "/{student_id}",
    response_model=Student
)
def update_student(
    student_id: int,
    updated_student: StudentCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    student = student_service.update_student(
        db,
        student_id,
        updated_student
    )

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student


# Delete Student
@router.delete(
    "/{student_id}",
    status_code=status.HTTP_200_OK
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    deleted = student_service.delete_student(
        db,
        student_id
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully!"
    }


# Enroll Student in Course
@router.post(
    "/{student_id}/enroll/{course_id}"
)
def enroll_student(
    student_id: int,
    course_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    student = student_service.enroll_student_in_course(
        db,
        student_id,
        course_id
    )

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student or Course not found"
        )

    return {
        "message": "Student enrolled successfully!"
    }


# Get Courses for a Student
@router.get(
    "/{student_id}/courses",
    response_model=List[Course]
)
def get_student_courses(
    student_id: int,
    db: Session = Depends(get_db)
):
    courses = student_service.get_student_courses(
        db,
        student_id
    )

    if courses is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return courses