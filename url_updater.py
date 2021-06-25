from download import CheckFileDir
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']

creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


def GetExcelValues(range,Id):
    result = sheet.values().get(spreadsheetId=Id,
                                range=range).execute()
    values = result.get('values', [])
    if not values:
        print('error : Excel No data found.')
        return 0
    else:
        print('success: Excel Readable found')
        return values
def UpdateValues(Id,values):
    Links_Range = "A1"
    request = sheet.values().update(spreadsheetId=Id, range=Links_Range, valueInputOption="USER_ENTERED", body={"values" : values})
    try:
        response = request.execute()
    except Exception as e:
        print("error : something went wrong or " + str(e))

def Updater(filename,to_file):
    file_id  = CheckFileDir(filename)
    to = CheckFileDir(to_file)
    values = GetExcelValues('A1',to)
    url = f"https://docs.google.com/spreadsheets/d/{file_id}/edit?usp=drive_web"
    print(values)
    if values == 0:
        values = [[url]]
    else:
        values[0][0] = url
    print(values)
    UpdateValues(to,values)


if __name__ == '__main__':
    Updater('GS2','GS1')