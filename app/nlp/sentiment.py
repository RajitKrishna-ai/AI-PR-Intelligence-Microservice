from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(text: str):
    res = sentiment_model(text[:512])[0]
    return {
        "label": res["label"],
        "score": float(res["score"])
    }