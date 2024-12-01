from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from database import Base

from .mixins import NameUniqueMaxLength50Mixin, TimestampMixin

if TYPE_CHECKING:
    from .spell_durations import SpellDuration


class UnitDuration(
    NameUniqueMaxLength50Mixin,
    TimestampMixin,
    Base,
):
    spell_durations: Mapped[list['SpellDuration']] = relationship(
        back_populates='unit_duration',
    )
