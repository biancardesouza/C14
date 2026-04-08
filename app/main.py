from fastapi import FastAPI, HTTPException
from app.models import Task
from app import service

app = FastAPI(title="To-Do API")

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/tasks")
def get_tasks():
    return service.get_all_tasks()

@app.post("/tasks")
def create_task(task: Task):
    return service.create_task(task)

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = service.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    task = service.update_task(task_id, updated_task)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    success = service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"message": "Task deleted"}

@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    task = service.mark_as_completed(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task