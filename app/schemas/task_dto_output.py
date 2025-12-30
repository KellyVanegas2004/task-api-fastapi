from pydantic import BaseModel
from datetime import datetime

class TaskResponseDTO(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
