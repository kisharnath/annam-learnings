from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.get("/")
def greetings():
    return {
        "message":"Hello, World!"
    }
@app.get("/greet/{name}")
def greet_name(name:str):
    return {
        "message": f"Hello, {name}!"
    }
#Query parameters
@app.get("/greet_details/{name}")
def greet_query(name:str, age:int, city:str):
    return {
        "message": f"Hello, {name}! You are {age} years old and live in {city}."
    }

@app.post("/items/")
def create_item(item: Item):
    return item