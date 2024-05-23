from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
    if file1['title'] == 'Summer Indorama budget 2024': ## filename
        print('title: %s, id: %s' % (file1['title'], file1['id']))
        file1.GetContentFile('Summer Indorama budget 2024.xlsx') # not working
        break

