import os
import time

import requests
from celery import Celery


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# you can change the name here
app = Celery('core_drf')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# discover and load tasks.py from from all registered Django apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Hello!")
    time.sleep(10)
    token = os.getenv("TELEGRAM_BOT_TOKEN", "telegram_token_here")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.get(
        url,
        params={
            # example (int) chat id
            "chat_id": 803431360,
            "text": "test test test drf django celery"
        }
    )
    print(f'Request: {self.request!r}')
