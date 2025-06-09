import uuid
from sqlalchemy import Column, Date, Enum, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.models.database import Base


class Task(Base):
    __tablename__ = "tasks"

    run_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(Enum("SCHEDULED", "STARTED", "FAILED", "FINISHED", name="status_enum"), nullable=False)
    error = Column(Text, nullable=True)
    started_at = Column(DateTime, nullable=True)
    finished_at = Column(DateTime, nullable=True)
    failed_at = Column(DateTime, nullable=True)
