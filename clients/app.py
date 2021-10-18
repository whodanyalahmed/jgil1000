from delete import deleteFile
from download import DownloadFile
from upload import UploadFile
from url_updater import Updater
from share import ShareFile
from YFE import YFEDownloader

if __name__ == '__main__':
    
    folder = "C:/STK_YFE/GoogleDrive/"
    filename = "GS2"
    YFEDownloader(folder,filename)
    deleteFile(filename)
    UploadFile(folder,"YFE-upload.xlsx",filename)
    Updater(filename,"GS1")
    emails = ["yahoo-finance@yahoo-307609.iam.gserviceaccount.com","yahoo-finance-1@yahoo-307609.iam.gserviceaccount.com","yahoo-finance-2@yahoo-307609.iam.gserviceaccount.com","yahoo-finance-3@yahoo-307609.iam.gserviceaccount.com","yahoo-finance-4@yahoo-307609.iam.gserviceaccount.com","yahoo-finance-5@yahoo-307609.iam.gserviceaccount.com","ticker-a@ticker-316606.iam.gserviceaccount.com"]
    ShareFile(filename,emails)


    
