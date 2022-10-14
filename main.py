# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body 
from fastapi import Query

app = FastAPI() #Se crea una variable con esta instancia

# Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

# Request and Response Body

@app.get('/')
def home():
    return {'Hello': 'World'}

# Request and Response Body

@app.post('/person/new')
def create_person(person: Person = Body(...)): #los 3 puntos significa que es obligatorio
    return person

    # Validations: Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: Optional[str] = Query(...)
):
    return {name: age}

