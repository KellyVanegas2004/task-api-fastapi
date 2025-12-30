from sqlalchemy import Column, Integer, String, Text, DateTime, Enum
from sqlalchemy.sql import func
from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    status = Column(
        Enum("pending", "in_progress", "done", name="task_status"),
        nullable=False,
        default="pending",
        index=True,
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())
