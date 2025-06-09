from fastapi import FastAPI
from app.routes.task import router as tasks_router
from app.routes.legitimate_sellers import router as legitimate_sellers_router

app = FastAPI()

# Include routers
app.include_router(tasks_router, prefix="/api", tags=["Tasks"])
app.include_router(legitimate_sellers_router, prefix="/api", tags=["Legitimate Sellers"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Ads.txt Scraper API"}
