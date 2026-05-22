from app.core.config import OPENAI_API_KEY
import requests

def summarize(text: str) -> str:
    """
    Returns 2-3 sentence summary under 350 chars.
    Falls back safely if my API key is missing/wrong.
    """

    if not OPENAI_API_KEY:
        return text[:200] + "..."

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "user",
                        "content": f"Summarize this in 2-3 sentences under 350 characters:\n\n{text}"
                    }
                ]
            },
            timeout=10
        )

        result = response.json()
        return result["choices"][0]["message"]["content"][:350]

    except Exception:
        return text[:200] + "..."