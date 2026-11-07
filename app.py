from flask import Flask, render_template_string
import os
import hashlib

app = Flask(__name__)

folder = "."

def get_hash(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

@app.route("/")
def home():
    files = []

    if os.path.exists(folder):
        for name in os.listdir(folder):
            path = os.path.join(folder, name)

            if os.path.isfile(path):
                files.append({
                    "name": name,
                    "hash": get_hash(path)
                })

    return render_template_string("""
    <h1>File Integrity Monitor</h1>
    <h3>Monitored Files</h3>
    {% for file in files %}
        <p><b>File:</b> {{ file.name }}</p>
        <p><b>SHA-256:</b> {{ file.hash }}</p>
        <hr>
    {% endfor %}
    """, files=files)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
