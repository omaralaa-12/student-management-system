from sqlalchemy.orm import Session

from app.core.logger import logger
from app.database.models import Student as StudentModel
from app.schemas.student import StudentCreate


# Create Student
def create_student(
    db: Session,
    student: StudentCreate
):
    new_student = StudentModel(
        name=student.name,
        age=student.age,
        major=student.major
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    logger.info(f"Student created: {new_student.name}")

    return new_student


# Get All Students (Search + Pagination)
def get_students(
    db: Session,
    name: str = None,
    major: str = None,
    skip: int = 0,
    limit: int = 10
):
    query = db.query(StudentModel)

    if name:
        query = query.filter(
            StudentModel.name.ilike(f"%{name}%")
        )

    if major:
        query = query.filter(
            StudentModel.major.ilike(f"%{major}%")
        )

    students = query.offset(skip).limit(limit).all()

    logger.info(f"Retrieved {len(students)} students")

    return students


# Get Student By ID
def get_student(
    db: Session,
    student_id: int
):
    student = db.query(StudentModel).filter(
        StudentModel.id == student_id
    ).first()

    if student:
        logger.info(f"Retrieved student ID {student_id}")
    else:
        logger.warning(f"Student ID {student_id} not found")

    return student


# Update Student
def update_student(
    db: Session,
    student_id: int,
    updated_student: StudentCreate
):
    student = get_student(db, student_id)

    if student is None:
        logger.warning(f"Update failed. Student ID {student_id} not found")
        return None

    student.name = updated_student.name
    student.age = updated_student.age
    student.major = updated_student.major

    db.commit()
    db.refresh(student)

    logger.info(f"Student updated: {student.name}")

    return student


# Delete Student
def delete_student(
    db: Session,
    student_id: int
):
    student = get_student(db, student_id)

    if student is None:
        logger.warning(f"Delete failed. Student ID {student_id} not found")
        return False

    logger.info(f"Student deleted: {student.name}")

    db.delete(student)
    db.commit()

    return True