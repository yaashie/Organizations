from datetime import timedelta, datetime
from typing import Optional, List
import jwt
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from passlib.context import CryptContext


class Security:
    SECRET_KEY = "fca72c61b841ed22f88dae4996e7e7a7b3bf8b71a0a1d1ed0ac8402ced420767"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> List:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, Security.SECRET_KEY, algorithm=Security.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def verify_password(plain_password, hashed_password) -> bool:
        return Security.pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password) -> str:
        return Security.pwd_context.hash(password)
