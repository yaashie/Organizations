from typing import Union
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from Organizations.database import Database


class ListOrganization(Database.Base): #type: ignore
    __tablename__ = "List_Organizations"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Users(Database.Base): #type: ignore
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class OrganizationBase(BaseModel):
    name: str


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationRead(OrganizationBase):
    id: int


class User(BaseModel):
    username: str


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class CryptContext:
    @staticmethod
    def verify(plain_password : str, hashed_password : str) -> None:
        pass

    @staticmethod
    def hash(password : str) -> None:
        pass
