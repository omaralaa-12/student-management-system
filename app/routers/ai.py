from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.ai import AIRequest, AIResponse
from app.services.ai_service import ask_database

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


@router.post(
    "/chat",
    response_model=AIResponse,
)
def chat(
    request: AIRequest,
    db: Session = Depends(get_db),
):

    answer = ask_database(
        db,
        request.question,
    )

    return {
        "answer": answer
    }