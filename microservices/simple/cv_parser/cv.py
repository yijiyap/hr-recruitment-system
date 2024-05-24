# meant for scanning CVs
from flask import (
    Flask,
    request,
    jsonify
)
import PyPDF2
import os
from . import cv_utils
import requests
from flask_cors import CORS
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
import spacy

UPLOAD_FOLDER_CV = "uploads/cv"

app = Flask(__name__)
CORS(app)

nlp = spacy.load('en_core_web_sm')

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@app.route("/cv/all", methods=["GET"])
def get_all_cv():
    return

@app.route("/upload", methods=["POST"])
def upload_file():
    """
    To receive a pdf file of the CV, parse it, and POST to the filtering microservice
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    if file:
        # try: 
            # save the file received
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER_CV, filename))

            # extract the text from the CV
            raw_text = cv_utils.extract_text_main(os.path.join(UPLOAD_FOLDER_CV, filename), filename.split(".")[-1])
            print(raw_text)
            nlp_text = nlp(raw_text)

            # prepare CV data to be sent
            data = {
                "raw_text": raw_text,
                "nlp_text": nlp_text,
                "email": cv_utils.extract_email(raw_text),
                "skills": cv_utils.extract_skills(nlp_text, nlp_text.noun_chunks),
                "experience": cv_utils.extract_experience(raw_text)
            }
            print(data)

            # send the CV data to the filtering microservice
            # url = "http://localhost:5001/upload"
            # response = requests.post(url, json=data)
            # return response.json()
        # except Exception as e:
            # return jsonify({"error": str(e)})
    return
if __name__ == "__main__":
    app.run(port=5002, debug=True)