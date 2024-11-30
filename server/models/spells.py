from database import Base
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column


class Spell(Base):
    __tablename__ = 'spell'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    __table_args__ = (
        CheckConstraint('LENGTH(name) < 60', name='max_length_name'),
    )
