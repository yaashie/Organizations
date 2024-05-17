from fastapi import Depends
from sqlmodel import Session
from Organizations.model.organization_model import ListOrganization
from Organizations.route import get_db
from Organizations.repository.organization_repository import organization_create_repo, organizations_read_repo


def organizations_create_service(db: Session, organ: str):
    org = ListOrganization(name=organ)
    return organization_create_repo(db, org)


def organization_read_service(db: Session):
    return organizations_read_repo(db)
