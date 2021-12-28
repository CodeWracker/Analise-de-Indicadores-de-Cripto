from datetime import date, timedelta, datetime
import requests
from tqdm import tqdm
import plotly.express as px
import pandas as pd
import numpy as np
# coinmarketcap key
# 2d9800d5-4e28-44b5-b450-a3275d653214

def getMercadoBTCdataByDate(year,month,day):
    #https://www.mercadobitcoin.net/api/BTC/day-summary/2021/11/11/
    dataMBTC = requests.get(f'https://www.mercadobitcoin.net/api/BTC/day-summary/{year}/{month}/{day}/')
    dataMBTC = dataMBTC.json()
    #https://blockchain.info/q/totalbc
    dataBLK = requests.get('https://blockchain.info/q/totalbc')
    coin_supply =int( dataBLK.text)/100000000
    returnData = {
        "market_cap": float(dataMBTC["avg_price"])* coin_supply,
        "coin_supply": coin_supply,
        "volume":float(dataMBTC["volume"]),
        "avg_price":float(dataMBTC["avg_price"]),
        "amount":float(dataMBTC["amount"]),
        "date":dataMBTC["date"]
    }
    return returnData

def getPriceByDay():
    return 

def getTodayDate():
    return str(date.today()).split("-")

def getYesterdayDate():
    return

def getNetValueByDay():
    return

def getTransactionsValueByDate():
    return    

# by 28 days
def calculateMovingAverage():
    return

def getNVT(year,month,day):
    nvt_data = getMercadoBTCdataByDate(year,month,day)
    print(nvt_data)
    nv_tv = nvt_data["market_cap"]/nvt_data["volume"]
    nvt_date = datetime.strptime(year+"/"+month+"/"+day,"%Y/%m/%d").date()
    mean = 0
    for i in (range(0,28)):
        analisys_date  =nvt_date - timedelta(days=i)
        yy,mm,dd = str(analisys_date).split('-')
        btc_data = getMercadoBTCdataByDate(yy,mm,dd)
        mean+=btc_data["avg_price"]
    mean = mean/28
    print(nv_tv,mean)
    print(nv_tv*mean)
    return nv_tv*mean

if __name__ == "__main__":
    today = date.today()
    yesterday = date.today() - timedelta(days=1)
    print(today)
    print(yesterday)
    yy,mm,dd = str(yesterday).split("-")
    nvt_list = []
    indexes = []
    for i in tqdm(range(1,4)):
        an_date = date.today() - timedelta(days=i)
        yy,mm,dd = str(an_date).split("-")
        nvt = getNVT(yy,mm,dd)
        nvt_list.append(nvt)
        indexes.append(i)
    df = pd.DataFrame()
    df['year'] = np.array(indexes)
    df["nvt"] = np.array(nvt_list)
    fig = px.line(df, x="year", y="nvt", title='NVT BTC')
    fig.show()