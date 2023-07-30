from datetime import datetime
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, Boolean, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from models.models import role
from time import ti

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base: DeclarativeMeta = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    username: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)

    register_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)

    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"))



# engine = create_async_engine(DATABASE_URL)
# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# async def create_db_and_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session


# async def get_user_db(session: AsyncSession = Depends(get_async_session)):
#     yield SQLAlchemyUserDatabase(session, User)