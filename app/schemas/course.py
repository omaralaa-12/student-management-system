from pydantic import BaseModel


class CourseCreate(BaseModel):
    course_name: str
    course_code: str
    credits: int


class Course(BaseModel):
    id: int
    course_name: str
    course_code: str
    credits: int

    class Config:
        from_attributes = True