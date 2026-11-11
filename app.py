from flask import Flask, request, render_template_string
import hashlib

app = Flask(__name__)

file_hashes = {}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>File Integrity Monitor</title>
    <style>
        body {
            font-family: Arial;
            margin: 40px;
            background: #f4f4f4;
        }
        .box {
            background: white;
            padding: 25px;
            border-radius: 10px;
        }
        button {
            padding: 10px 20px;
            background: #2563eb;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
<div class="box">
    <h1>File Integrity Monitor</h1>
    <h3>Upload a file to check its integrity</h3>

    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Check File</button>
    </form>

    <h3>Monitoring Results</h3>
    {% for item in results %}
        <p><b>File:</b> {{ item[0] }}</p>
        <p><b>SHA-256:</b> {{ item[1] }}</p>
        <p><b>Status:</b> {{ item[2] }}</p>
        <hr>
    {% endfor %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    results = []

    if request.method == "POST":
        uploaded_file = request.files.get("file")

        if uploaded_file:
            content = uploaded_file.read()
            name = uploaded_file.filename
            new_hash = hashlib.sha256(content).hexdigest()

            if name not in file_hashes:
                status = "NEW FILE"
            elif file_hashes[name] != new_hash:
                status = "FILE MODIFIED"
            else:
                status = "NO CHANGES"

            file_hashes[name] = new_hash
            results.append((name, new_hash, status))

    return render_template_string(HTML, results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
