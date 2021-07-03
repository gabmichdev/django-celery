import time

from core.celery import app
from celery import shared_task


@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True


@app.task
def check():
    print("I am checking your stuff")
