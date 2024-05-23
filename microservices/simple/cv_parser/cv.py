# meant for scanning CVs
from flask import (
    Flask,
    request,
    jsonify
)
from . import cv_utils
import requests
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@app.route("/cv/all", methods=["GET"])
def get_all_cv():
    return

if __name__ == "__main__":
    app.run(port=5002, debug=True)