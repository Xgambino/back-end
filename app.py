from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.catalogue import Catalogue
from models.motorcycle_offer import MotorcycleOffer
from models.motorcycle_events import MotorcycleEvent

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

@app.get("/motorcycle_offers")
async def get_motorcycle_offers():
    motorcycle_offers = MotorcycleOffer.get_all()
    return {"motorcycle_offers": [motorcycle_offer.to_dict() for motorcycle_offer in motorcycle_offers]}
@app.get("/motorcycle_events")
async def get_motorcycle_events():
    motorcycle_events = MotorcycleEvent.get_all()
    return [motorcycle_event.to_dict() for motorcycle_event in motorcycle_events]