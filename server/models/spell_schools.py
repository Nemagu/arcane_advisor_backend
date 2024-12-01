from database import Base

from .mixins import (
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin
)


class SpellSchool(
    DescriptionMixin,
    NameUniqueMaxLength50Mixin,
    TimestampMixin,
    Base,
):
    pass
