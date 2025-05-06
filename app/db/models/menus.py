from app.db.database import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

"""
SQLAlchemy ORM models for the menu system:

- Menu: A collection of menu items.
- MenuItem: An individual item that can appear on one or more menus.
- MenuItemMenu: Junction table associating Menu and MenuItem with a specific price.
"""


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id", ondelete="CASCADE"), nullable=False)

    restaurant = relationship("Restaurant", back_populates="menus")
    items = relationship("MenuItemMenu", back_populates="menu", cascade="all, delete-orphan")


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    image_url = Column(String)

    menus = relationship("MenuItemMenu", back_populates="menu_item", cascade="all, delete-orphan")
    orders = relationship("OrderItem", back_populates="menu_item")


class MenuItemMenu(Base):
    __tablename__ = "menu_item_menus"

    id = Column(Integer, primary_key=True)
    menu_id = Column(Integer, ForeignKey("menus.id", ondelete="CASCADE"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id", ondelete="CASCADE"), nullable=False)
    price = Column(Float, nullable=False)

    menu = relationship("Menu", back_populates="items")
    menu_item = relationship("MenuItem", back_populates="menus")