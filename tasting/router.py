from fastapi import APIRouter
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str
router = APIRouter()

todo_list = []
@router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    print(todo_list)
    return {"message": "Todo added successfully"}

@router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}
