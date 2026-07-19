from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.student import Student, StudentCreate
from app.services import student_service

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
    db: Session = Depends(get_db)
):
    return student_service.create_student(db, student)


# Get All Students (Search + Pagination)
@router.get(
    "/",
    response_model=List[Student]
)
def get_students(
    name: Optional[str] = None,
    major: Optional[str] = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return student_service.get_students(
        db=db,
        name=name,
        major=major,
        skip=skip,
        limit=limit
    )


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
    db: Session = Depends(get_db)
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
    db: Session = Depends(get_db)
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