from fastapi import APIRouter

from queries import AsyncORM
from schemas import CharacterClassRefAllDTO

router = APIRouter(prefix='/character-classes', tags=['character-classes'])


@router.get('/', response_model=list[CharacterClassRefAllDTO])
async def get_character_classes():
    res = await AsyncORM.get_all_character_classes_all_ref()
    resl = [CharacterClassRefAllDTO.model_validate(
        row, from_attributes=True) for row in res]
    return resl
