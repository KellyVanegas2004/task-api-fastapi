from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task_dto_input import TaskCreateDTO, TaskUpdateDTO


def create_task(db: Session, dto: TaskCreateDTO) -> Task:
    task = Task(**dto.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task(db: Session, task_id: int) -> Task | None:
    return db.query(Task).filter(Task.id == task_id).first()


def list_tasks(db: Session, page: int, page_size: int):
    offset = (page - 1) * page_size
    return (
        db.query(Task)
        .order_by(Task.created_at.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )


def update_task(db: Session, task: Task, dto: TaskUpdateDTO) -> Task:
    for key, value in dto.model_dump(exclude_unset=True).items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task):
    db.delete(task)
    db.commit()
