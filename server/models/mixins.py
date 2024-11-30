import datetime

from sqlalchemy import CheckConstraint, text
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class TimestampMixin:
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text('TIMEZONE(\'utc\', now())'),

    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text('TIMEZONE(\'utc\', now())'),
        onupdate=datetime.datetime.utcnow,
    )


class UniqueNameMaxLength50Mixin:
    name: Mapped[str] = mapped_column(unique=True)

    __table_args__ = (
        CheckConstraint(
            'LENGTH(name) < 50',
            name='max_length_name',
        ),
    )


class DescriptionNullableMixin:
    description: Mapped[str] = mapped_column(nullable=True)


class DescriptionMixin:
    description: Mapped[str]
