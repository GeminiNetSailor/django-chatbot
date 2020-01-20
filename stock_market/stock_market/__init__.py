import csv
from io import StringIO

import requests


def today_price_for(stock):
    url = 'https://stooq.com/q/l/?s={}&f=sd2t2ohlcv&h&e=csv'.format(stock)
    response = requests.get(url)

    decoded_content = response.content.decode('utf-8')
    reader = csv.DictReader(decoded_content.splitlines(), delimiter=',')
    return list(reader)[0]
