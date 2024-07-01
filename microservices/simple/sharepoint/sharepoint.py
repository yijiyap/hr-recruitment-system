import requests
from flask import Flask, jsonify
import os
import asyncio
import asyncio
from flask_cors import CORS
from dotenv import load_dotenv
from rich import print
import polars as pl

app = Flask(__name__)
CORS(app)

# only for testing
cur_path = os.path.dirname(os.path.realpath(__file__))
# go back 3 folders to get to the .env file
for i in range(3):
      cur_path = os.path.dirname(cur_path)
load_dotenv(os.path.join(cur_path, '.env'))

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
TENANT_ID = os.getenv("TENANT_ID")
SCOPE = ["User.Read"]
INTERNSHIP_SHAREPOINT_SITE = os.getenv("INTERNSHIP_SHAREPOINT_SITE")
INTERNSHIP_SHAREPOINT_SITE_ID = os.getenv("INTERNSHIP_SHAREPOINT_SITE_ID")
INTERNSHIP_SHAREPOINT_LIBRARY_NAME = os.getenv("INTERNSHIP_SHAREPOINT_LIBRARY_NAME")
INTERNSHIP_SHAREPOINT_DRIVE_ID = os.getenv("INTERNSHIP_SHAREPOINT_DRIVE_ID")

# Authenticate and get access token
auth_url = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token'
data = {
      'grant_type': 'client_credentials',
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET,
      'scope': 'https://graph.microsoft.com/.default'
}
response = requests.post(auth_url, data=data)
access_token = response.json()['access_token']

@app.route("/ping", methods=["GET"])
def ping():
      return "pong"
   
@app.route("/sharepoint/cv/all", methods=["GET"])
def all_cv():
      """
      This endpoint will be called by the cv_parser microservice to get the CVs of all candidates.
      """
      # Get the list of files in the SharePoint library
      url = f'https://graph.microsoft.com/v1.0/sites/{INTERNSHIP_SHAREPOINT_SITE_ID}/drives/{INTERNSHIP_SHAREPOINT_DRIVE_ID}/items/root:/recruitment-system/2025_resume:/children'
      headers = {
         'Authorization': f'Bearer {access_token}'
      }
      response = requests.get(url, headers=headers)
      files = response.json()['value']

      files_to_return = []

      # download each pdf file and send it to the cv_parser microservice
      for file in files:
         try:
            download_url = file['@microsoft.graph.downloadUrl']
            
            files_to_return.append({
               "id": file['id'],
               "content": download_url
            })
         except Exception as e:
            print(f"An error occurred while processing the file: {file['name']}")
            print(e)

      return jsonify({
         "files": files_to_return
      })

@app.route("/sharepoint/ds/all", methods=["GET"])
def all_ds():
      """
      This microservice will be called by the demand_survey microservice to get the demand survey data.
      
      Note: THIS CODE ASSUMES THAT THERE IS ONLY 1 FILE IN THE FOLDER "demand_survey"
      """
      # Get the list of files in the SharePoint library
      url = f'https://graph.microsoft.com/v1.0/sites/{INTERNSHIP_SHAREPOINT_SITE_ID}/drives/{INTERNSHIP_SHAREPOINT_DRIVE_ID}/items/root:/recruitment-system/demand_survey:/children'
      headers = {
         'Authorization': f'Bearer {access_token}'
      }
      response = requests.get(url, headers=headers)
      download_url = response.json()['value'][0]['@microsoft.graph.downloadUrl']

      # process the file content and return it
      df = pl.read_excel(download_url)

      return jsonify({
         "df": df.to_dict(as_series=False)
      })

if __name__ == "__main__":
   app.run(port=5001, debug=True, host='0.0.0.0')

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