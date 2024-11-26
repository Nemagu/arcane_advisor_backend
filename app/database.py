from config import settings
from sqlalchemy import URL, create_engine, text
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

sync_engine = create_engine(
    url=settings.DATABASE_URL,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

# async_engine = create_async_engine(
#     url=settings.DATABASE_URL,
#     echo=True,
#     # pool_size=5,
#     # max_overflow=10,
# )

session_factory = sessionmaker(sync_engine)
# async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass
