from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List,Optional
from app.db import product as models
from app.schemas import product as schemas
from app.db.database import sessionLocal

router = APIRouter()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
# Create category endpoint
@router.post("/category", response_model=schemas.CategoryOut , status_code=status.HTTP_201_CREATED,tags=["Category"])
def create_category(category:schemas.CategoryCreate, db:Session = Depends(get_db)):
    db_cat = models.Category(name = category.name, is_active=category.is_active )
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

# get all categories endpoint
@router.get("/category", response_model=List[schemas.CategoryOut], tags=["Category"])
def get_categories(db:Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return categories

# Create product endpoint
@router.post("/product", response_model=schemas.ProductOut, status_code=status.HTTP_201_CREATED, tags=["Product"])
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category_id=product.category_id,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Get all products with pagination filtering and sorting search
@router.get("/product", response_model=List[schemas.ProductOut], tags=["Product"])
def get_products(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    search:Optional[str] = Query(None, min_length=3, max_length=50),
    sort_by: Optional[str] = Query("id"),
    order_by: Optional[str] = Query("asc"),
    category_id: Optional[int] = Query(None, description="Filter by category ID")

):
    query = db.query(models.Product)
    if search:
        query = query.filter(models.Product.name.ilike(f"%{search}%"))
    if category_id:
        query = query.filter(models.Product.category_id == category_id)
    if sort_by:
        if order_by == "desc":
            query = query.order_by(getattr(models.Product, sort_by).desc())
        else:
            query = query.order_by(getattr(models.Product, sort_by).asc())
    else:
        query = query.order_by(getattr(models.Product,sort_by))

    products = query.offset(skip).limit(limit).all()
    return products