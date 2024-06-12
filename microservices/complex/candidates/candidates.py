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
    #   - Link to CV
    #   - Job Application info
    #   - English test score
    # and send it to the filtering microservice
    candidate_id = request.args.get("candidate_id")
    
    # get the link to the CV