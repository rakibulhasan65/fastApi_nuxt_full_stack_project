# add to cart table model
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
class AddToCart(Base):
    __tablename__ = 'add_to_cart'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, default=1)

    user = relationship("User", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")