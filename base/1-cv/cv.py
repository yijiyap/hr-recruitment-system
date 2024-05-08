# meant for scanning CVs
from flask import (
    Flask,
    request,
    jsonify
)

import requests
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

# function to add a new CV into the database
@app.route("/add_cv", methods=["POST"])
def add_cv():
    """
    Sample data received (to change according to the teams' needs):
    {
        "name": "Pom",
        "role applied to": "HR Intern",
        "email": "pom@gmail.com",
        "skills": ["communication", "teamwork", "problem solving"],
        "experience": "1 year in HR",
        "CV text": "I am a Year 2 student..."
    }
    """
    print("CV service received the following payload: ", request.json)
    
    try:
        # deposit CV into the RDS database
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
    
# function to retrieve all CVs from the database
@app.route("/get_all_cvs", methods=["GET"])
def get_all_cvs():
    """
    Sample data received (to change according to the teams' needs):
    [
        {
            "name": "Pom",
            "role applied to": "HR Intern",
            "email": "...",
            ...
        },
        {
            "name": "Tom",
            "role applied to": "Software Engineer",
            "email": "...",
            ...
        },
        ...
    ]
    """
    try:
        # retrieve all CVs from the RDS database
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
    
# function to retrieve a specific CV by id from the database
@app.route("/get_cv_by_id", methods=["GET"])
def get_cv_by_id():
    """
    Sample data received (to change according to the teams' needs):
    {
        "name": "Pom",
        "role applied to": "HR Intern",
        "email": "...",
        ...
    }
    """
    print("CV service received the following payload: ", request.json)
    
    try:
        # retrieve the specific CV from the RDS database
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
    
# function to delete a specific CV by id from the database
@app.route("/delete_cv_by_id", methods=["DELETE"])
def delete_cv_by_id():
    """
    Sample data received (to change according to the teams' needs):
    {
        "id": 1
    }
    """
    print("CV service received the following payload: ", request.json)
    
    try:
        # delete the specific CV from the RDS database
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
    
if __name__ == "__main__":
    app.run(port=5002, debug=True)