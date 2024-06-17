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

@app.route("/candidates/all", methods=["GET"])
def all():
    """
    consolidate the following candidate info:
      - CV Info
      - Job Application info
      - English test score
    and send it to the filtering microservice

    Example of the consolidated data:
    {
        "1": {
            "cv_info": {
                "name": "John Doe",
                ...
            },
            "job_application_info": {
                "job_id": "1",
                ...
            },
            "english_test_score": 80
        },
        "2": {
            "cv_info": {
                "name": "Jane Doe",
                ...
            },
            "job_application_info": {
                "job_id": "2",
                ...
            },
            "english_test_score": 70
        }
    }
    """
    # call the CV microservice to get all the CV info
    cv_info = requests.get("http://localhost:5002/api/all").json()

    # call the SharePoint Wrapper microservice to get the job application info
    job_application_info = requests.get("http://localhost:5001/sharepoint/job_app/all").json()

    # call the English Test microservice to get the English test score
    english_test_score = requests.get("http://localhost:5004/eng_test/all").json()

    # combine them by the email address
    combined_data = {}
    for email, cv in cv_info.items():
        combined_data[email] = {
            "cv_info": cv,
            "job_application_info": job_application_info[email],
            "english_test_score": english_test_score[email]
        }
    return jsonify(combined_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9002, debug=True)