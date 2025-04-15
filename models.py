from sqlalchemy import Column, Integer, String
from database import Base

# Define the Book model
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)