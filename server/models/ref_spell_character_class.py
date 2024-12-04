from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from database import Base


class RefSpellCharacterClass(Base):
    spell_id: Mapped[int] = mapped_column(
        ForeignKey('spell.id', ondelete='CASCADE'),
        primary_key=True,
    )
    character_class_id: Mapped[int] = mapped_column(
        ForeignKey('characterclass.id', ondelete='CASCADE'),
        primary_key=True,
    )

    @declared_attr.directive
    def __table_args__(cls):
        return (
            UniqueConstraint(
                'spell_id',
                'character_class_id',
                name='unique_character_classes_for_spell',
            ),
        )
