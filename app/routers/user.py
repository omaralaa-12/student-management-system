from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.auth import create_access_token
from app.database.database import get_db
from app.schemas.user import UserCreate, User
from app.services.user_service import (
    create_user,
    get_user_by_username,
    authenticate_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# Register User
@router.post("/", response_model=User)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = get_user_by_username(
        user.username,
        db
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    return create_user(user, db)


# Login User
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    authenticated_user = authenticate_user(
        form_data.username,
        form_data.password,
        db
    )

    if not authenticated_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={
            "sub": authenticated_user.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }