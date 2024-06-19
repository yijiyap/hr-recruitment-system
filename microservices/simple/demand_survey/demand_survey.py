# Receives demand survey data from onedrive
# Sends demand survey data to the filtering microservice
from flask import (
    Flask,
    request,
    jsonify
)
import os
import requests
from flask_cors import CORS
import polars as pl

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@app.route("/ds", methods=["POST"])
def upload_excel():
    """
    To receive an excel file of the demand survey, 
    parse it, 
    and POST to the filtering microservice.
    """
    # TO RECEIVE FROM THE SHAREPOINT
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    if file:
        # try: 
            # read the excel file
            df = pl.read_excel(file)
            
            # change the headers to lowercase
            df.columns = [col.lower() for col in df.columns]

            # prepare demand survey data to be sent
            data = df.to_dicts() # to get row by row
            return jsonify(data)
            # # send the data to the filtering microservice
            # response = requests.post("http://localhost:9001/upload", json=data)

            # # return response.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)

    