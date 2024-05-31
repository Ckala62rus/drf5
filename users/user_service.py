import os
import time

import requests
from celery import shared_task
from core.celery import app


@app.task
def email_notification(message: str, email: str):
    time.sleep(10)
    token = os.getenv("TELEGRAM_BOT_TOKEN", "telegram_token_here")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.get(
        url,
        params={
            # example (int) chat id
            "chat_id": 803431360,
            "text": "send some text"
        }
    )
