from config import Base
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base_datatype import created_at, primaryk, unique_name_60, updated_at


class Spell(Base):
    __tablename__ = 'spell'

    id: Mapped[primaryk]
    # created_at: Mapped[created_at]
    # updated_at: Mapped[updated_at]
    unique_name: Mapped[unique_name_60]

    __table_args__ = (
        CheckConstraint('unique_name > 0', name='dsaf'),
        CheckConstraint('unique_name < 60', name='dsadsfaf'),
    )
