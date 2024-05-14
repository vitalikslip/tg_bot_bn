import os
import asyncio

#Libraries for Coinmarketcup
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from aiogram import Bot

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

sender = Bot(token=os.getenv('TOKEN'))

async def get_aptos_price():
    try:
        while True:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            symbol = ((data['data'])['21794'])['symbol']
            price = ((((data['data'])['21794'])['quote'])['USD'])['price']
            format_price = format(price , '.4f')
            await msg_sender()
            await asyncio.sleep(10)
            #return (f'Price of {symbol} token is {format_price}') 
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e
    

async def msg_sender():
    with open("id.txt") as file:
        lines = file.readlines()
        print(lines)
        for i in lines:
            await sender.send_message(i, "Sender works")
        
    

    