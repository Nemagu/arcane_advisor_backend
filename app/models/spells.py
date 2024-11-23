from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship

from .base_models import Description, IdEditedBy, UniqueName
from .consts import MIN_VALUE_SPELL_RANGE
from .spell_character_class_link import SpellCharacterClassLink
from .spell_component_link import SpellComponentLink

if TYPE_CHECKING:
    from .character_class_subclasses import CharacterClassSubclass
    from .damege_type import DamegeType
    from .source import Source
    from .spell_components import SpellComponent
    from .spell_levels import SpellLevel
    from .spell_schools import SpellSchool


class Spell(IdEditedBy, Description, UniqueName, table=True):
    spell_range: int = Field(
        min_length=MIN_VALUE_SPELL_RANGE,
        title='Дальность',
        description='Дальность заклинания.',
    )
    next_level: Optional[str] = Field(
        default=None,
        title='Бафы для сдующего уровня',
        description=(
            'Бафы использования заклинания при использовании ячейки '
            'следующего уровня.'
        ),
    )
    ritual: Optional[bool] = Field(
        default=False,
        title='Ритуал',
        description='Нужно ли производить для заклинания ритуал.',
    )
    concentration: Optional[bool] = Field(
        default=False,
        title='Концентрация',
        description='Требуется для заклинания концентрация.',
    )

    school: Optional['SpellSchool'] = Relationship(
        back_populates='spells'
    )
    school_id: Optional[int] = Field(
        default=None,
        foreign_key='school.id',
    )
    level: 'SpellLevel' = Relationship(
        back_populates='spells'
    )
    level_id: Optional[int] = Field(
        default=None,
        foreign_key='level.id',
    )
    damege_type: 'DamegeType' = Relationship(
        back_populates='spells'
    )
    damege_type_id: Optional[int] = Field(
        default=None,
        foreign_key='damege_type.id',
    )
    source: 'Source' = Relationship(
        back_populates='spells'
    )
    source_id: Optional[int] = Field(
        default=None,
        foreign_key='source.id',
    )

    components: Optional[list['SpellComponent']] = Relationship(
        back_populates='spells',
        link_model=SpellComponentLink,
    )
    character_classes: Optional[list['CharacterClassSubclass']] = Relationship(
        back_populates='spells',
        link_model=SpellCharacterClassLink,
    )
