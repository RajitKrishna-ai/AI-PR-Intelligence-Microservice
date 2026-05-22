import requests
from app.core.config import SLACK_WEBHOOK

def send(top_docs):
    blocks = []

    for d in top_docs:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{d['title']}*\n{d['text'][:200]}"
            }
        })

    requests.post(SLACK_WEBHOOK, json={"blocks": blocks})
