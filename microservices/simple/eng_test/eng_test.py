# To consolidate the eng_test results 

import os
import requests
from flask import (
    Flask,
    request,
    jsonify
)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@app.route("/eng_test/all", methods=["GET"])
def all():
    """
    call the sharepoint microservice and get all the english test scores
    """
    # call the SharePoint Wrapper microservice to get the job application info
    eng_test_scores = requests.get("http://localhost:5004/eng_test/all").json()

    # make the email the key
    eng_test_scores = {score["email"]: score for score in eng_test_scores}
    return eng_test_scores

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=True)