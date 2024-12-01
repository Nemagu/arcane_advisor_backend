from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column


class NameUniqueMaxLength50Mixin:
    name: Mapped[str] = mapped_column(unique=True)

    __table_args__ = (
        CheckConstraint(
            'LENGTH(name) < 50',
            name='max_length_name',
        ),
    )
