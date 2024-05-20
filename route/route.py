from datetime import timedelta
import jwt
from jwt import PyJWTError
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Type, Dict, Union

from Organizations.model.organization_model import Users
from Organizations.JWT_Security.security import Security
from Organizations.model import organization_model
from Organizations.schema.organization_schema import Organization_create
from Organizations.service.organization_service import Service
from Organizations.database import Database


app = FastAPI()
Database.Base.metadata.create_all(bind=Database.engine)


class User:
    @staticmethod
    def get_current_user(
            token: str = Depends(Security.oauth2_scheme),
            db: Session = Depends(Database.get_db)) -> Type[Users]:

        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, Security.SECRET_KEY, algorithms=[Security.ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = organization_model.TokenData(username=username)
        except PyJWTError:
            raise credentials_exception
        user = Service.get_user(token_data.username, db)
        if user is None:
            raise credentials_exception
        return user


class Route:
    @staticmethod
    @app.post("/Organization")
    def organization_name(org: Organization_create, db: Session = Depends(Database.get_db)):
        return Service.organizations_create_service(db, org.name)

    @staticmethod
    @app.post('/token')
    def generate_token(form_data: OAuth2PasswordRequestForm = Depends(),
                       db: Session = Depends(Database.get_db)) -> Dict[str, Union[list, str]]:
        user = Service.authenticate_user(form_data.username, form_data.password, db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=Security.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = Security.create_access_token(data={"sub": user.username},
                                                    expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}

    @staticmethod
    @app.get("/Organizations")
    def organizations(db: Session = Depends(Database.get_db)):
        return Service.organization_read_service(db)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0', port=9000)
