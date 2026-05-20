from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# запасной список (если Google не ответит)
fallback_trends = [
    "iPhone 16 leak",
    "TikTok AI filter",
    "Messi news",
    "Instagram Reels update",
    "YouTube Shorts trend",
    "AI video generator",
    "ChatGPT update",
    "Viral dance challenge",
    "Netflix new series",
    "Gaming PC build trend"
]

@app.route("/")
def home():
    return "API is running"

@app.route("/api/trends")
def trends():

    # имитация "live trends"
    result = {"trends": []}

    shuffled = random.sample(fallback_trends, len(fallback_trends))

    for i, t in enumerate(shuffled[:10]):
        result["trends"].append({
            "title": t,
            "views": f"{random.randint(100, 900)}K+",
            "source": "live"
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run()
