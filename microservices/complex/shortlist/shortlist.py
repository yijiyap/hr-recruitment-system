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
from . import shortlist_utils

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@app.route("/shortlist", methods=["POST"])
def shortlist():
    # get demand survey info from the post request
    ds_info = request.json["ds_info"]

    # get all candidates info from the candidate microservice
    candidates_info = requests.get("http://localhost:9002/all").json()

    # calculate fitness score for each candidate, and rank them
    shortlisted_candidates = shortlist_utils.rank_candidates(ds_info, candidates_info)

    return jsonify(shortlisted_candidates)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001, debug=True)
