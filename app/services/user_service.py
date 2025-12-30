from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_dto_input import UserCreateDTO
from app.core.security import hash_password, verify_password


def create_user(db: Session, dto: UserCreateDTO) -> User:
    user = User(
        username=dto.username,
        hashed_password=hash_password(dto.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(
    db: Session,
    username: str,
    password: str
) -> User | None:
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user
