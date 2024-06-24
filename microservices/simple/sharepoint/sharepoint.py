import requests
from flask import Flask, jsonify
import os
import asyncio
import asyncio
from flask_cors import CORS
from O365 import Account, MSGraphProtocol, FileSystemTokenBackend
from dotenv import load_dotenv

# only for testing
load_dotenv('hr-recruitment-system/.env')

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
TENANT_ID = os.getenv("TENANT_ID")
SCOPE = ["User.Read"]

credentials = (CLIENT_ID, CLIENT_SECRET)

# token storage
cur_path = os.path.dirname(os.path.realpath(__file__))
token_backend = FileSystemTokenBackend(token_path=cur_path, token_filename='o365_token.txt')

# with your own identity
account = Account(credentials, auth_flow_type='credentials', tenant_id=TENANT_ID, token_backend=token_backend)
if account.authenticate():
   print('Authenticated!')

SHAREPOINT_SITE_ID = os.getenv("SHAREPOINT_SITE_ID")
sharepoint = account.sharepoint()
root_site = sharepoint.get_root_site()

# asyncio.run(main())

# app = Flask(__name__)
# CORS(app)

# @app.route("/ping", methods=["GET"])
# def ping():
#     return "pong"

# @app.route("/sharepoint/job_app/all", methods=["GET"])
# def all():
#     """
#     This endpoint will be called by the `candidates` microservice to get the job application info of all candidates.
#     When this endpoint is called, the `sharepoint` microservice will call the SharePoint API and get all the job application info from SharePoint.

#     It will return the job application info of all candidates in the following JSON format:
#     {
#         "
#         "
#     }
#     """
#     # GRAPH API CODE HERE

#     # Convert the PDF urls to base64 encoded strings
#     pass

# @app.route("/sharepoint/cv/all", methods=["GET"])
# def all_cv():
#     """
#     This endpoint will be called by the `candidates` microservice to get the CVs of all candidates.
#     When this endpoint is called, the `sharepoint` microservice will call the SharePoint API and get all the CVs from SharePoint.

#     It will return the CVs of all candidates in PDF format.
#     """
#     # GRAPH API CODE HERE

#     # Convert the PDF urls to base64 encoded strings
#     files_base64 = []
#     for file_url in pdf_urls:
#         response = requests.get(file_url)
#         if response.status_code == 200:
#             files_base64.append(response.content)

#     # Send the base64 encoded PDFs to the Next.js microservice
#     headers = {'Content-Type' : 'application/json'}
#     cv_parser_url = "http://localhost:5003/api/all"
#     try:
#         response = requests.post(cv_parser_url, json={"files": files_base64}, headers=headers)
#         if response.status_code == 200:
#             return jsonify({"message": "The cv of all candidates has been successfully consolidated.", "data": response.json()})    
#     except Exception as e:
#         return jsonify({"message": "An error occurred while consolidating the cv of all candidates."})

#     return jsonify({"message": "This endpoint will return the cv of all candidates in PDF format."})