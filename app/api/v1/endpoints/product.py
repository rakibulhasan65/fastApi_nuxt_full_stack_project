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
@router.post("/products", response_model=schemas.ProductOut, status_code=status.HTTP_201_CREATED, tags=["Product"])
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    print(product)
    db_product = models.Product(
        product_code=product.product_code,
        image=product.image,
        in_stock=product.in_stock,
        is_active=product.is_active,
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
@router.get("/products", response_model=schemas.ProductListResponse, tags=["Product"])
def get_products(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    search:Optional[str] = Query(None , description="Search by product name"),
    sort_by: Optional[str] = Query("id"),
    order_by: Optional[str] = Query("asc"),
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    
):
   query = db.query(models.Product)
   # Apply search filter
   if search:
       query = query.filter(models.Product.name.ilike(f"%{search}%"))

    # Apply category filter
   if category_id:
        query = query.filter(models.Product.category_id == category_id)

    # Calculate total count AFTER filter
   total_count = query.count()

    # Sorting
   if sort_by:
        if order_by == "desc":
            query = query.order_by(getattr(models.Product, sort_by).desc())
        else:
            query = query.order_by(getattr(models.Product, sort_by).asc())

    # Pagination
   products = query.offset(skip).limit(limit).all()

    # Total pages calculation
   total_pages = (total_count + limit - 1) // limit

   return {
        "products": products,
        "totalPages": total_pages,
        "totalCount": total_count,
        "currentPage": (skip // limit) + 1
    }

# product delete endpoint
@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Product"])
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted successfully"}