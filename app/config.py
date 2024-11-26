from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    @property
    def DATABASE_URL_asyncpg(self):
        return 'sqlite+psycopg:///:memory:'


settings = Settings()
