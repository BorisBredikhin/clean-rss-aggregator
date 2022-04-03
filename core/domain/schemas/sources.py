from pydantic import BaseModel, AnyUrl


class AddSourceSchema(BaseModel):
    label: str
    url: AnyUrl
