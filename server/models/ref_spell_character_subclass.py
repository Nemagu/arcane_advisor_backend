from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from database import Base


class RefSpellCharacterSubclass(Base):
    spell_id: Mapped[int] = mapped_column(
        ForeignKey('spell.id', ondelete='CASCADE'),
    )
    character_subclass_id: Mapped[int] = mapped_column(
        ForeignKey('charactersubclass.id', ondelete='CASCADE'),
    )

    @declared_attr.directive
    def __table_args__(cls):
        return (
            UniqueConstraint(
                'spell_id',
                'character_subclass_id',
                name='unique_character_subclasses_for_spell',
            ),
        )
