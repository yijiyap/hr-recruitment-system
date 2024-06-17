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
    # get demand survey info from the post request
    ds_info = request.json["ds_info"]

    # get all candidates info from the candidate microservice
    candidates_info = requests.get("http://localhost:9002/all").json()

    # get the scores of all the candidates
    score_dict = calculate_scores(ds_info, candidates_info)

    # sort the scores
    sorted_scores = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)

    # return the top 20 candidates
    return sorted_scores[:20]

def calculate_scores(ds_info, candidates_info):
    """
    Calculate the scores of all the candidates based on the demand survey info.
    """
    score_dict = {}
    # for candidate in candidates_info:
    #     score = 0
    #     for key, value in ds_info.items():
    #         if key in candidate:
    #             if candidate[key] == value:
    #                 score += 1
    #     score_dict[candidate["candidate_id"]] = score
    return score_dict

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001, debug=True)
