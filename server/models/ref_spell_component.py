from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from database import Base


class RefSpellComponent(Base):
    spell_id: Mapped[int] = mapped_column(
        ForeignKey('spell.id', ondelete='CASCADE'),
        primary_key=True,
    )
    component_id: Mapped[int] = mapped_column(
        ForeignKey('spellcomponent.id', ondelete='CASCADE'),
        primary_key=True,
    )

    @declared_attr.directive
    def __table_args__(cls):
        return (
            UniqueConstraint(
                'spell_id',
                'component_id',
                name='unique_components_for_spell',
            ),
        )
