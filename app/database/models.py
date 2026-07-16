from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.database.database import Base


# Association Table (Many-to-Many)
student_course = Table(
    "student_course",
    Base.metadata,

    Column(
        "student_id",
        Integer,
        ForeignKey("students.id"),
        primary_key=True
    ),

    Column(
        "course_id",
        Integer,
        ForeignKey("courses.id"),
        primary_key=True
    )
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    major = Column(String, nullable=False)

    courses = relationship(
        "Course",
        secondary=student_course,
        back_populates="students"
    )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)

    course_name = Column(
        String,
        nullable=False
    )

    course_code = Column(
        String,
        unique=True,
        nullable=False
    )

    credits = Column(
        Integer,
        nullable=False
    )

    students = relationship(
        "Student",
        secondary=student_course,
        back_populates="courses"
    )