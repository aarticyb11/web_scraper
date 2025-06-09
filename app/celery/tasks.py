import json
import uuid
import requests
from datetime import datetime
from app.celery.celery_worker import celery_app
from app.services.scraper import parse_ads_txt
from app.models.database import SessionLocal
from app.models.task import Task
from app.models.legitimate_sellers import LegitimateSeller


@celery_app.task
def schedule_task():
    session = SessionLocal()
    run_id = str(uuid.uuid4())
    task = Task(run_id=run_id, date=datetime.now().date(), status="SCHEDULED")
    session.add(task)
    session.commit()
    session.close()


@celery_app.task
def execute_tasks():
    db = SessionLocal()
    task = db.query(Task).filter(Task.status == "SCHEDULED").first()
    if task:
        print(f"Status task: {task.status}")
        print(f"Found scheduled task: {task.run_id}")
        task.status = "STARTED"
        task.started_at = datetime.now()
        db.commit()

        try:
            with open("sites.json") as f:
                domains = json.load(f)["sites"]

            for domain in domains:
                try:
                    print(f"Fetching ads.txt from {domain}")
                    response = requests.get(f"https://{domain}/ads.txt", timeout=10)
                    if response.status_code == 200:
                        sellers = parse_ads_txt(domain, response.text, task.run_id)
                        for seller in sellers:
                            db.add(LegitimateSeller(**seller.dict()))
                        db.commit()
                    else:
                        print(f"Failed to fetch ads.txt from {domain}: Status {response.status_code}")
                except Exception as e:
                    print(f"Error fetching from {domain}: {e}")
                    continue  # Skip to next domain on failure

            task.status = "FINISHED"
            task.finished_at = datetime.now()
        except Exception as e:
            task.status = "FAILED"
            task.error = str(e)
            task.failed_at = datetime.now()
            print(f"Executor failed: {e}")
        finally:
            db.commit()
    else:
        print("No scheduled task found.")
    db.close()

