from delete import deleteFile
from download import DownloadFile
from upload import UploadFile
from url_updater import Updater
from share import ShareFile
from YFE import YFEDownloader

if __name__ == '__main__':
    
    folder = "C:/Ticker/"
    filename = "GS2"
    YFEname = YFEDownloader(folder,filename)
    deleteFile(filename)
    UploadFile(folder,YFEname+".xlsx",filename)
    Updater(filename,"GS1")
    emails = ["daniahmedkhatri@gmail.com","something@gmail.com","anotheremail@gmail.com"]
    ShareFile(filename,emails)


    
