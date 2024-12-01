from database import Base

from .mixins import NameUniqueMaxLength50Mixin, TimestampMixin


class UnitDuration(
    NameUniqueMaxLength50Mixin,
    TimestampMixin,
    Base,
):
    pass
