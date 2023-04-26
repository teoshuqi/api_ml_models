from celery import Celery
import os

worker = Celery(
    "worker",
    backend=os.getenv("CELERY_BACKEND_URL"),
    broker=os.getenv("CELERY_BROKER_URL"),
    include=["fast-api-celery.worker.tasks", "fast-api-celery.logic"],
)

# Optional configuration, see the application user guide.
worker.conf.update(
    result_expires=3600,
    task_track_started=True,
    result_backend='redis'
)

if __name__ == "__main__":
    worker.start()
