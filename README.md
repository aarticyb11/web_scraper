# 🕷️ FastAPI Web Scraper with Celery & Redis

This project is a web scraping system built with **FastAPI**, **Celery**, and **Redis**. It periodically fetches `ads.txt` files from configured websites, parses the content, and stores validated data into a database using Pydantic models.
---

## 📦 Features

- Scheduled scraping of `ads.txt` from multiple websites
- Celery workers with periodic task execution
- PostgreSQL-based task tracking with statuses like `SCHEDULED`, `STARTED`, `FAILED`, `FINISHED`
- JSON-based domain configuration
- Graceful error handling for fetch and parse failures

---
## 🚀 Getting Started
### Setup Instructions

## Prerequisites
1. Python 3.11+
2. PostgreSQL installed locally
3. Redis for Celery task queue

## Installation
### 1. Clone the Repo
```bash
git clone https://github.com/your-org/web_scraper.git
cd web_scraper
```

### 2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:
pip install -r requirements.txt

### 4. Set up the database:
1. Create a PostgreSQL database named web_scraper.
   1. Start the PostgreSQL service:
        sudo service postgresql start
   2. Log in to the PostgreSQL prompt as the default user (postgres):
        sudo -u postgres psql
   3. Create a new database:
        CREATE DATABASE web_scraper;
   4. Create a user with a password:
        CREATE USER web_user WITH PASSWORD 'secure_password';
   5. Grant privileges to the user on the database:
        GRANT ALL PRIVILEGES ON DATABASE web_scraper TO web_user;
   6. Exit the PostgreSQL prompt:
        \q


2. Apply migrations:
   ```bash
        alembic upgrade head
   ```
    ## If you dont have migration file then run following command
        1. alembic init alembic
        2. alembic revision --autogenerate -m "Initial migration"
        3. alembic upgrade head       

### 5. Configure environment variables:
1. Create a .env file in the project root with the following content:
    1. DATABASE_URL=postgresql+psycopg2://<user>:<password>@localhost:5432/web_scraper
    2. REDIS_URL=redis://localhost:6379/0

### 6. Run the Celery worker:
    celery -A app.celery.celery_worker.celery_app worker --loglevel=info

### 7. Run the Celery beat:
    celery -A app.celery.celery_worker.celery_app beat --loglevel=info

### 8. Start the FastAPI server:
    uvicorn app.main:app --reload

# Usage
## Access the API
### After starting the server, the API can be accessed at:
    Base URL: http://127.0.0.1:8000

    Example Endpoints
    1. Get all tasks:
        GET /api/tasks

    2. Get tasks by date:
        GET /api/tasks?date=YYYY-MM-DD

    3. Get legitimate sellers for a domain:
        GET /api/legitimate_sellers?domain=example.com

    4. Get task statistics:
        GET /api/stats?from=YYYY-MM-DD&to=YYYY-MM-DD


Documentation
Interactive API documentation is available at:
Swagger UI: http://127.0.0.1:8000/docs





