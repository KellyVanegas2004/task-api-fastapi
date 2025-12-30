from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class TaskBaseDTO(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending


class TaskCreateDTO(TaskBaseDTO):
    pass


class TaskUpdateDTO(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    status: Optional[TaskStatus] = None


class TaskResponseDTO(TaskBaseDTO):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
