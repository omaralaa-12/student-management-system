from typing import List

from pydantic import BaseModel, Field


# ----------------------------
# Create Course
# ----------------------------
class CourseCreate(BaseModel):
    course_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Course name"
    )

    course_code: str = Field(
        ...,
        min_length=2,
        max_length=20,
        description="Course code"
    )

    credits: int = Field(
        ...,
        gt=0,
        le=6,
        description="Course credit hours"
    )


# ----------------------------
# Simple Course (used in relationships)
# ----------------------------
class CourseSimple(BaseModel):
    id: int
    course_name: str
    course_code: str

    class Config:
        from_attributes = True


# ----------------------------
# Full Course
# ----------------------------
class Course(CourseCreate):
    id: int

    class Config:
        from_attributes = True


# ----------------------------
# Course with Students
# (We'll use this later)
# ----------------------------
class CourseWithStudents(Course):
    students: List["StudentSimple"] = []

    class Config:
        from_attributes = True


# Fix forward references
from app.schemas.student import StudentSimple

CourseWithStudents.model_rebuild()