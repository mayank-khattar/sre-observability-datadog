from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/work")
def work():
    # simulate latency and occasional failure
    delay = random.uniform(0.1, 1.5)
    time.sleep(delay)

    if random.random() < 0.2:
        return jsonify(error="simulated failure"), 500

    return jsonify(message="work completed", latency=delay), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
