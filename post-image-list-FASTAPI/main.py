# ????server
# uvicorn main:app --reload --port 8888
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from PIL import Image
import numpy as np

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list = []

class Item2(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/sys/sinoma/v1/optimization/predict/fcao")
async def create_item(item: Item):
    data = np.uint8(np.array(item.tags))
    img = Image.fromarray(data, 'L')
    img.save('my.jpg')
    img.show()
    return {"Predict":"AngelaBaby"}

