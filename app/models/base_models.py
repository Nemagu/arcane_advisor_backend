from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from .consts import MAX_LENGTH_NAME, MIN_VALUE_COUNT


class Count(SQLModel):
    count: int = Field(
        min_length=MIN_VALUE_COUNT,
        title='Количество',
        description='Поле для указания количества.',
    )


class Description(SQLModel):
    description: Optional[str] = Field(
        default=None,
        title='Описание',
        description='Описание записи.',
    )


class EditedBy(SQLModel):
    edited_by: datetime | None = Field(
        default=datetime.now,
        title='Дата изменения',
        description='Дата изменения записи.',
    )


class Id(SQLModel):
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        index=True,
    )


class IdEditedBy(Id, EditedBy):
    pass


class Name(SQLModel):
    name: str = Field(
        max_length=MAX_LENGTH_NAME,
        index=True,
        title='Название',
        description='Название записи.'
    )


class UniqueName(SQLModel):
    name: str = Field(
        max_length=MAX_LENGTH_NAME,
        index=True,
        unique=True,
        title='Название',
        description='Название записи.'
    )
