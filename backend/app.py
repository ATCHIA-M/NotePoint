from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import os

app = Flask(__name__)
CORS(app)

def clean_notes(text, mode="normal"):
    text = text.lower()

    # Better sentence splitting
    sentences = re.split(r'[.?!,\n]', text)

    cleaned = ""

    # Common useless words to ignore
    stopwords = {"is", "the", "in", "of", "and", "to", "a", "for", "on"}

    for s in sentences:
        s = s.strip()
        if not s:
            continue

        words = s.split()

        # 📝 NORMAL MODE (clean + readable)
        if mode == "normal":
            cleaned += f"✦ {s.capitalize()}<br>"

        # 📚 EXAM MODE (SMART KEYWORDS)
        elif mode == "exam":
            keywords = [w for w in words if w not in stopwords]
            keywords = keywords[:5]

            if keywords:
                cleaned += f"📌 {' | '.join(keywords).capitalize()}<br>"

        # ✨ FUN MODE (structured + styled)
        elif mode == "fun":
            if len(words) > 4:
                title = " ".join(words[:2]).capitalize()
                rest = " ".join(words[2:])
                cleaned += f"🌟 <b>{title}</b><br>➤ {rest.capitalize()}<br><br>"
            else:
                cleaned += f"✨ {s.capitalize()}<br>"

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