from fastapi import APIRouter
from social_media.api.dtos.users import UserRegistration, UserLogin
from social_media.datalayer.models.user import UserModel
from social_media.api.responses.user import (
    login_wrong_exception,
    email_already_exists,
    )

router = APIRouter(
    prefix="/users",
    tags=['users'],
    responses={404: {'description': "Not found"}},
)

@router.post('/register')
async def register(body: UserRegistration):

    # Verifica se o email já existe
    email_exists = await UserModel.filter(email=body.email)
    # Se existir dá conflito
    if email_exists:
        raise email_already_exists()
    # Se não existir, cria o usuário
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
    user = None
    try:
        user = await UserModel.get(email = body.email)
    except Exception:
        raise login_wrong_exception()
    # Se existir, verificar se a senha é igual
    # Se a senha estiver errada: retorna email/senha incorreto
    if user.password != body.password:
        raise login_wrong_exception()
    # Se estiver certa, realiza login
    return user



