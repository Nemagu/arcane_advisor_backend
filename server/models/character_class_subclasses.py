from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from database import Base


class CharacterClassSubclass(Base):
    character_class_id: Mapped[int] = mapped_column(
        ForeignKey('characterclass.id', ondelete='CASCADE'),
        primary_key=True,
    )
    character_subclass_id: Mapped[int] = mapped_column(
        ForeignKey('charactersubclass.id', ondelete='CASCADE'),
        primary_key=True,
    )

    # character_class: Mapped['CharacterClass'] = relationship(
    #     back_populates='combination_character_class_subclass',
    # )
    # character_subclass: Mapped['CharacterSubclass'] = relationship(
    #     back_populates='combination_character_class_subclass',
    # )

    @declared_attr.directive
    def __table_args__(cls):
        return (
            UniqueConstraint(
                'character_class_id',
                'character_subclass_id',
                name='unique_character_class_subclass',
            ),
        )
