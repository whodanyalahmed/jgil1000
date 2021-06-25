from delete import CheckFileDir,build,creds

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
    if values == 0:
        values = [[url]]
    else:
        values[0][0] = url
    UpdateValues(to,values)
    print("success : wrote to " + to_file)


if __name__ == '__main__':
    Updater('GS2','GS1')