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
    name = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates="products")