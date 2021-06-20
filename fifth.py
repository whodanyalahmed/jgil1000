from __future__ import print_function
from http.client import error
import os.path
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import io

from googleapiclient.http import MediaIoBaseDownload
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
def retrieve_permissions(file_id):
  """Retrieve a list of permissions.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to retrieve permissions for.
  Returns:
    List of permissions.
  """
  try:
    permissions = service.permissions().list(fileId=file_id).execute()
    return permissions.get('permissions', [])
  except Exception as error:
    print('An error occurred: %s' % error)
  return None
emails = []
filename = input("Enter filename(case sensitive) to assign email in drive: ")
no_of_emails = int(input("Enter no of emails you wanna add: "))
for no in range(no_of_emails):
    email = input("Enter email to share the file: ")
    emails.append(email)
file_id = CheckFileDir(filename)
perm_id = retrieve_permissions(file_id)
print(perm_id)
# Insert new permission first
# emails = ['daninotific@gmail.com','ayizashiekh@gmail.com','whodanyalahmed@gmail.com']

# Then delete old permission
for id in perm_id:
    try:
        service.permissions().delete(fileId=file_id, permissionId=id['id']).execute()
    except Exception as e:
        print("Done deleting...")
for email in emails:
    try:
        
        new_permission = {
            'type': 'user',
            'role': 'writer',
            'emailAddress': email
            }
        run_new_permission = service.permissions().create(fileId=file_id,sendNotificationEmail=False,body=new_permission).execute()
        print("success : New Email added")
    except Exception as e:
        print("error : cant add new permission")