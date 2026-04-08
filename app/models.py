from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    title: str
    description: Optional[str] = None

class TaskResponse(Task):
    id: int
    completed: bool