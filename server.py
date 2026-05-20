from flask import Flask, jsonify
from flask_cors import CORS
from pytrends.request import TrendReq

app = Flask(__name__)
CORS(app)

pytrends = TrendReq(hl='en-US', tz=360)

@app.route("/api/trends")
def trends():
    data = pytrends.trending_searches(pn="united_states")

    result = {"trends": []}

    for i, row in data.head(10).iterrows():
        result["trends"].append({
            "title": str(row[0]),
            "views": "Google Trends"
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run()