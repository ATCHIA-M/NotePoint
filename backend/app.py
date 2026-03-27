from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)


def clean_notes(text, mode):
    import re

    # 1. Clean spaces
    text = re.sub(r'\s+', ' ', text.strip())

    # 2. Try splitting using punctuation first
    sentences = re.split(r'[.?!]', text)

    # 3. If no proper sentences → smart chunking
    if len(sentences) <= 1:
        words = text.split()
        sentences = []

        temp = []
        for w in words:
            temp.append(w)

            # break at meaningful length AND avoid bad endings
            if len(temp) >= 8 and w not in ["in", "on", "of", "and", "to"]:
                sentences.append(" ".join(temp))
                temp = []

        if temp:
            sentences.append(" ".join(temp))

    cleaned = ""

    for s in sentences:
        s = s.strip()
        if len(s) < 3:
            continue

        words = s.split()

        # 📝 NORMAL MODE
        if mode == "normal":
            if mode == "normal":
                cleaned += f"✦ {s.capitalize()}<br>"

        # 📚 EXAM MODE (keywords only)
        elif mode == "exam":
            keywords = [w for w in words if len(w) > 4]
            cleaned += f"📌 {' | '.join(keywords[:4]).capitalize()}<br>"

        # ✨ FUN MODE
        elif mode == "fun":
            title = words[0].capitalize()
            rest = " ".join(words[1:])
            cleaned += f"🌟 <b>{title}</b>: {rest} 🚀<br>"

    return cleaned


@app.route('/clean', methods=['POST'])
def clean():
    data = request.json
    text = data['text']
    mode = data.get("mode", "normal")

    result = clean_notes(text, mode)

    return jsonify({"cleaned": result})


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
=======
from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)


def clean_notes(text, mode):
    import re

    # 1. Clean spaces
    text = re.sub(r'\s+', ' ', text.strip())

    # 2. Try splitting using punctuation first
    sentences = re.split(r'[.?!]', text)

    # 3. If no proper sentences → smart chunking
    if len(sentences) <= 1:
        words = text.split()
        sentences = []

        temp = []
        for w in words:
            temp.append(w)

            # break at meaningful length AND avoid bad endings
            if len(temp) >= 8 and w not in ["in", "on", "of", "and", "to"]:
                sentences.append(" ".join(temp))
                temp = []

        if temp:
            sentences.append(" ".join(temp))

    cleaned = ""

    for s in sentences:
        s = s.strip()
        if len(s) < 3:
            continue

        words = s.split()

        # 📝 NORMAL MODE
        if mode == "normal":
            if mode == "normal":
                cleaned += f"✦ {s.capitalize()}<br>"

        # 📚 EXAM MODE (keywords only)
        elif mode == "exam":
            keywords = [w for w in words if len(w) > 4]
            cleaned += f"📌 {' | '.join(keywords[:4]).capitalize()}<br>"

        # ✨ FUN MODE
        elif mode == "fun":
            title = words[0].capitalize()
            rest = " ".join(words[1:])
            cleaned += f"🌟 <b>{title}</b>: {rest} 🚀<br>"

    return cleaned


@app.route('/clean', methods=['POST'])
def clean():
    data = request.json
    text = data['text']
    mode = data.get("mode", "normal")

    result = clean_notes(text, mode)

    return jsonify({"cleaned": result})


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

