from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.models.database import Base


class LegitimateSeller(Base):
    __tablename__ = "legitimate_sellers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    site = Column(String(100), nullable=False)
    ssp_domain_name = Column(String(200), nullable=False)
    publisher_id = Column(String(200), nullable=False)
    relationship = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)
    run_id = Column(UUID(as_uuid=True), ForeignKey("tasks.run_id"), nullable=False)
