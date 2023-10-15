import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

celery = Celery("main")


celery.config_from_object("django.conf:settings", namespace="CELERY")

celery.autodiscover_tasks()

@celery.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
