from uuid import uuid4, UUID

from app.schemas.legitimate_sellers import LegitimateSellerSchema
from datetime import datetime


def parse_ads_txt(domain: str, content: str, run_id: UUID):
    sellers = []
    for line in content.splitlines():
        if line.startswith("#") or not line.strip():
            continue
        parts = [p.strip() for p in line.split(",")]
        if len(parts) >= 3:
            sellers.append(LegitimateSellerSchema(
                id=uuid4(),
                site=domain,
                ssp_domain_name=parts[0],
                publisher_id=parts[1],
                relationship=parts[2],
                date=datetime.now().date(),
                run_id=run_id
            ))
    print(f"Parsed {len(sellers)} sellers from {domain}")
    return sellers
