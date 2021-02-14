from flask import Flask, render_template, request, redirect, send_file
import scrapper_functions
import exporter
import requests
from bs4 import BeautifulSoup
import tqdm

app = Flask("ScrapperWeb")

CaseID = []
DecDate = []
Preview = []
Topic = []
index = []
searched = []


URL = "https://www.samili.com/law/ChoishinPanre.asp?op=1&part=ALL"
max_page = scrapper_functions.getMaxPage(URL)
for num in range(1, max_page + 1):
  print(f"Server is starting up... {round(num/max_page*100)}%")
  URL = f"https://www.samili.com/law/ChoishinPanre.asp?op=1&part=ALL&page={num}"
  data_raw = requests.get(URL)
  data_raw.encoding = 'euc-kr'
  soup = BeautifulSoup(data_raw.text, "html.parser")
  CaseID.extend(scrapper_functions.getCaseID(soup))
  DecDate.extend(scrapper_functions.getDecDate(soup))
  Preview.extend(scrapper_functions.getPreview(soup))
  Topic.extend(scrapper_functions.getTopic(soup))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/searching")
def searching():
    s_caseid = request.args.get('case_no')
    s_decdate = request.args.get('dec_date')
    s_topic = request.args.get('topic')
    s_keyword = request.args.get('key_word')
    if s_caseid:
        index = scrapper_functions.finding(s_caseid, CaseID)
        searched.append(s_caseid)
    elif s_decdate:
        index = scrapper_functions.finding(s_decdate, DecDate)
        searched.append(s_decdate)
    elif s_topic:
        index = scrapper_functions.finding(s_topic, Topic)
        searched.append(s_topic)
    elif s_keyword:
        index = scrapper_functions.finding(s_keyword, Preview)
        searched.append(s_keyword)
    else:
        return redirect('/error')
    term = searched[0]
    searched.clear()
    return render_template('search.html',
                           term=term,
                           length=len(index),
                           index = index,
                           CaseID=CaseID,
                           DecDate=DecDate,
                           Preview=Preview,
                           Topic=Topic)


@app.route("/download_result")
def download():
    try:
        term = request.args.get('term')
    except:
        return redirect("/")


app.run(host='0.0.0.0')
