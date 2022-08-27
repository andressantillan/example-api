from typing import Union

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
baseUrl = "/api"

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get(baseUrl)
def root():
    return {"Hello":"world"}

@app.get(baseUrl + "/items/{item_id}")
def read_item(item_id: int, q: Union[str, None]=None):
    return {"item_id": item_id, "q": q}

@app.put(baseUrl + "/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

    