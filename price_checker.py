import os


#Libraries for Coinmarketcup
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'id':'21794',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': f"{os.getenv('CMC_API_KEY')}",
}

session = Session()
session.headers.update(headers)

def get_aptos_price():
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

        symbol = ((data['data'])['21794'])['symbol']
        price = ((((data['data'])['21794'])['quote'])['USD'])['price']
        format_price = format(price , '.3f')
        return (f'Price of {symbol} token is {format_price}')
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e