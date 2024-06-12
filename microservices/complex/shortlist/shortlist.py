# gather job info from the post request
# gather applicant info from the candidate microservice
# rank the applicants 

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

@app.route("/shortlist", methods=["POST"])
def shortlist():
    # get job info from the post request
    job_id = request.json["job_id"]

    # get applicant info from the candidate microservice

    # get the scores of all the candidates

    # rank the candidates

    # return the top 20 candidates in JSON format

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001, debug=True)
