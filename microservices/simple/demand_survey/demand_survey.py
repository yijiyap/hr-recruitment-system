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

@app.route("/ds/all", methods=["GET"])
def all():
    """
    1. This endpoint will be called by the frontend to get all the demand survey data.
    2. DS microservice will call the SharePoint Wrapper microservice to get all the demand survey data.
    3. DS microservice will then return the DS info to the frontend.
    """
    # call the SharePoint Wrapper microservice to get the demand survey data
    # response = requests.get("http://localhost:5001/sharepoint/ds/all")

    # for now, we get the excel file of the results locally
    # only for testingg
    cur_path = os.path.dirname(os.path.realpath(__file__))
    # go back 3 folders to get to the excel file
    for i in range(4):
        cur_path = os.path.dirname(cur_path)
    dummy_survey = os.path.join(cur_path, "Internship Demand Survey Form for 2025(1-7).xlsx")

    df = pl.read_excel(dummy_survey)

    # change the headers to lowercase
    df.columns = [col.lower() for col in df.columns]

    # change to JSON format
    data = df.to_dicts() # to get row by row

    # group the supervisor details together
    grouped_data = {}
    for row in data:
        if row["supervisor"] not in grouped_data:
            grouped_data[row["supervisor"]] = []
        grouped_data[row["supervisor"]].append(row)

    


    return jsonify(data)

@app.route("/ds/test", methods=["POST"])
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

    