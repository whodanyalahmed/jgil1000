from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import io

from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']


creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'C:\\Ticker\\ticker.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('drive', 'v3', credentials=creds)



def CheckFileDir(FileName):
    results = service.files().list(q="mimeType = 'application/vnd.google-apps.spreadsheet' and trashed = false",spaces='drive',fields="nextPageToken, files(id, name)",pageSize=400).execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
        return None
    else:
        for item in items:
            if(item['name'] == FileName):
                # print(FileName + " is already there")
                return item['id']
 
def DownloadFile(filename):
    try:
        file_id = CheckFileDir(filename)
        print(file_id)
        path = 'I:\\clients\\jgil1000\\'
        request = service.files().export_media(fileId=file_id,mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        fh = io.FileIO(path + filename + '.xlsx','wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print('Download %d%%.' % int(status.progress() * 100))
        return fh
    except Exception as e:
        print('Error downloading file from Google Drive: %s' % e)


if __name__ == '__main__':
    DownloadFile('sheet')
    # write code to be executed only on direct execution, but not on import
    # This is because direct execution assigns `'__main__'` to `__name__` while import of any way assigns the name under which it is imported.