import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Using environment variable for database URL
database_url = os.environ.get("DATABASE_URL")

# Ensure DATABASE_URL is set
if not database_url:
    raise ValueError("DATABASE_URL environment variable is not set.")

# Creating the engine to interact with PostgreSQL
engine = create_engine(database_url, echo=True)

# Creating a session local class to interact with the database
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class to create tables
Base = declarative_base()