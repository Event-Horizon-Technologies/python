# main.py
from fastapi import FastAPI, Path
from pydantic import BaseModel
app = FastAPI()

class Benefit(BaseModel):
    title: str
    description: str

benefits = [
    {
        "title": "High performance",
        "description": "FastAPI is built on top of Starlette, providing high performance and asynchronous capabilities."
    },
    {
        "title": "Easy to use",
        "description": "FastAPI uses Python's type hints and decorators, making it intuitive and easy to learn."
    },
    {
        "title": "Automatic validation",
        "description": "FastAPI validates request and response data automatically using Pydantic."
    },
    {
        "title": "Interactive documentation",
        "description": "FastAPI generates interactive API documentation using OpenAPI and JSON Schema."
    }
]

@app.get("/")
def read_root():
    return {"Welcome": "This is a FastAPI showcase of its benefits"}

@app.get("/benefits/")
def get_benefits(skip: int = 0, limit: int = 10):
    return benefits[skip : skip + limit]

@app.get("/benefits/{benefit_id}", response_model=Benefit)
def get_benefit(benefit_id: int = Path(..., ge=0, le=len(benefits) - 1, description="The ID of the benefit to retrieve")):
    return benefits[benefit_id]

@app.post("/benefits/")
def add_benefit(benefit: Benefit):
    benefits.append(benefit)
    return {"status": "Benefit added", "benefit": benefit}
