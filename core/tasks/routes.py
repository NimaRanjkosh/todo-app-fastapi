from fastapi import APIRouter

router = APIRouter(tags=["tasks"], prefix="/todo")

@router.get("/tasks")
async def retrieve_tasks_lists():
    return []

@router.get("/tasks/{task_id}")
async def retrieve_tasks_lists(task_id: int):
    return []
