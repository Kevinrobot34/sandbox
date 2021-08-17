import os

import requests

SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']


def post_message(notification_text: dict):
    res = requests.post(SLACK_WEBHOOK_URL,
                        headers={'Content-type': 'application/json'},
                        json=notification_text)
    if res.ok:
        print('Succeeded to post messages')
    else:
        print('something wrong in post message')
        print(res)


def handler(event, context):
    # send notification
    notification_text = {
        'text': 'test sandbox_container_lambda',
        'username': 'sandbox_container_lambda',
        'icon_emoji': ':package:',
    }
    post_message(notification_text)

    result = {'statusCode': 200, 'body': 'Done'}
    return result
