from config import settings
from sqlalchemy import URL, create_engine, text
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
)

with engine.connect() as conn:
    res = conn.execute(text('SELECT VERSION()'))
    print(f'{res=}')
