import os
from typing import Union
from collections import OrderedDict
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import requests
from urllib.parse import urlencode

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_NEARBY_API_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?";
GOOGLE_DISTANCE_API_URL = "https://maps.googleapis.com/maps/api/distancematrix/json?"

app = FastAPI()

origins = [
    "https://nomorehumor.github.io/City-Navigator/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/nearby")
def get_nearby(location: str, rankby:str, type: str):
    query = urlencode(OrderedDict(key=GOOGLE_API_KEY, location=location, rankby=rankby, type=type))
    request = GOOGLE_NEARBY_API_URL + query
    response = requests.get(request)
    print("Query:", request)
    print("Response:", response.json())
    return response.json()

    
@app.get("/distance")
def get_distance(destinations: str, origins:str, mode: str):
    query = urlencode(OrderedDict(key=GOOGLE_API_KEY, destinations=destinations, origins=origins, mode=mode))
    request = GOOGLE_DISTANCE_API_URL + query
    response = requests.get(request)
    print("Query:", request)
    print("Response:", response.json())
    return response.json()