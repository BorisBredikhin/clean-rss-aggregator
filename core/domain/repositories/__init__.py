from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from core.domain.models import User
from infrastructure.database import engine, SessionLocal


class UserRepository:
    @staticmethod
    def create(nickname: str, password: str) -> User:
        with Session(engine) as session:
            user = User(nickname=nickname, password=password)
            session.add(user)
            session.commit()
            return user


    @staticmethod
    def login(nickname: str, password: str) -> Optional[User]:
        with SessionLocal() as session:
            user = session.execute(select(User) \
                                   .where(User.nickname == nickname, User.password == password))
            try:
                return user.first().User
            except AttributeError:
                return None
