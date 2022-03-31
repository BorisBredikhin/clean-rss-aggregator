import secrets
from typing import Optional

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from core.domain.models import User

_d: dict[str, User] = {}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def auth(token: str) -> Optional[User]:
    return _d.get(token, None)


def get_token(user: User) -> str:
    token = secrets.token_urlsafe(64)
    _d[token] = user
    return token


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = auth(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
