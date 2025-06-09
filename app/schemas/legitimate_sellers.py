from pydantic import BaseModel, ConfigDict
from datetime import date
from uuid import UUID


class LegitimateSellerSchema(BaseModel):
    id: UUID
    site: str
    ssp_domain_name: str
    publisher_id: str
    relationship: str
    date: date
    run_id: UUID

    model_config = ConfigDict(from_attributes=True)
