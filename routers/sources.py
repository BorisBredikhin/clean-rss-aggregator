import hashlib

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED

from core.dependencies.auth import get_token, get_current_user
from core.domain.models import User
from core.domain.repositories import SourceRepository
from core.domain.schemas import AddSourceSchema, PostSchema

router = APIRouter(
    prefix='/source'
)


@router.post('')
async def add(data: AddSourceSchema, current_user: User = Depends(get_current_user)):
    source = SourceRepository.add(data.label, data.url)
    SourceRepository.subscribe(current_user, source, data.label)
    return Response(status_code=201)

@router.get('/', response_model=list[PostSchema])
async def list(current_user: User = Depends(get_current_user)):
    return SourceRepository.get_subscriptions(current_user)
