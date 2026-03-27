from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import os

app = Flask(__name__)
CORS(app)

# 🧠 Function to clean notes
def clean_notes(text, mode="normal"):
    text = text.lower()

    # Split text into sentences/phrases
    sentences = re.split(r'[.?!,]', text)

    cleaned = ""

    for s in sentences:
        s = s.strip()
        if not s:
            continue

        words = s.split()

        # 📝 NORMAL MODE
        if mode == "normal":
            cleaned += f"✦ {s.capitalize()}<br>"

        # 📚 EXAM MODE
        elif mode == "exam":
            keywords = words[:5]
            cleaned += f"📌 {' '.join(keywords).capitalize()}<br>"

        # ✨ FUN MODE
        elif mode == "fun":
            title = words[0].capitalize() if words else ""
            rest = " ".join(words[1:])
            cleaned += f"🌟 <b>{title}</b>: {rest} 🚀<br>"

    return cleaned


# 🌐 API route
@app.route("/clean", methods=["POST"])
def clean():
    data = request.get_json()
    text = data.get("text", "")
    mode = data.get("mode", "normal")

    result = clean_notes(text, mode)

    return jsonify({"cleaned": result})

@app.route("/")
def home():
    return "Note Cleaner AI is running 🚀"


# 🚀 Run app (Render compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)