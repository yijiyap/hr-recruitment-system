# gather job info from the demand survey microservice
# gather applicant info from the cv microservice
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001, debug=True)
