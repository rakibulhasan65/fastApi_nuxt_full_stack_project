from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import sessionLocal
from app.schemas import user as schemas
from app.db import userModel as models
from app.core import security as auth
import logging

logger = logging.getLogger("uvicorn.error")

router = APIRouter()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register",response_model=schemas.UserShow)
def user_register(user:schemas.UserCreate, db:Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    hashed_password = auth.hash_password(user.password)
    new_user = models.User(username=user.username,email=user.email,password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# login route
@router.post("/login", response_model=schemas.Token)
def user_login(user:schemas.userLogin, db:Session = Depends(get_db)):
    logger.info(user)
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not auth.verify_password(user.password,db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")
    token_data = auth.create_access_token({"sub": db_user.email})
    return {"access_token": token_data, "token_type": "bearer"}