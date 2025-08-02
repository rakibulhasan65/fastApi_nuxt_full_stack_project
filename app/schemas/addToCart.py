from pydantic import BaseModel
from typing import Optional, List

# addToCart schema
class AddToCartBase(BaseModel):
    user_id: int
    product_id: int
    quantity: int
class AddToCartCreate(AddToCartBase):
    pass
class AddToCartOut(AddToCartBase):
    id: int

    class Config:
        orm_mode = True
class AddToCartList(BaseModel):
    cart_items: List[AddToCartOut]
    total: int  # Total number of items in the cart

    class Config:
        orm_mode = True 
class AddToCartUpdate(BaseModel):
    quantity: Optional[int] = None

    class Config:
        orm_mode = True
class AddToCartFilter(BaseModel):
    user_id: Optional[int] = None
    product_id: Optional[int] = None
    search: Optional[str] = None  # Search term for product name or user details

    class Config:
        orm_mode = True
class AddToCartPagination(BaseModel):
    page: int = 1
    limit: int = 10
    total_pages: int = 0
    total_items: int = 0

    class Config:
        orm_mode = True