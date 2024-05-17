from pyexpat import model

from fastapi import Depends
from sqlmodel import Session
from Organizations.model import organization_model
from Organizations.model.organization_model import ListOrganization
from Organizations.schema.organization_schema import Organization


def organization_create_repo(db: Session, req: Organization):
    db.add(req)
    db.commit()
    db.refresh(req)
    return req


def organizations_read_repo(db: Session):
    return db.query(ListOrganization).all()
