# To consolidate the eng_test results 

import os
import requests
from flask import (
    Flask,
    request,
    jsonify
)
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@app.route("/all", methods=["GET"])
def all():
    """
    This endpoint will be called by the `candidates` microservice to get the english test scores of all candidates.
    When this endpoint is called, the `eng_test` microservice will call the `sharepoint` microservice and get all the english test scores from SharePoint.

    It will return the english test scores of all candidates in the following format:
    {
        "john@example.com": 80,
        "stacy@example.com": 70,
        ...
        "jane@example.com": 90
    }
    """
    # call the SharePoint Wrapper microservice to get the job application info
    # eng_test_scores = requests.get("http://localhost:5001/eng_test/all").json()

    # for testing purposes, read the csv file directly
    csv_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../eng_test.csv'))
    eng_test_scores = pd.read_csv(csv_file_path, header=None, skiprows=1)

    # keep only the 0th and 5th column, and give the titles "email" and "percent"
    eng_test_scores = eng_test_scores[[0, 5]]
    eng_test_scores.columns = ["email", "percent"]

    # convert the dataframe to a dictionary
    eng_test_scores_dict = eng_test_scores.set_index("email").T.to_dict("records")[0]

    return jsonify(eng_test_scores_dict)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=True)