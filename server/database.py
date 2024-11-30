from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import (DeclarativeBase, Mapped, declared_attr,
                            mapped_column)

from config import settings

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
