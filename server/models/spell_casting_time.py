from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from database import Base

if TYPE_CHECKING:
    from .spells import Spell
    from .unit_durations import UnitDuration


class SpellCastingTime(Base):
    count: Mapped[int]
    unit_duration_id: Mapped[int] = mapped_column(
        ForeignKey('unitduration.id', ondelete='CASCADE'),
    )
    spell_id: Mapped[int] = mapped_column(
        ForeignKey('spell.id', ondelete='CASCADE'),
    )

    unit_duration: Mapped['UnitDuration'] = relationship(
        back_populates='spell_casting_times',
    )
    spell: Mapped['Spell'] = relationship(
        back_populates='casting_time',
    )

    @declared_attr.directive
    def __table_args__(cls):
        return (
            CheckConstraint(
                'count >= 0',
                name='min_value_spell_casting_time_count',
            ),
            UniqueConstraint(
                'unit_duration_id',
                'spell_id',
                name='unique_casting_time_spell',
            ),
        )
