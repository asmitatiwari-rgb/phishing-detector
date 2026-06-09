from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

model = joblib.load("phishing_model.pkl")

@app.route("/")
def home():
    return "🔥 AI Phishing Detection System Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data.get("URL", "")

    # simple rule-based logic (stable demo)
    url = url.lower()

    if "login" in url or "verify" in url or "bank" in url or "secure" in url:
        result = "Phishing ❌"
    else:
        result = "Safe ✅"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)