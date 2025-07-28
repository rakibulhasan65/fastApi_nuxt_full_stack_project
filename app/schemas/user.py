from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserCreate(UserBase):
    pass

class UserShow(UserBase):
    id: int

    class Config:
        orm_mode = True

class userLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str