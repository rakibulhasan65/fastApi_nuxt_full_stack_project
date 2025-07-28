from app.db import userModel
from app.db.database import SessionLocal
from app.core.security import hash_password

def create_user(user_data):
    db = SessionLocal()
    user = userModel.User(
        username=user_data.username,
        hashed_password=hash_password(user_data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
