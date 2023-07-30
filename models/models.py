from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON), 
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("register_at", TIMESTAMP, default=datetime.utcnow), # function cant be used!
    Column("role_id", Integer, ForeignKey("role.id")) # reference to roles table -> id column
)