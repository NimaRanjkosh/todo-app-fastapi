from fastapi import APIRouter, Depends, HTTPException, status
from tasks.schemas import (
    TaskCreateSchema,
    TaskUpdateSchema,
    TaskResponseSchema,
)
from tasks.models import TaskModel
from sqlalchemy.orm import Session
from core.database import get_db
from typing import List


router = APIRouter()


@router.get(
    "/tasks", response_model=List[TaskResponseSchema], status_code=status.HTTP_200_OK
)
async def retrieve_tasks_lists(
    db: Session = Depends(get_db),
):
    results = db.query(TaskModel).all()
    return results


@router.get(
    "/tasks/{task_id}",
    response_model=TaskResponseSchema,
    status_code=status.HTTP_200_OK,
)
async def retrieve_tasks_by_id(task_id: int, db: Session = Depends(get_db)):
    result = db.query(TaskModel).where(TaskModel.id == task_id).one_or_none()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"task_id: {task_id} not exists",
        )
    else:
        return result


@router.post(
    "/tasks", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED
)
async def create_task(
    new_task: TaskCreateSchema,
    db: Session = Depends(get_db),
):
    new_task = TaskModel(**new_task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.put(
    "/tasks/{task_id}",
    response_model=TaskResponseSchema,
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_task_by_id(
    task_id: int,
    desired_task: TaskUpdateSchema,
    db: Session = Depends(get_db),
):
    fetched_task = db.query(TaskModel).where(TaskModel.id == task_id).one_or_none()
    if fetched_task:
        fetched_task.title = desired_task.title
        fetched_task.description = desired_task.description
        fetched_task.status_id = desired_task.status_id
        fetched_task.is_completed = desired_task.is_completed
        db.commit()
        db.refresh(fetched_task)
        return fetched_task
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"task_id: {task_id} not exists",
        )


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task_by_id(
    task_id: int,
    db: Session = Depends(get_db),
):
    fetched_task = db.query(TaskModel).where(TaskModel.id == task_id).one_or_none()
    if not fetched_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"task_id: {task_id} not exists",
        )
    db.delete(fetched_task)
    db.commit()
    return
