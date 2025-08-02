from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db import addToCart as models
from app.schemas import addToCart as schemas
from app.db.database import sessionLocal
router = APIRouter()
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create add to cart endpoint
@router.post("/add_to_cart", response_model=schemas.AddToCartOut, status_code=status.HTTP_201_CREATED, tags=["AddToCart"])
def create_add_to_cart(add_to_cart: schemas.AddToCartCreate, db: Session = Depends(get_db)):
    db_add_to_cart = models.AddToCart(
        user_id=add_to_cart.user_id,
        product_id=add_to_cart.product_id,
        quantity=add_to_cart.quantity
    )
    db.add(db_add_to_cart)
    db.commit()
    db.refresh(db_add_to_cart)
    return db_add_to_cart