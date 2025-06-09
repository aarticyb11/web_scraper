from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from app.models.database import get_db
from app.models.task import Task
from app.schemas.task import TaskSchema

router = APIRouter()


@router.get("/tasks", response_model=dict)
def get_tasks(
    page: int = Query(1, ge=1, description="Page number (starts at 1)"),
    page_size: int = Query(10, ge=1, le=100, description="Number of items per page"),
    date_filter: Optional[date] = Query(None, alias="date"),
    db: Session = Depends(get_db)
):
    """
    Get tasks with optional date filter.

    - `GET /tasks` returns all paginated tasks.
    - `GET /tasks?date=YYYY-MM-DD` filters tasks by that date.

    Returns paginated tasks or tasks filtered by date.
    Pagination:
        - `page`: The page number (default is 1).
        - `page_size`: The number of records per page (default is 10, max is 100).
    """
    query = db.query(Task)
    if date_filter:
        query = query.filter(Task.date == date_filter)

    total_tasks = query.count()
    tasks = query.offset((page - 1) * page_size).limit(page_size).all()

    return {
        "total": total_tasks,
        "page": page,
        "page_size": page_size,
        "tasks": [TaskSchema.model_validate(task) for task in tasks]
    }


@router.get("/stats")
def get_average_execution_time(
    from_date: date = Query(..., alias="from"),
    to_date: date = Query(..., alias="to"),
    db: Session = Depends(get_db)
):
    if from_date > to_date:
        raise HTTPException(status_code=400, detail="from date must be <= to date")

    tasks = db.query(Task).filter(Task.date.between(from_date, to_date)).all()

    total_duration = 0
    count = 0
    for task in tasks:
        if task.started_at and task.finished_at:
            total_duration += (task.finished_at - task.started_at).total_seconds()
            count += 1

    avg_duration = total_duration / count if count > 0 else 0
    return {"average_execution_time_seconds": avg_duration}