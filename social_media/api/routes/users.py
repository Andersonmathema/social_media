from fastapi import APIRouter
from social_media.api.dtos.users import UserRegistration, UserLogin
from social_media.datalayer.models.user import UserModel

router = APIRouter(
    prefix="/users",
    tags=['users'],
    responses={404: {'description': "Not found"}},
)

@router.post('/register')
async def register(body: UserRegistration):
    user = await UserModel.create(
        name = body.name,
        email = body.email,
        password = body.password
    )
    return {'created': user}


@router.post('/login')
async def login(body: UserLogin):
    # Busca no banco de dados pelo email
    # Se o email não existe, retorna o erro
    try:
        user: UserModel = UserModel.filter(email = body.email).first()
    except Exception:
        return {'error': 'Email/senha incorretos.'}
    # Se existir, verificar se a senha é igual
    if user.password != body.password:
        return {'error': 'Email/senha incorretos.'}
    # Se a senha estiver errada: retorna email/senha incorreto

    # Se estiver certa, realiza login


@router.get('/get-users')
async def get_users():
    users = await UserModel.all()
    return {'users': users}
