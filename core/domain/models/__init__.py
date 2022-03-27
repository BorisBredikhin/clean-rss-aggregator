from sqlalchemy import Column, Integer, String

from infrastructure.database import Base

class Source(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)
    url = Column(String)