from fastapi import APIRouter

router = APIRouter(
    # prefix="/users",
    # tags=['users'],
    # responses={404: {'description': "Not found"}},
)

@router.get("/users/", tags=['users'])
async def read_users():
    return [{"name": "Rick"}, {"name": "Morty"}]


@router.get('/')
async def home():
    return {'status': 'ok'}