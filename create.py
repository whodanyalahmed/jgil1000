from delete import service

def CreateFile(filename):
    data = {
        # this script will create a file name 'newFile'
        'name': filename,
        'mimeType': 'application/vnd.google-apps.spreadsheet',
    }
    file = service.files().create(body=data).execute() 
    print("success: file created")
    print('File ID: %s' % file.get('id'))
    
if __name__ == '__main__':
    CreateFile("newFile")
