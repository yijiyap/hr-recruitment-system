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

@app.route("/consolidate", methods=["GET"])
def consolidate():
    # consolidate the following candidate info:
    #   - CV Info
    #   - Job Application info
    #   - English test score
    # and send it to the filtering microservice
    candidate_id = request.args.get("candidate_id")
    
    # get the CV info
    cv_info = requests.get(f"http://localhost:5002/api/cv_info/{candidate_id}").json()