from fastapi import APIRouter
from app.vector.embed import embed
from app.vector.index import search
from app.db.sqlite import conn

router = APIRouter()

@router.get("/search")
def search_api(query: str, k: int = 5):

    vec = embed(query)
    ids = search(vec, k)

    c = conn()
    cur = c.cursor()

    results = []

    for i in ids:
        cur.execute("SELECT * FROM docs LIMIT 1 OFFSET ?", (int(i),))
        row = cur.fetchone()
        if row:
            results.append(dict(row))

    return {"results": results}