# -*- coding: utf-8 -*-

import requests
from settings import mailgun_api_key, from_email, to_email, bot_url


def send_email_notifications(message):
    return requests.post(
        "https://api.mailgun.net/v3/XXXXXX/messages",
        auth=("api", mailgun_api_key),
        data={"from": from_email,
              "to": to_email,
              "subject": "Service Alert",
              "html": message})


def send_telegram_notifications(message):
    return requests.post(bot_url, data={'message': message})


def send_notifications(message):
    send_email_notifications(message=message)
    send_telegram_notifications(message=message)

    # send over SMS, webhook
