from celery import Celery
from app.config import settings

celery_app = Celery(
    "worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

celery_app.conf.timezone = 'UTC'

import app.celery.tasks
import app.celery.beat_schedule