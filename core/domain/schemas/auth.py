from pydantic import BaseModel, Field

class RegistrationSchema(BaseModel):
    nickname: str
    password: str
