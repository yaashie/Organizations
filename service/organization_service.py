from typing import Union, Type, Optional
from sqlmodel import Session
from Organizations.model.organization_model import ListOrganization, Users

from Organizations.JWT_Security.security import Security
from Organizations.repository.organization_repository import Repository


class Service:
    @staticmethod
    def organizations_create_service(db: Session, organ: str):
        org = ListOrganization(name=organ)
        return Repository.organization_create_repo(db, org)

    @staticmethod
    def organization_read_service(db: Session):
        return Repository.organizations_read_repo(db)

    @staticmethod
    def authenticate_user(username: str, password: str, db: Session) -> Union[bool, Type[Users]]:
        user = Repository.get_user_by_username(db, username)
        if not user:
            return False
        if not Security.verify_password(password, user.hashed_password):
            return False
        return user

    @staticmethod
    def get_user(username: str, db: Session) -> Optional[Type[Users]]:
        user = Repository.get_user_by_username(db, username)
        if user:
            return user
        return None
