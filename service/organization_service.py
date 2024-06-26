from typing import Union, Type, Optional, Any, List
from sqlmodel import Session
from Organizations.model.organization_model import ListOrganization, Users

from Organizations.JWT_Security.security import Security
from Organizations.repository.organization_repository import Repository


class Service:
    @staticmethod
    def organizations_create_service(db: Session, organ: str) -> ListOrganization:
        org = ListOrganization(name=organ)
        return Repository.organization_create_repo(db, org)

    @staticmethod
    def organization_read_service(db: Session) -> Any:
        return Repository.organizations_read_repo(db)

    @staticmethod
    def authenticate_user(username: str, password: str, db: Session) -> Union[bool, Any]:
        user = Repository.get_user_by_username(db, username)
        if not user:
            return False
        if not Security.verify_password(password, user.hashed_password): #type: ignore
            return False
        return user

    @staticmethod
    def get_user(username: str, db: Session) -> Any:
        user = Repository.get_user_by_username(db, username)
        if user:
            return user
        return None
