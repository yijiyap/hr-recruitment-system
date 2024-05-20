import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

tenant_id = os.getenv('AZURE_TENANT_ID')
client_id = os.getenv('AZURE_CLIENT_ID')
client_secret = os.getenv('AZURE_CLIENT_SECRET_VAlUE')

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

# # list files in OneDrive
graph_url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'
headers = {
    'Authorization': f'Bearer {access_token}'
}
graph_response = requests.get(graph_url, headers=headers)
print(graph_response.json())
files = graph_response.json().get('value')
print(files)

