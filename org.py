import uvicorn
from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel

app = FastAPI()


class ID(BaseModel):
  id: int


organization_data = {
  1: "Collance",
  2: "CCMG"
}


@app.post("/Organization")
def organization_name(id: ID) -> Dict:
  org_name = organization_data.get(id.id, "org not found")
  return {"data": org_name}


@app.get("/Organizations")
def organizations() -> Dict:
  return organization_data


if __name__ == '__main__':
  uvicorn.run(app)