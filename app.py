from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.catalogue import Catalogue

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/catalogues")
async def get_catalogues():
    cards = Catalogue.get_all()
    return {"catalogues": [card.to_dict() for card in cards]}