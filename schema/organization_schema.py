from pydantic import BaseModel


class Organization(BaseModel):
    name: str


class Organization_create(Organization):
    pass


class Organization_read(Organization):
    id: int
