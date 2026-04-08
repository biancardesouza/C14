from app.database import tasks_db, task_id_counter

def get_all_tasks():
    return tasks_db

def create_task(task):
    global task_id_counter

    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "description": task.description,
        "completed": False
    }

    tasks_db.append(new_task)
    task_id_counter += 1

    return new_task

def get_task_by_id(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    return None

def update_task(task_id: int, updated_data):
    task = get_task_by_id(task_id)
    if not task:
        return None

    task["title"] = updated_data.title
    task["description"] = updated_data.description
    return task

def delete_task(task_id: int):
    global tasks_db
    task = get_task_by_id(task_id)

    if not task:
        return False

    tasks_db = [t for t in tasks_db if t["id"] != task_id]
    return True

def mark_as_completed(task_id: int):
    task = get_task_by_id(task_id)

    if not task:
        return None

    task["completed"] = True
    return task