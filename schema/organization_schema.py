from pydantic import BaseModel


class Organization(BaseModel):
    name: str


class Organization_create(Organization):
    pass


class Organization_read(Organization):
    id: int


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserInDB:
    def __init__(self):
        self.hashed_password = None
    pass

