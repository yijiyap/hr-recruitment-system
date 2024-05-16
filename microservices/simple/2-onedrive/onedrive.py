import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/list_files')
def list_files():
    tenant_id = 'YOUR_TENANT_ID'
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'

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

    # list files in OneDrive
    graph_url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    graph_response = requests.get(graph_url, headers=headers)
    files = graph_response.json().get('value')

    return jsonify(files)

if __name__ == '__main__':
    app.run(debug=True)