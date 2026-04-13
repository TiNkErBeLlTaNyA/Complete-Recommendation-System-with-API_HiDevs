from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    interests = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class Content(Base):
    __tablename__ = "content"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    category = Column(String)
    difficulty = Column(String)
    popularity = Column(Float)


class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content_id = Column(Integer, ForeignKey("content.id"))
    type = Column(String)
    rating = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)