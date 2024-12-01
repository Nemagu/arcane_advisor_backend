from sqlalchemy.orm import Mapped, mapped_column


class DescriptionNullableMixin:
    description: Mapped[str] = mapped_column(nullable=True)


class DescriptionMixin:
    description: Mapped[str]
