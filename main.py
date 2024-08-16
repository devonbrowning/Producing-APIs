from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import random

app = FastAPI()
class Fact(BaseModel):
    id: int
    fact: str

facts: List[Fact] = [
    Fact(id=0, fact="Octopuses have three hearts."),
    Fact(id=1, fact="Honey never spoils."),
    Fact(id=2, fact="Gummy bears were originally called dancing bears."),
    Fact(id=3, fact="Comets in ancient Greece were called hairy stars.")
]


# End point to get a random fact
@app.get('/fact')
async def get_random_fact(id: int = None):
    if id is not None:
        for fact in facts:
            if fact.id == id:
                return fact
        return {'message': 'Fact not found'}
    return random.choice(facts)

# Endpoint to get specified fact by id
@app.get('/fact/{id}')
async def get_fact_by_id(id: int):
    for fact in facts:
        if fact.id == id:
            return fact
    return {'message': 'Fact not found'}

# add new fact
@app.post('/fact')
async def add_fact(new_fact: Fact):
    if any(fact.id == new_fact.id for fact in facts):
        return {'message': 'Fact with this id already exists'}
    facts.append(new_fact)
    return {'message': 'Fact added successfully', 'fact': new_fact}
