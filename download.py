
from delete import CheckFileDir,service
import io
from googleapiclient.http import MediaIoBaseDownload


def DownloadFile(filename_in_drive,outputname,path):
    try:
        file_id = CheckFileDir(filename_in_drive)
        print(file_id)
        request = service.files().export_media(fileId=file_id,mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        fh = io.FileIO(path + outputname + '.xlsx','wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print('Download %d%%.' % int(status.progress() * 100))
        return fh
    except Exception as e:
        print('Error downloading file from Google Drive: %s' % e)


if __name__ == '__main__':
    
    path = 'C:/Ticker/'
    DownloadFile('GS2','GS2',path)
