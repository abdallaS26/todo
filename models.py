from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    ForeignKey
)

from sqlalchemy.sql import func

from database import metadata


users = Table(
    "users",
    metadata,

    Column(
        "id",
        Integer,
        primary_key=True
    ),

    Column(
        "email",
        String,
        unique=True,
        nullable=False
    ),

    Column(
        "password",
        String,
        nullable=False
    ),

    Column(
        "name",
        String,
        nullable=False
    ),

    Column(
        "created_at",
        DateTime,
        server_default=func.now()
    )
)


todos = Table(
    "todos",
    metadata,

    Column(
        "id",
        Integer,
        primary_key=True
    ),

    Column(
        "user_id",
        Integer,
        ForeignKey("users.id")
    ),

    Column(
        "title",
        String,
        nullable=False
    ),

    Column(
        "description",
        Text
    ),

    Column(
        "parent_todo_id",
        Integer,
        ForeignKey("todos.id")
    ),

    Column(
        "created_at",
        DateTime,
        server_default=func.now()
    ),

    Column(
        "completed",
        Boolean,
        default=False
    )
)