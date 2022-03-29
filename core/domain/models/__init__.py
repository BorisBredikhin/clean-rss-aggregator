from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from infrastructure.database import Base

class Source(Base):
    __tablename__ = "source"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)
    url = Column(String)

    users = relationship('Subscription', back_populates='source')


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer(), ForeignKey(Source.id))
    
    source = relationship('Source', foreign_keys='Post.source_id')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String)
    password = Column(String)

    sources = relationship('Subscription', back_populates='user')


class Subscription(Base):
    __tablename__ = 'subscription'

    user_id = Column(ForeignKey('user.id'), primary_key=True)
    source_id = Column(ForeignKey('source.id'), primary_key=True)
    subscribed_at = Column(DateTime)

    user = relationship('User', back_populates='sources')
    source = relationship('Source', back_populates='users')
