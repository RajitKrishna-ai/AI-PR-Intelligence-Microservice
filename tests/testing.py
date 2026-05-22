def test_ingest():
    res = ingest({
        "id": "1",
        "title": "testing our AI_PRIntelligence",
        "text": "ETH wallet 0x123...",
        "source": "x",
        "published_at": "2026"
    })
    assert "status" in res