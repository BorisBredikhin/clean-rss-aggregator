import datetime
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from core.domain.models import User, Source, Subscription
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


class SourceRepository:
    @staticmethod
    def add(label: str, url: str) -> Source:
        with SessionLocal() as session:
            source = session.execute(select(Source) \
                                     .where(Source.url == url)).first()
            if source is None:
                source = Source(label=label, url=url)
                session.add(source)
                session.commit()
            else:
                source = source.Source
            return source

    @staticmethod
    def subscribe(user: User, source: Source, label: str) -> Subscription:
        with SessionLocal() as session:
            subscription = Subscription(
                    user_id=user.id,
                    source_id=source.id,
                    subscribed_at=datetime.datetime.now(),
                    label=label
            )
            session.add(subscription)
            session.commit()
