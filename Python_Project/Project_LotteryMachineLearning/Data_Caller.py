'''
Below code brings data from website and stores data as csv file
Currently set as draw 1 ~ 948
'''

# -*- coding: eur-kr -*-

# Setting up the required library
import pandas as pd
import requests
from tqdm import tqdm
import json
from bs4 import BeautifulSoup
import re


# Function to call the previous lottery data

def getLottoWinInfo(minDrwNo, maxDrwNo):
    drwtNo1 = []
    drwtNo2 = []
    drwtNo3 = []
    drwtNo4 = []
    drwtNo5 = []
    drwtNo6 = []
    bnusNo = []
    drwNo = []
    drwYear = []
    drwMon = []
    drwDay = []

    for i in tqdm(range(minDrwNo, maxDrwNo+1, 1)):
        req_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(i)
        req_lotto = requests.get(req_url)
        lottoNo = req_lotto.json()
        drwNo.append(lottoNo['drwNo'])
        drwtNo1.append(lottoNo['drwtNo1'])
        drwtNo2.append(lottoNo['drwtNo2'])
        drwtNo3.append(lottoNo['drwtNo3'])
        drwtNo4.append(lottoNo['drwtNo4'])
        drwtNo5.append(lottoNo['drwtNo5'])
        drwtNo6.append(lottoNo['drwtNo6'])
        bnusNo.append(lottoNo['bnusNo'])
        drwYear.append(lottoNo['drwNoDate'][:4])
        drwMon.append(lottoNo['drwNoDate'][5:7])
        drwDay.append(lottoNo['drwNoDate'][-2:])


    lotto_dict = {"Round":drwNo, "Year":drwYear, "Month":drwMon, "Day":drwDay, "Num1":drwtNo1, "Num2":drwtNo2, "Num3":drwtNo3, "Num4":drwtNo4, "Num5":drwtNo5, "Num6":drwtNo6, "bnsNum":bnusNo} 


    return lotto_dict


def getWeather(year, mon, day):
    URL = f"https://www.weather.go.kr/weather/climate/past_cal.jsp?stn=108&yy={year}&mm={mon}&x=22&y=6&obs=1"
    web_page = requests.get(URL)
    soup = BeautifulSoup(web_page.text, 'html.parser')
    weather_table = soup.find("table", {"class":"table_develop"})
    table_data = weather_table.find_all("td", {"class":"align_left"})
    weather_day = []
    weather_temp = []
    weather_rain = []
    for data in table_data:
        current_string = data.text.strip()
        if current_string:
            if current_string[-1] == "일":
                weather_day.append(current_string[:-1])
            else:
                try:
                    temp = re.search("평균기온:(.+?)℃최고기온", current_string)
                    rain = re.search("강수량:(.+?)", current_string)
                    weather_temp.append(temp.group(1))
                    weather_rain.append(rain.group(1))
                except:
                    pass
    index = weather_day.index(str(int(day)))
    result = [weather_temp[index], weather_rain[index]]
    return result


min_round = 1
max_round = 800

print("Getting Lottery Information\n\n\n")

DB = getLottoWinInfo(1, 800)
temperature = []
rain = []
for y, m, d in zip(DB["Year"], DB["Month"], DB["Day"]):
    print(f"Getting Information... {round(min_round/max_round*100, 2)}%  {min_round}/{max_round}")
    min_round += 1
    weather = getWeather(y, m, d)
    temperature.append(weather[0])
    rain.append(weather[1])
DB["Temperature"] = temperature
DB["RainAmout"] = rain

DB = pd.DataFrame(DB)
DB.to_csv("Data.csv", index = False)
