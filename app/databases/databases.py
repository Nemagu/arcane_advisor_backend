# from app.config import settings
from sqlalchemy import URL, create_engine, text
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine(
    # url=settings.DATABASE_URL_asyncpg,
    url='sqlite+psycopg:///:memory:',
    echo=True,
    # pool_size=1,
    # max_overflow=0,
)

with engine.connect() as conn:
    res = conn.execute(text('SELECT VERSION()'))
    print(f'{res=}')
