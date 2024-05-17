import uvicorn
from fastapi import FastAPI, Depends
from sqlmodel import Session
from Organizations import model
from Organizations.database import Base, engine, SessionLocal, get_db
from Organizations.schema.organization_schema import Organization_create
from Organizations.service import organization_service

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/Organization")
def organization_name(org: Organization_create, db: Session = Depends(get_db)):
    return organization_service.organizations_create_service(db, org.name)


@app.get("/Organizations")
def organizations(db: Session = Depends(get_db)):
    return organization_service.organization_read_service(db)


if __name__ == '__main__':
    uvicorn.run(app)
