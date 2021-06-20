from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


"""Shows basic usage of the Drive v3 API.
Prints the names and ids of the first 10 files the user has access to.
"""
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('drive', 'v3', credentials=creds)
def CheckFileDir(FileName):
    # page_token = None
    results = service.files().list(spaces='drive',fields="nextPageToken, files(id, name)",pageSize=400).execute()
    items = results.get('files', [])

    # print(len(items))
    # for i in items:  
    if not items:
        print('No files found.')
        return None
    else:
        # print('Files:')
        for item in items:
            # print(item['name'])
            if(item['name'] == FileName):
                print(FileName + " is already there")
                # print(item['name'])
                return item['id']
 
def delete_file(filename):

    file_id = CheckFileDir(filename)
    print(file_id)
    try:
        service.files().delete(fileId=file_id).execute()
        print("success : successfully deleted the file")
    except Exception as e:
        print('An error occurred: %s',e)
def UploadFile(path,local_filename,upload_name):
    file = CheckFileDir(upload_name)
    # print(file)
    if(file != None):
        ask = input("Wanna replace ? delete old one? Y/N: ")
        if(ask.lower() == 'y' ):
            delete_file(upload_name)
            
    file_metadata = {
    'name': upload_name,
    'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload(path+local_filename,
                        mimetype='application/vnd. openxmlformats-officedocument',
                        resumable=True)
    file = service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
    print('File ID: %s' % file.get('id'))
    

path = 'I:\\clients\\jgil1000\\'
filename = input("Enter local filename(case sensitive) with extension to upload in drive: ")
# drive_filename = "agency"

drive_filename = input("Enter filename(case sensitive) to show in drive: ")
UploadFile(path,filename,drive_filename)
