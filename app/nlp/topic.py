from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

TOPICS = ["product", "funding", "partnership", "thought_leadership", "crisis"]

def train(X, y):
    vec = TfidfVectorizer(max_features=5000)
    model = LogisticRegression()

    Xv = vec.fit_transform(X)
    model.fit(Xv, y)

    joblib.dump((vec, model), "topic.pkl")


def load():
    return joblib.load("topic.pkl")


def predict(text, vec, model):
    return model.predict(vec.transform([text]))[0]