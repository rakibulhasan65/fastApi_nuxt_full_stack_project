from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db import orders as models
from app.schemas import orders as schemas
from app.db.database import sessionLocal
router = APIRouter()
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
# Create order endpoint
@router.post("/orders", response_model=schemas.OrderOut, status_code=status.HTTP_201_CREATED, tags=["Order"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = models.Order(
        user_id=order.user_id,
        product_id=order.product_id,
        quantity=order.quantity,
        status=order.status
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order