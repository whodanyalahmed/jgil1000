from googleapiclient.http import MediaFileUpload
from delete import service
def CheckFileDir(FileName):
    # page_token = None
    results = service.files().list(q='trashed=false',spaces='drive',fields="nextPageToken, files(id, name)",pageSize=400).execute()
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
    

if __name__ == '__main__':
    path = 'I:\\clients\\jgil1000\\'
    drive_filename = "newFile"
    filename = "agency.xlsx"
    UploadFile(path,filename,drive_filename)
