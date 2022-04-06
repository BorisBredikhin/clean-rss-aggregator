from datetime import datetime
from pydantic import BaseModel, AnyUrl


class AddSourceSchema(BaseModel):
    label: str
    url: AnyUrl

class PostSchema(BaseModel):
    source: int
    title: str
    link: AnyUrl
    pub_date: datetime

    class Comfig:
        orm_mode = True
