from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from database import Base

if TYPE_CHECKING:
    from .spells import Spell
    from .unit_durations import UnitDuration


class SpellDuration(Base):
    count: Mapped[int]
    unit_duration_id: Mapped[int] = mapped_column(
        ForeignKey(
            'unitduration.id', ondelete='CASCADE',
        ),
        primary_key=True,
    )
    spell_id: Mapped[int] = mapped_column(
        ForeignKey(
            'spell.id', ondelete='CASCADE',
        ),
        primary_key=True,
    )

    unit_duration: Mapped['UnitDuration'] = relationship(
        back_populates='spell_durations',
    )
    spell: Mapped['Spell'] = relationship(
        back_populates='spell_duration',
    )

    @declared_attr.directive
    def __table_args__(cls):
        return (
            CheckConstraint(
                'count >= 0',
                name='min_value_spell_duration_count',
            ),
            UniqueConstraint(
                'unit_duration_id',
                'spell_id',
                name='unique_unit_duration_spell',
            ),
        )
