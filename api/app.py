from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "Brightfield API",
        "status": "running",
        "message": "Brightfield analysis pipeline is live"
    })


@app.route("/health")
def health():
    return jsonify({
        "ok": True
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
