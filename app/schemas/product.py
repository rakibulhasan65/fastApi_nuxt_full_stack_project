from pydantic import BaseModel

from typing import Optional, List

class CategoryBase(BaseModel):
    name: str
    is_active: Optional[int] = 1

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    product_code: Optional[str] = None
    image: Optional[str] = None
    name: str
    description: str
    price: int
    is_active: Optional[int] = 1  # 1 for active, 0 for inactive
    in_stock: Optional[int] = 0  # Quantity in stock
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    category: CategoryOut

    class Config:
        orm_mode = True
class ProductListResponse(BaseModel):
    products: List[ProductOut]
    totalPages: int
    totalCount: int
    currentPage: int
