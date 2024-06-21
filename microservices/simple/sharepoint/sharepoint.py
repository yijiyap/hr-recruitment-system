import requests
from flask import Flask, jsonify
import os
import asyncio
from graph import Graph
import configparser
from msgraph.generated.models.o_data_errors.o_data_error import ODataError
import asyncio
from flask_cors import CORS

# # create an instance of the Graph class
# async def main():
#     print('Starting the Graph API')

#     # Load settings from config file
#     config = configparser.ConfigParser()
#     config.read('config.cfg')
#     azure_settings = config['azure']

#     # Create an instance of the Graph class
#     graph: Graph = Graph(azure_settings)

#     try:
#         # Get the access token
#         await display_access_token(graph)

#         # await display_files(graph)
#         print('Displayed files')
    
#     except ODataError as odata_error:
#         print('Error:')
#         if odata_error.error:
#             print(odata_error.error.code, odata_error.error.message)

# async def display_access_token(graph: Graph):
#     # Get the files
#     token = await graph.get_user_token()
#     print("User token:", token, "\n")

# async def display_files(graph: Graph):
#     # Get the files
#     # TODO
#      return

# asyncio.run(main())

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@app.route("/sharepoint/job_app/all", methods=["GET"])
def all():
    """
    This endpoint will be called by the `candidates` microservice to get the job application info of all candidates.
    When this endpoint is called, the `sharepoint` microservice will call the SharePoint API and get all the job application info from SharePoint.

    It will return the job application info of all candidates in the following JSON format:
    {
        "
        "
    }
    """
    # GRAPH API CODE HERE

    # Convert the PDF urls to base64 encoded strings
    pass

@app.route("/sharepoint/cv/all", methods=["GET"])
def all_cv():
    """
    This endpoint will be called by the `candidates` microservice to get the CVs of all candidates.
    When this endpoint is called, the `sharepoint` microservice will call the SharePoint API and get all the CVs from SharePoint.

    It will return the CVs of all candidates in PDF format.
    """
    # GRAPH API CODE HERE

    # Convert the PDF urls to base64 encoded strings
    files_base64 = []
    for file_url in pdf_urls:
        response = requests.get(file_url)
        if response.status_code == 200:
            files_base64.append(response.content)

    # Send the base64 encoded PDFs to the Next.js microservice
    headers = {'Content-Type' : 'application/json'}
    cv_parser_url = "http://localhost:5003/api/all"
    try:
        response = requests.post(cv_parser_url, json={"files": files_base64}, headers=headers)
        if response.status_code == 200:
            return jsonify({"message": "The cv of all candidates has been successfully consolidated.", "data": response.json()})    
    except Exception as e:
        return jsonify({"message": "An error occurred while consolidating the cv of all candidates."})

    return jsonify({"message": "This endpoint will return the cv of all candidates in PDF format."})