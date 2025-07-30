from pydantic import BaseModel

from typing import Optional

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
    name: str
    description: str
    price: int
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    category: CategoryOut

    class Config:
        orm_mode = True
