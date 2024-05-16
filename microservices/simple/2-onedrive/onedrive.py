import requests
from flask import Flask, jsonify
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# app = Flask(__name__)

# @app.route('/list_files')
# def list_files():
#     tenant_id = os.getenv('AZURE_TENANT_ID')
#     client_id = os.getenv('AZURE_CLIENT_ID')
#     client_secret = os.getenv('AZURE_CLIENT_SECRET_ID')

#     print(tenant_id, client_id, client_secret)

    # # obtain access token
    # token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
    # token_data = {
    #     'grant_type': 'client_credentials',
    #     'client_id': client_id,
    #     'client_secret': client_secret,
    #     'scope': 'https://graph.microsoft.com/.default'
    # }
    # token_response = requests.post(token_url, data=token_data)
    # access_token = token_response.json().get('access_token')

    # # list files in OneDrive
    # graph_url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'
    # headers = {
    #     'Authorization': f'Bearer {access_token}'
    # }
    # graph_response = requests.get(graph_url, headers=headers)
    # files = graph_response.json().get('value')

    # return jsonify(files)

# if __name__ == '__main__':
#     app.run(debug=True)


tenant_id = os.getenv('AZURE_TENANT_ID')
# tenent_id = "consumers"
client_id = os.getenv('AZURE_CLIENT_ID')
client_secret = os.getenv('AZURE_CLIENT_SECRET_VAlUE')

print(tenant_id, client_id, client_secret)

# obtain access token
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
token_data = {
    
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'https://graph.microsoft.com/.default'
}
token_response = requests.post(token_url, data=token_data)
access_token = token_response.json().get('access_token')

print(token_response.json())

# # list files in OneDrive
# graph_url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'
# headers = {
#     'Authorization': f'Bearer {access_token}'
# }
# graph_response = requests.get(graph_url, headers=headers)
# files = graph_response.json().get('value')