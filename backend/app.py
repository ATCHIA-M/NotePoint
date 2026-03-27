from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import os

app = Flask(__name__)
CORS(app)

def clean_notes(text, mode="normal"):
    text = text.lower()
    sentences = re.split(r'[.?!]', text)

    cleaned = ""

    for s in sentences:
        s = s.strip()
        if not s:
            continue

        words = s.split()

        if mode == "normal":
            cleaned += f"✦ {s.capitalize()}<br>"

        elif mode == "exam":
            keywords = words[:5]
            cleaned += f"📌 {' | '.join(keywords).capitalize()}<br>"

        elif mode == "fun":
            cleaned += f"✨ • {s.capitalize()}<br>"

    return cleaned

@app.route("/")
def home():
    return "Note Cleaner AI is running 🚀"

@app.route("/clean", methods=["POST"])
def clean():
    data = request.get_json()
    text = data.get("text", "")
    mode = data.get("mode", "normal")

    result = clean_notes(text, mode)

    return jsonify({"cleaned": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)