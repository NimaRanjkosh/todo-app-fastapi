from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TaskBaseSchema(BaseModel):
    title: str = Field(..., max_length=50, description="Title of the task")
    description: Optional[str] = Field(
        None, max_length=500, description="Description of the task"
    )
    status_id: int = Field(1, description="FK of taskstatus.id", gt=0)
    is_completed: bool = Field(default=0, description="Task completion flag")


class TaskCreateSchema(TaskBaseSchema):
    pass


class TaskUpdateSchema(TaskBaseSchema):
    pass


class TaskResponseSchema(TaskBaseSchema):
    id: int = Field(..., description="ID of the task")
    created_date: datetime = Field(..., description="Creation date of the task")
    updated_date: datetime = Field(..., description="Updating date of the task")
