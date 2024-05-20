from typing import Optional, Type

from sqlmodel import Session
from Organizations.model import organization_model
from Organizations.model.organization_model import ListOrganization
from Organizations.schema.organization_schema import Organization
from Organizations.model.organization_model import Users


class Repository:
    @staticmethod
    def organization_create_repo(db: Session, req: Organization):
        db.add(req)
        db.commit()
        db.refresh(req)
        return req

    @staticmethod
    def organizations_read_repo(db: Session):
        return db.query(ListOrganization).all()

    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[Type[Users]]:
        return db.query(organization_model.Users).filter(organization_model.Users.username == username).first()


def organization_create_repo():
    return None


def organizations_read_repo():
    return None
