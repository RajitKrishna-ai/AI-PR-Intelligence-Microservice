from fastapi import FastAPI
from app.db.sqlite import init
from app.api import ingest, search, health

app = FastAPI()

init()

app.include_router(ingest.router)
app.include_router(search.router)
app.include_router(health.router)

@app.get("/")
def home():
    return {"status": "AI PR Intelligence Running"}