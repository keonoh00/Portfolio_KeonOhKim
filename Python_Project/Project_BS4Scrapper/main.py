import functions
import requests
from bs4 import BeautifulSoup
import csv

# This comment is used to check whether git hub is working

CaseID = []
DecDate = []
Preview = []
Topic = []

Main_URL = "https://www.samili.com/law/ChoishinPanre.asp?op=1&part=ALL"
max_page = functions.getMaxPage(Main_URL)

for num in range(1,max_page+1):
    URL = f"https://www.samili.com/law/ChoishinPanre.asp?op=1&part=ALL&page={num}"
    data_raw = requests.get(URL)
    data_raw.encoding = 'euc-kr'
    soup = BeautifulSoup(data_raw.text, "html.parser")
    CaseID.extend(functions.getCaseID(soup))
    DecDate.extend(functions.getDecDate(soup))
    Preview.extend(functions.getPreview(soup))
    Topic.extend(functions.getTopic(soup))
header = ["사건번호", "판결일자", "주제", "판결 미리보기"]
temp2 = zip(*[CaseID, DecDate, Topic, Preview])
total_data = list()
total_data.append(header)
total_data.extend(temp2)
with open('Samil_Scraped.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(total_data)