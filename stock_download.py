import requests
from datetime import datetime
import time

ticker = input("Enter the ticker symbol: ")

from_date = input("Enter start date in yyyy/mm/dd format: ")
to_date = input("Enter end date in yyyy/mm/dd format: ")

from_date_time = datetime.strptime(from_date, '%Y/%m/%d')
to_date_time = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(time.mktime(from_date_time.timetuple()))
to_epoch = int(time.mktime(to_date_time.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"


headers = {"User-Agent": "Mozilla/5.0 (x11, Linux x84_64) AppleWebkit"
                         "/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url, headers=headers).content

with open('data.csv', 'wb') as file:
    file.write(content)