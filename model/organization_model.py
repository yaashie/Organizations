from sqlalchemy import Column, Integer, String

from Organizations.database import Base


class ListOrganization(Base):
    __tablename__ = "List_Organizations"

    id = Column(Integer, primary_key=True)
    name = Column(String)
