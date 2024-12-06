from pydantic_settings import BaseSettings, SettingsConfigDict


class Settigs(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_ECHO: str

    model_config = SettingsConfigDict(env_file='.env')

    @property
    def db_echo(self) -> bool:
        return True if self.DB_ECHO == 'true' else False

    @property
    def DATABASE_URL_async(self) -> str:
        return (
            f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@'
            f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )

    @property
    def DATABASE_URL_sync(self) -> str:
        return (
            f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@'
            f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )


settings = Settigs()
