from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models.catalogue import Model

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins = ["*"], allow_credentials = True, allow_methods = ["*"], allow_headers = ["*"])

class CatalogueModel(BaseModel):
    name: str
    description: str
    # price: float
    # is_offer: Union[bool, None] = None
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/models')
def models():
    models = Model.find_all()

    return models
@app.get('/catalogue')
def get_catalogues():
    return[{"name":"Yamaha R6"}]

@app.post('/catalogue')
def save_catalogue(data: CatalogueModel):
    print(data)