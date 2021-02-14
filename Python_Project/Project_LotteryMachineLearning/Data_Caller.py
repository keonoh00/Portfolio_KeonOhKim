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
    totSellamnt = []
    drwNoDate = []
    firstAccumamnt = []
    firstPrzwnerCo = []
    firstWinamnt = []

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
        totSellamnt.append(lottoNo['totSellamnt'])
        drwNoDate.append(lottoNo['drwNoDate'])
        firstAccumamnt.append(lottoNo['firstAccumamnt'])
        firstPrzwnerCo.append(lottoNo['firstPrzwnerCo'])
        firstWinamnt.append(lottoNo['firstWinamnt'])


    lotto_dict = {"Round":drwNo, "DATE":drwNoDate, "Num1":drwtNo1, "Num2":drwtNo2, "Num3":drwtNo3, "Num4":drwtNo4, "Num5":drwtNo5, "Num6":drwtNo6, "bnsNum":bnusNo, "Total_Sold":totSellamnt, "Prize_Tot":firstAccumamnt, "NumWinner":firstPrzwnerCo, "Prize_Ind":firstWinamnt} 

    df_lotto = pd.DataFrame(lotto_dict)


    return df_lotto


DB = getLottoWinInfo(1, 948)
DB.to_csv("Data.csv", index = False)