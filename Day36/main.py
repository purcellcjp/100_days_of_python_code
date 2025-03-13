import pandas as pd
import requests
from config import stock_api

url = 'https://www.alphavantage.co/query'
ticker_symbol = 'TSLA'

params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': ticker_symbol,
    'apikey': stock_api,
}

r = requests.get(url, params=params)

stock_data = r.json()
date = []
close = []
for key in stock_data['Time Series (Daily)']:
    # print(key, stock_data['Time Series (Daily)'][key]['4. close'], sep='|')
    date.append(key)
    close.append(float(stock_data['Time Series (Daily)'][key]['4. close']))

stock_df = pd.DataFrame(
    {'date': date,
     'close': close,
     }
)
stock_df['delta'] = float(0.00)
stock_df['change_pct'] = float(0.00)
# print(stock_df.dtypes)


prev_close = float(0.00)

for index, row in stock_df.iloc[::-1].iterrows():
    # print(index, row.date, row.close, row.delta, row.change_pct, sep='|')
    delta = row.close - prev_close
    pct = delta / row.close

    stock_df.delta[index] = delta
    stock_df.change_pct[index] = pct
    prev_close = row.close

print(stock_df.head(10))
