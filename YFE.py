from download import DownloadFile,CheckFileDir
from url_updater import GetExcelValues
def YFEDownloader(folder,filename):

    file_id = CheckFileDir(filename)
    sheetname = "TickerList"
    values = GetExcelValues(sheetname+"!E1",file_id)
    value = values[0][0]
    value= str(value)
    DownloadFile(filename,"YFE-"+value,folder)

    return ("YFE-"+value)


if __name__ == '__main__':
    folder = "C:/Ticker/"
    filename = "GS2"
    YFEDownloader(folder,filename)