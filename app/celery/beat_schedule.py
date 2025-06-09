from celery.schedules import crontab
from app.celery.celery_worker import celery_app


celery_app.conf.beat_schedule = {
    'run-daily-scheduler': {
        'task': 'app.celery.tasks.schedule_task',
        'schedule': crontab(hour=10, minute=0),  # every day at midnight
    },
    'run-5min-executor': {
        'task': 'app.celery.tasks.execute_tasks',
        'schedule': crontab(minute='*/5'),  # every 5 minutes
    },
}
celery_app.conf.timezone = 'UTC'