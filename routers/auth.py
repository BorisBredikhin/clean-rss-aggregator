import hashlib

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED

from core.dependencies.auth import get_token, get_current_user
from core.domain.models import User
from core.domain.repositories import UserRepository
from core.domain.schemas import RegistrationSchema

router = APIRouter(
    prefix=''
)


@router.post('/register')
async def register(data: RegistrationSchema):
    user = UserRepository.create(data.nickname, hashlib.sha1(data.password).hexdigest())
    return Response()


@router.post('/token')
async def login(data: OAuth2PasswordRequestForm = Depends()):
    user = UserRepository.login(data.username, hashlib.sha1(data.password).hexdigest())
    if user is None:
        return Response("wrong credentials", HTTP_401_UNAUTHORIZED)
    return {"access_token": get_token(user), "token_type": "bearer"}


@router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
