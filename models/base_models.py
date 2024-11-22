from sqlmodel import Field, SQLModel

from .consts import MAX_LENGTH_NAME


class Id(SQLModel):
    id: int | None = Field(
        default=None,
        primary_key=True,
        index=True,
    )


class UniqueName(SQLModel):
    name: str = Field(
        max_length=MAX_LENGTH_NAME,
        index=True,
        unique=True,
        title='Название',
        description='Название записи.'
    )


class Name(SQLModel):
    name: str = Field(
        max_length=MAX_LENGTH_NAME,
        index=True,
        title='Название',
        description='Название записи.'
    )


class Description(SQLModel):
    description: str | None = Field(
        default=None,
        title='Описание',
        description='Описание записи.',
    )
