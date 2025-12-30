from pydantic import BaseModel, Field
from typing import Optional

class TaskCreateDTO(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None


class TaskUpdateDTO(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    status: Optional[str] = Field(None, pattern="^(pending|in_progress|done)$")
