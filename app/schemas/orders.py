from pydantic import BaseModel
from typing import Optional, List

class OrderBase(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    status: Optional[str] = "pending"  # Default status is 'pending'
class OrderCreate(OrderBase):
    pass
class OrderOut(OrderBase):
    id: int

    class Config:
        orm_mode = True
class OrderList(BaseModel):
    orders: List[OrderOut]
    total: int  # Total number of orders

    class Config:
        orm_mode = True

class OrderUpdate(BaseModel):
    quantity: Optional[int] = None
    status: Optional[str] = None  # e.g., 'pending', 'completed', 'cancelled'

    class Config:
        orm_mode = True
class OrderStatus(BaseModel):
    status: str  # e.g., 'pending', 'completed', 'cancelled'

    class Config:
        orm_mode = True
class OrderPagination(BaseModel):
    page: int = 1
    limit: int = 10
    total_pages: int = 0
    total_items: int = 0

    class Config:
        orm_mode = True
class OrderFilter(BaseModel):
    user_id: Optional[int] = None
    product_id: Optional[int] = None
    status: Optional[str] = None  # e.g., 'pending', 'completed', 'cancelled'
    search: Optional[str] = None  # Search term for product name or user details

    class Config:
        orm_mode = True
        