import datetime
from typing import Optional

from bs4 import BeautifulSoup
import requests
from sqlalchemy import select
from sqlalchemy.orm import Session

from core.domain.models import User, Source, Subscription, Post
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
            return subscription

    @staticmethod
    def get_subscriptions(user: User) -> list[Subscription]:
        with SessionLocal() as session:
            subscriptions = session.execute(
                    select(Subscription).where(Subscription.user_id==user.id)
            ).all()
            return subscriptions

class PostRepository:
    @staticmethod
    def get_posts(source: Source) -> list[Post]:
        url = source.url
        data = requests.get(url).content
        soup = BeautifulSoup(data)
        posts = soup.find_all('item')
        result = []
        with SessionLocal() as session:
            for post in posts:
                 db_post = Post()
                 db_post.source = source
                 db_post.title = post.find_next('title').text
                 db_post.link = post.find_next('link').text
                 db_post.pub_date = post.find_next('pubDate').text
                 session.add(db_post)
            session.commit()
            result.append(post)
        return result
