# meant for scanning CVs
from flask import (
    Flask,
    request,
    jsonify
)

import requests
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

if __name__ == "__main__":
    app.run(port=5002, debug=True)