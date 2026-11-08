from sqlmodel import Session

from api_services.features.users.models import CreateUser, User, UserEmail


def create_user(db: Session, payload: CreateUser):
    user = User(is_verified=False)
    db.add(user)
    user_email = UserEmail(user_id=user.id, email=payload.email)
    db.add(user_email)
    return user
