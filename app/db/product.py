from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive

    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    product_code = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Integer)
    image = Column(String, nullable=True)
    is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive
    in_stock = Column(Integer, default=0)  # Quantity in stock
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates="products")
    orders = relationship("Order", back_populates="product")
    cart_items = relationship("AddToCart", back_populates="product")