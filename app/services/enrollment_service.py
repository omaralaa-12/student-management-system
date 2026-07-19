from sqlalchemy.orm import Session

from app.database.models import (
    Enrollment,
    Student,
    Course,
)

from app.schemas.enrollment import EnrollmentCreate


def create_enrollment(
    db: Session,
    enrollment: EnrollmentCreate
):
    # Check if student exists
    student = db.query(Student).filter(
        Student.id == enrollment.student_id
    ).first()

    if not student:
        return None, "Student not found"

    # Check if course exists
    course = db.query(Course).filter(
        Course.id == enrollment.course_id
    ).first()

    if not course:
        return None, "Course not found"

    # Prevent duplicate enrollment
    existing = db.query(Enrollment).filter(
        Enrollment.student_id == enrollment.student_id,
        Enrollment.course_id == enrollment.course_id
    ).first()

    if existing:
        return None, "Student already enrolled in this course"

    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )

    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    return new_enrollment, None


def get_enrollments(db: Session):
    return db.query(Enrollment).all()


def get_student_courses(
    db: Session,
    student_id: int
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return None

    return student.enrollments


def get_course_students(
    db: Session,
    course_id: int
):
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        return None

    return course.enrollments