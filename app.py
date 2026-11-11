from flask import Flask, request, render_template_string, session
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "file-monitor-secret-key")

app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


def get_hash(file):
    return hashlib.sha256(file.read()).hexdigest()


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>File Integrity Monitor</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #eef2f7;
            color: #1e293b;
        }

        header {
            background: #101827;
            color: white;
            padding: 25px 8%;
        }

        header h1 {
            margin: 0;
            font-size: 28px;
        }

        header p {
            color: #b8c5d6;
        }

        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
        }

        .card {
            background: white;
            padding: 30px;
            margin-bottom: 25px;
            border-radius: 14px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.06);
        }

        h2 {
            color: #172554;
        }

        .description {
            color: #64748b;
            line-height: 1.6;
        }

        input[type=file] {
            display: block;
            margin: 20px 0;
            padding: 12px;
            width: 100%;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
        }

        button {
            background: #2563eb;
            color: white;
            border: none;
            padding: 13px 25px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 15px;
        }

        button:hover {
            background: #1d4ed8;
        }

        .result {
            padding: 18px;
            margin-top: 20px;
            border-radius: 10px;
            line-height: 1.7;
            overflow-wrap: anywhere;
        }

        .success {
            background: #dcfce7;
            color: #166534;
        }

        .danger {
            background: #fee2e2;
            color: #991b1b;
        }

        .warning {
            background: #fef3c7;
            color: #92400e;
        }

        .hash {
            background: #f1f5f9;
            padding: 12px;
            border-radius: 8px;
            overflow-wrap: anywhere;
            font-size: 13px;
        }

        footer {
            text-align: center;
            padding: 25px;
            color: #64748b;
        }
    </style>
</head>

<body>

<header>
    <h1>File Integrity Monitor</h1>
    <p>Secure File Verification Using SHA-256</p>
</header>

<div class="container">

    <div class="card">
        <h2>Step 1: Upload Trusted File</h2>

        <p class="description">
            Upload the original file that you trust.
            Its SHA-256 hash will be saved as your reference.
        </p>

        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="trusted_file" required>
            <button type="submit" name="action" value="trust">
                Save Trusted File
            </button>
        </form>

        {% if trusted_name %}
        <div class="result success">
            Trusted file saved: <b>{{ trusted_name }}</b>
            <br>
            Reference hash:
            <div class="hash">{{ trusted_hash }}</div>
        </div>
        {% endif %}
    </div>


    <div class="card">
        <h2>Step 2: Verify Another File</h2>

        <p class="description">
            Upload the file you want to check.
            The system will compare its hash with the trusted file.
        </p>

        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="check_file" required>
            <button type="submit" name="action" value="verify">
                Verify File
            </button>
        </form>

        {% if message %}
        <div class="result {{ result_class }}">
            <h3>{{ message }}</h3>
            {{ details }}
        </div>
        {% endif %}

        {% if checked_hash %}
        <h3>Uploaded File SHA-256</h3>
        <div class="hash">{{ checked_hash }}</div>
        {% endif %}
    </div>

</div>

<footer>
    File Integrity Monitor | Python & SHA-256
</footer>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    message = ""
    details = ""
    result_class = ""
    checked_hash = ""

    trusted_name = session.get("trusted_name", "")
    trusted_hash = session.get("trusted_hash", "")

    if request.method == "POST":

        action = request.form.get("action")

        if action == "trust":

            file = request.files.get("trusted_file")

            if file and file.filename:

                trusted_hash = get_hash(file)

                session["trusted_hash"] = trusted_hash
                session["trusted_name"] = file.filename

                trusted_name = file.filename

                message = "Trusted reference file saved."
                details = "You can now upload another file for comparison."
                result_class = "success"

        elif action == "verify":

            file = request.files.get("check_file")

            if file and file.filename:

                checked_hash = get_hash(file)

                trusted_hash = session.get("trusted_hash", "")

                if not trusted_hash:

                    message = "No trusted file found."
                    details = "Please upload a trusted original file first."
                    result_class = "warning"

                elif checked_hash == trusted_hash:

                    message = "VERIFIED - FILE MATCHES"
                    details = "The uploaded file has the same SHA-256 hash as the trusted reference."
                    result_class = "success"

                else:

                    message = "WARNING - FILE DOES NOT MATCH"
                    details = "The uploaded file has a different SHA-256 hash from the trusted reference."
                    result_class = "danger"

    return render_template_string(
        HTML,
        trusted_name=trusted_name,
        trusted_hash=trusted_hash,
        message=message,
        details=details,
        result_class=result_class,
        checked_hash=checked_hash
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
