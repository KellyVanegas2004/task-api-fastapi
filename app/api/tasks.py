from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.core.auth import get_current_user
from app.services import task_service
from app.schemas.task_dto_input import TaskCreateDTO, TaskUpdateDTO
from app.schemas.task_dto_output import TaskResponseDTO

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
    dependencies=[Depends(get_current_user)],
)


@router.post("/", response_model=TaskResponseDTO, status_code=status.HTTP_201_CREATED)
def create_task(dto: TaskCreateDTO, db: Session = Depends(get_db)):
    return task_service.create_task(db, dto)


@router.get("/", response_model=List[TaskResponseDTO])
def list_tasks(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
):
    return task_service.list_tasks(db, page, page_size)


@router.get("/{task_id}", response_model=TaskResponseDTO)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskResponseDTO)
def update_task(
    task_id: int,
    dto: TaskUpdateDTO,
    db: Session = Depends(get_db),
):
    task = task_service.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_service.update_task(db, task, dto)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task_service.delete_task(db, task)
