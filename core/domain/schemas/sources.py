from datetime import datetime
from pydantic import BaseModel, AnyUrl


class AddSourceSchema(BaseModel):
    label: str
    url: AnyUrl

    class Config:
        orm_mode = True

class PostSchema(BaseModel):
    source: int
    title: str
    link: AnyUrl
    pub_date: datetime

    class Config:
        orm_mode = True
