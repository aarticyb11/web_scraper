from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.models.legitimate_sellers import LegitimateSeller
from app.schemas.legitimate_sellers import LegitimateSellerSchema

router = APIRouter()

@router.get("/legitimate_sellers", response_model=dict)
def get_legitimate_sellers(
    domain: str = Query(..., alias="domain"),
    page: int = Query(1, ge=1, description="Page number (starts at 1)"),
    page_size: int = Query(10, ge=1, le=100, description="Number of items per page"),
    db: Session = Depends(get_db)
):
    """
    Returns legitimate sellers for a given domain with pagination.

    Parameters:
    - `domain`: The domain to filter legitimate sellers.
    - `page`: The current page number (default is 1).
    - `page_size`: The number of items per page (default is 10, max is 100).
    """
    query = db.query(LegitimateSeller).filter(LegitimateSeller.site == domain)
    total_sellers = query.count()

    if total_sellers == 0:
        raise HTTPException(status_code=404, detail="No legitimate sellers found for this domain.")

    sellers = query.offset((page - 1) * page_size).limit(page_size).all()

    return {
        "total": total_sellers,
        "page": page,
        "page_size": page_size,
        "sellers": [LegitimateSellerSchema.model_validate(seller) for seller in sellers],  # Parse sellers into Pydantic models
    }
