from sqlalchemy.orm import Session

from app.database.models import User
from app.schemas.user import UserCreate
from app.core.security import hash_password
from app.core.security import verify_password

def create_user(user: UserCreate, db: Session):

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_by_username(username: str, db: Session):

    return db.query(User).filter(User.username == username).first()

def authenticate_user(username: str, password: str, db: Session):

    user = get_user_by_username(username, db)

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user