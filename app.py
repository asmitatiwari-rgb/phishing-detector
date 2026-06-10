from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import render_template
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

model = joblib.load("phishing_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

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
   app.run(debug=True, host="0.0.0.0", port=5000)