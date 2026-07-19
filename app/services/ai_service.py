from sqlalchemy.orm import Session

from app.database.models import Student
from app.ai.gemini import ask_gemini


def ask_database(db: Session, question: str):

    students = db.query(Student).all()

    data = []

    for student in students:
        data.append(
            {
                "name": student.name,
                "age": student.age,
                "major": student.major,
            }
        )

    prompt = f"""
You are an AI assistant for a Student Management System.

Student Database:

{data}

Answer this question using ONLY the database above.

Question:
{question}
"""

    return ask_gemini(prompt)