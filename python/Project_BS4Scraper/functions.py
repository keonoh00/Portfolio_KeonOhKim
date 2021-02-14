import requests
from bs4 import BeautifulSoup

def getMaxPage(URL):
    data_raw = requests.get(URL)
    data_raw.encoding = 'euc-kr'
    soup = BeautifulSoup(data_raw.text, "html.parser")
    content = soup.find("div", {"class":"page_num mt2"}).find_all("a")
    page_links = []
    for page in content:
        page_links.append(page['href'])
    max_page = int(page_links[-1][-2:])
    return max_page


def getCaseID(raw_soup):
    content = raw_soup.find("div", {"class": "list_type1"}).find("ul").find_all("li")
    strings = []
    for each_case in content:
        strings.append(each_case.text)
    title = []
    for line in strings:
        title.append(line.split(",")[0])
    return title

def getDecDate(raw_soup):
    content = raw_soup.find("div", {"class":"list_type1"}).find_all("strong", {"class":"l"})
    date = []
    for each_case in content:
        written = each_case.text.split()[1]
        date.append(written[0:10])
    return date


def getTopic(raw_soup):
    content = raw_soup.find("div", {"class":"list_type1"}).find_all("strong", {"class":"r"})
    topic = []
    for each_case in content:
        if each_case.text == "":
            topic.append("본문을 읽어보삼")
        else:
            topic.append(each_case.text)
    return topic

def getPreview(raw_soup):
    content = raw_soup.find("div", {"class": "list_type1"}).find("ul").find_all("a", {"class":"tit"})
    preview = []
    for each_case in content:
        preview.append(each_case.text)
    return preview