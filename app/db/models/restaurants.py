from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

    # restaurant must have a user
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="restaurant", uselist=False)
