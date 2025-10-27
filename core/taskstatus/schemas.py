from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TaskStatusBaseSchema(BaseModel):
    description : str = Field(..., description="Description of the task")

class TaskStatusCreateSchema(TaskStatusBaseSchema):
    pass

class TaskStatusUpdateSchema(TaskStatusBaseSchema):
    pass

class TaskStatusResponseSchema(TaskStatusBaseSchema):
    id : int = Field(..., description="ID of the task status")
    
    created_date : datetime = Field(..., description="Creation date of the task")
    updated_date : datetime = Field(..., description="Updating date of the task")