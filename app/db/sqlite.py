import sqlite3
from app.core.config import DB_PATH

def conn():
    return sqlite3.connect(DB_PATH)

def init():
    c = conn()
    cur = c.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS docs (
        id TEXT PRIMARY KEY,
        title TEXT,
        text TEXT,
        source TEXT,
        published_at TEXT,
        reach INTEGER,
        sentiment TEXT,
        topic TEXT
    )
    """)

    c.commit()
    c.close()