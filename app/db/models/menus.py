from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

"""
SQLAlchemy ORM models for the menu system:

- Menu: A collection of menu items.
- MenuItem: An individual item that can appear on one or more menus.
- MenuItemMenu: Junction table associating Menu and MenuItem with a specific price.
"""


if TYPE_CHECKING:
    from app.db.models.orders import OrderItem
    from app.db.models.restaurants import Restaurant


class Menu(Base):
    __tablename__ = "menus"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    restaurant_id: Mapped[int] = mapped_column(
        ForeignKey("restaurants.id", ondelete="CASCADE"), nullable=False
    )

    restaurant: Mapped["Restaurant"] = relationship(
        "Restaurant", back_populates="menus"
    )
    items: Mapped[list["MenuItemMenu"]] = relationship(
        "MenuItemMenu", back_populates="menu", cascade="all, delete-orphan"
    )


class MenuItem(Base):
    __tablename__ = "menu_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    image_url: Mapped[str | None] = mapped_column(String, nullable=True)

    menus: Mapped[list["MenuItemMenu"]] = relationship(
        "MenuItemMenu", back_populates="menu_item", cascade="all, delete-orphan"
    )
    orders: Mapped[list["OrderItem"]] = relationship(
        "OrderItem", back_populates="menu_item"
    )


class MenuItemMenu(Base):
    __tablename__ = "menu_item_menus"

    id: Mapped[int] = mapped_column(primary_key=True)
    menu_id: Mapped[int] = mapped_column(
        ForeignKey("menus.id", ondelete="CASCADE"), nullable=False
    )
    menu_item_id: Mapped[int] = mapped_column(
        ForeignKey("menu_items.id", ondelete="CASCADE"), nullable=False
    )
    price: Mapped[float] = mapped_column(Float, nullable=False)

    menu: Mapped["Menu"] = relationship("Menu", back_populates="items")
    menu_item: Mapped["MenuItem"] = relationship("MenuItem", back_populates="menus")
