from sqlalchemy.orm import Session


from app.schemas.course import CourseCreate
from app.database.models import Course

def create_course(db: Session, course: CourseCreate):

    new_course = Course(
        course_name=course.course_name,
        course_code=course.course_code,
        credits=course.credits
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course


def get_courses(db: Session):

    return db.query(Course).all()