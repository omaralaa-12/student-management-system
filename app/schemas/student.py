from typing import List

from pydantic import BaseModel, Field


# ----------------------------
# Create Student
# ----------------------------
class StudentCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Student name"
    )

    age: int = Field(
        ...,
        gt=0,
        lt=100,
        description="Student age"
    )

    major: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Student major"
    )


# ----------------------------
# Simple Student (used in relationships)
# ----------------------------
class StudentSimple(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


# ----------------------------
# Full Student
# ----------------------------
class Student(StudentCreate):
    id: int

    class Config:
        from_attributes = True


# ----------------------------
# Student with Courses
# (We'll use this later)
# ----------------------------
class StudentWithCourses(Student):
    courses: List["CourseSimple"] = []

    class Config:
        from_attributes = True


# Fix forward references
from app.schemas.course import CourseSimple

StudentWithCourses.model_rebuild()