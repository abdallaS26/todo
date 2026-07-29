import os

from sqlalchemy import create_engine, MetaData

# Use DATABASE_URL for PostgreSQL. The default here is PostgreSQL as requested.
# Example:
# export DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/todo_db"
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:123456@localhost:5432/todo_db",
)

engine = create_engine(DATABASE_URL, future=True)

metadata = MetaData()
