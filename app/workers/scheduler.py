from apscheduler.schedulers.background import BackgroundScheduler
from app.services.digest_service import send

scheduler = BackgroundScheduler()

def job():
    top_docs = []  # fetch top Web3 docs from DB
    send(top_docs)

scheduler.add_job(job, "interval", hours=24)

def start():
    scheduler.start()