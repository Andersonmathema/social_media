from pydantic import BaseModel
from fastapi import HTTPException
from http import HTTPStatus

def login_wrong_exception():
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, 
        detail='Email/senha incorretos'
        )


def email_already_exists():
    raise HTTPException(
        status_code=HTTPStatus.CONFLICT, 
        detail='Email já cadastrado'
        )
