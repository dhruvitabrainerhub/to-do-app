from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

db : list[Todo] = []

@app.get("/")
async def read_root():
    return {"message":"Todo API Running..."}

@app.get("/todos",response_model = List[Todo])
async def get_todos():
    return db

@app.post("/todos", response_model = Todo)
async def create_todos(todo : Todo):
    db.append(todo)
    return todo

@app.delete("/todos/{todo_id}")
async def delete_todos(todo_id : int):
    global db
    db = [t for t in db if t.id != todo_id]
    return {"message" : "Todo deleted"}