from typing import Optional

from pydantic.main import BaseModel


class UserSignUp(BaseModel):
    username: str
    password: str


class UserSignUpOut(BaseModel):
    username: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
