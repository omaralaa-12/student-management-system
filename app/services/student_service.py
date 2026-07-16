from sqlalchemy.orm import Session

from app.database.models import Student as StudentModel
from app.database.models import Course
from app.schemas.student import StudentCreate


# Create Student
def create_student(db: Session, student: StudentCreate):
    new_student = StudentModel(
        name=student.name,
        age=student.age,
        major=student.major
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# Get All Students
def get_students(db: Session):
    return db.query(StudentModel).all()


# Get Student By ID
def get_student(db: Session, student_id: int):
    return db.query(StudentModel).filter(
        StudentModel.id == student_id
    ).first()


# Update Student
def update_student(
    db: Session,
    student_id: int,
    updated_student: StudentCreate
):
    student = get_student(db, student_id)

    if student is None:
        return None

    student.name = updated_student.name
    student.age = updated_student.age
    student.major = updated_student.major

    db.commit()
    db.refresh(student)

    return student


# Delete Student
def delete_student(db: Session, student_id: int):
    student = get_student(db, student_id)

    if student is None:
        return False

    db.delete(student)
    db.commit()

    return True


# Enroll Student in Course
def enroll_student_in_course(
    db: Session,
    student_id: int,
    course_id: int
):
    student = get_student(db, student_id)

    if student is None:
        return None

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if course is None:
        return None

    # Avoid duplicate enrollments
    if course not in student.courses:
        student.courses.append(course)

    db.commit()
    db.refresh(student)

    return student


# Get Courses for a Student
def get_student_courses(
    db: Session,
    student_id: int
):
    student = get_student(db, student_id)

    if student is None:
        return None

    return student.courses