from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "API is running"

@app.route("/api/trends")
def trends():

    trends_list = [
        "iPhone 16 leak",
        "TikTok AI filter",
        "Instagram Reels boost",
        "Messi injury update",
        "YouTube Shorts viral",
        "ChatGPT new update",
        "AI video generator",
        "Gaming setup trend",
        "Netflix new series",
        "Viral dance challenge"
    ]

    result = {"trends": []}

    shuffled = random.sample(trends_list, len(trends_list))

    for i, t in enumerate(shuffled[:10]):
        result["trends"].append({
            "title": t,
            "views": f"{random.randint(100,900)}K+",
            "source": "stable-api"
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run()
