from pydantic import BaseModel

from app.schemas.student import StudentSimple
from app.schemas.course import CourseSimple


# ----------------------------
# Create Enrollment
# ----------------------------
class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int


# ----------------------------
# Enrollment Response
# ----------------------------
class Enrollment(BaseModel):
    id: int
    student: StudentSimple
    course: CourseSimple

    class Config:
        from_attributes = True