from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
from uuid import UUID


class TaskSchema(BaseModel):
    run_id: UUID
    date: date
    status: str
    error: str | None = None
    started_at: datetime | None = None
    finished_at: datetime | None = None
    failed_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
