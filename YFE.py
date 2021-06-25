from download import DownloadFile
from url_updater import GetExcelValues,CheckFileDir


folder = "C:/Ticker/"
filename = "GS2"
file_id = CheckFileDir(filename)
sheet_Name = "TickerList"
values = GetExcelValues("E1",file_id)
print(values)
value = values[0][0]
value= str(value)
DownloadFile(filename,"YFE-"+value,folder)