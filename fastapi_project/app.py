# this is the basic fastapi project that contains basic code for crud operations
# and also contains the code for the basic authentication using jwt token

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import UUID,uuid4

app = FastAPI()

class Task(BaseModel):
    id: Optional[UUID]=None
    title: str
    description: Optional[str]=None
    completed: bool=False

Tasks = []

# endpoints to create a task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task.id = uuid4()
    Tasks.append(task)
    return task

# end point to get all the tasks
@app.get("/tasks/", response_model=list[Task])
def read_tasks():
    return Tasks

# endpoint to get a specific or path parameter task
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: UUID):
    for task in Tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, task_update: Task):
    for idx,task in enumerate(Tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            Tasks[idx] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: UUID):
    for idx,task in enumerate(Tasks):
        if task.id == task_id:
            return Tasks.pop(idx)
        
    raise HTTPException(status_code=404, detail="Task not found")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)


# Now run the main.py file using the below command and also you use docs and redocs to see the api documentation it will link you to swagger ui and redoc ui. plus you can also use the postman to test the api.to do this do : "http://http://127.0.0.1:8000/docs" and "http://127.0.0.1:8000/redoc" in the browser.
