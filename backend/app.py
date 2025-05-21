import os
from flask import Flask, request, jsonify
from model import predict_movie
from flask_cors import CORS
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
CORS(app)  # ✅ This allows requests from the browser

print("IMGBB Key:", os.getenv("IMGBB_API_KEY"))


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Save uploaded file temporarily
    file_path = "uploads/" + file.filename
    file.save(file_path)

    # Simulate prediction
    prediction = predict_movie(file_path)

    return jsonify({"title": prediction})

if __name__ == "__main__":
    app.run(debug=True)
