from bs4 import BeautifulSoup
import requests
import pandas as pd

#爬蟲方法
def runbug():
    url = urls
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    tables = soup.select('table')
    df_list = []
    for table in tables:
        df_list.append(pd.concat(pd.read_html(table.prettify())))    
    df = pd.concat(df_list)
    df.to_csv('weather.csv')
    return df_list

#創造一個資料list
df_list = []
#指定抓取資料日期範圍
for y in range(2015,2018):
    for m in range(1,13):
        for d in range(1,32):
            if d in range(1,10) and m in range(1,10):
                urls = ("http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467590&stname=%25E6%2581%2586%25E6%2598%25A5&datepicker=" + str(y) + '-0' + str(m) + '-0' + str(d))
            elif d in range(10,32) and m in range(1,10):
                urls = ("http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467590&stname=%25E6%2581%2586%25E6%2598%25A5&datepicker=" + str(y) + '-0' + str(m) + '-' + str(d))
            elif d in range(1,10) and m == 10:
                urls = ("http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467590&stname=%25E6%2581%2586%25E6%2598%25A5&datepicker=" + str(y) + '-' + str(m) + '-0' + str(d))
            elif d in range(1,10) and m in range(11,13):
                urls = ("http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467590&stname=%25E6%2581%2586%25E6%2598%25A5&datepicker=" + str(y) + '-' + str(m) + '-0' + str(d))
            else:
                urls = ("http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467590&stname=%25E6%2581%2586%25E6%2598%25A5&datepicker=" + str(y) + '-' + str(m) + '-' + str(d))
            url = urls
            res = requests.get(url)
            #beautifulSoup分析網站資料
            soup = BeautifulSoup(res.text, 'lxml')
            #取得所有表格
            tables = soup.select('table')
            #使用pd.read_html將表格內容寫入list中
            for table in tables:
                df_list.append(pd.concat(pd.read_html(table.prettify())))
#將資料寫入csv
df = pd.concat(df_list)
df.to_csv('weather.csv')