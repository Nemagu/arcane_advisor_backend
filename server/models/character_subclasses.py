from database import Base

from .mixins import (
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin
)


class CharacterSubclass(
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin,
    Base,
):
    pass
