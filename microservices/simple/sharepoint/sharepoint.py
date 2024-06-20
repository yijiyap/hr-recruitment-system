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

    It will return the job application info of all candidates in the following format:
    {
        "