from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column
)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncEngine

from config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self._engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self._session_factory = async_sessionmaker(
            bind=self._engine,
            # autoflush=False,
            # expire_on_commit=False,
        )

    @property
    def engine(self) -> 'AsyncEngine':
        return self._engine

    @property
    def session(self):
        return self._session_factory()


db_helper = DatabaseHelper(
    url=settings.DATABASE_URL_async,
    echo=settings.db_echo,
)


async_engine = create_async_engine(
    url=settings.DATABASE_URL_async,
    echo=True,
)

async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    repr_columns_number: int = 3
    repr_columns: tuple = tuple()

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def __repr__(self):
        columns: list = list()
        for idx, column in enumerate(self.__table__.columns.keys()):
            if column in self.repr_columns or idx < self.repr_columns_number:
                columns.append(f'{column}={getattr(self, column)}')
        return f'<{self.__class__.__name__} {', '.join(columns)}>'
