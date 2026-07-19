from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.database.database import get_db
from app.schemas.enrollment import Enrollment, EnrollmentCreate
from app.services import enrollment_service

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)


@router.post(
    "/",
    response_model=Enrollment,
    status_code=status.HTTP_201_CREATED
)
def create_enrollment(
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    new_enrollment, error = enrollment_service.create_enrollment(
        db,
        enrollment
    )

    if error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return new_enrollment


@router.get(
    "/",
    response_model=List[Enrollment]
)
def get_enrollments(
    db: Session = Depends(get_db)
):
    return enrollment_service.get_enrollments(db)


@router.get("/student/{student_id}")
def get_student_courses(
    student_id: int,
    db: Session = Depends(get_db)
):
    enrollments = enrollment_service.get_student_courses(
        db,
        student_id
    )

    if enrollments is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return enrollments


@router.get("/course/{course_id}")
def get_course_students(
    course_id: int,
    db: Session = Depends(get_db)
):
    enrollments = enrollment_service.get_course_students(
        db,
        course_id
    )

    if enrollments is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return enrollments