import os
import pandas as pd
import requests
# from newsapi import NewsApiClient
from config import stock_api, news_api

os.system('cls')

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
    # pct = delta / row.close

    # stock_df.delta[index] = delta
    stock_df.loc[index, 'delta'] = delta

    # stock_df.change_pct[index] = pct
    prev_close = row.close


stock_df.change_pct = ((stock_df.delta / stock_df.close) * 100)
# print(stock_df.head())


delta_df = stock_df[(stock_df['change_pct'] < -9.9) |
                    (stock_df['change_pct'] > 9.9)]

# newsapi = NewsApiClient(api_key=news_api)
news_url = 'https://newsapi.org/v2/everything'


for index, row in delta_df.iterrows():
    news_params = {
        'q': 'Tesla',
        'from': row.date,
        'sortBy': 'publishedAt',
        'apiKey': news_api,
    }
    news_response = requests.get(news_url, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()['articles']
    three_articles = articles[:3]
    print('-'*50)
    print(three_articles)
    print('-'*50)
