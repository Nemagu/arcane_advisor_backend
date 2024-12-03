from fastapi import APIRouter

router = APIRouter(prefix='/spells', tags=('users',))


@router.get('')
async def get_spells():
    return None
