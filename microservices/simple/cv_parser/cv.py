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

@app.route("/shortlist_cv", methods=["POST"])
def shortlist_cv():
    data = request.get_json()
    cv = data.get("cv")
    if not cv:
        return jsonify({
            "error": "Please provide a CV"
        }), 400
    try:
        extracted_details = cv_utils.cv_result_wrapper(cv)
        return jsonify(extracted_details)
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
    
def shortlist_cv_helper(cv):
    return

if __name__ == "__main__":
    app.run(port=5002, debug=True)