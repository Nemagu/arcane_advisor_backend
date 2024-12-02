from datetime import datetime

from pydantic import BaseModel


class IdDTO(BaseModel):
    id: int


class CreatedAtUpdatedAtDTO(BaseModel):
    created_at: datetime
    updated_at: datetime


class NameDTO(BaseModel):
    name: str


class DescriptionDTO(BaseModel):
    description: str


class NameDescriptionDTO(NameDTO, DescriptionDTO):
    pass
