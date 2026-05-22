from fastapi import APIRouter
from app.db.sqlite import conn
from app.nlp.sentiment import analyze_sentiment
from app.nlp.topic import predict
from app.nlp.web3 import detect
from app.vector.embed import embed
from app.vector.index import add

router = APIRouter()

@router.post("/ingest")
def ingest(doc: dict):
    c = conn()
    cur = c.cursor()

    sentiment = analyze_sentiment(doc["text"])
    topic = "product"  # simplified for MVP
    entities = detect(doc["text"])
    vector = embed(doc["text"])

    cur.execute("""
    INSERT OR REPLACE INTO docs VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        doc["id"], doc["title"], doc["text"],
        doc["source"], doc["published_at"],
        doc.get("reach", 0),
        sentiment["label"], topic
    ))

    c.commit()
    c.close()

    add(doc["id"], vector)

    return {
        "status": "ok",
        "sentiment": sentiment,
        "topic": topic,
        "entities": entities
    }