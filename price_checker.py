import os
import asyncio

#Libraries for Coinmarketcup
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from aiogram import Bot

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

sender = Bot(token=os.getenv('TOKEN'))

#This is Price checker use Coinmarcetcup API

# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
# parameters = {
#   'id':'21794',
#   'convert':'USD'
# }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': f"{os.getenv('CMC_API_KEY')}",
# }

# session = Session()
# session.headers.update(headers)


# async def get_aptos_price():
#     try:
#         price_before = 8.12
#         while True:
#             response = session.get(url, params=parameters)
#             data = json.loads(response.text)
#             symbol = ((data['data'])['21794'])['symbol']
#             price = ((((data['data'])['21794'])['quote'])['USD'])['price']
#             format_price = float(format(price , '.4f'))

#             if ((format_price/price_before)*100 - 100) > 0.2:
#                 percent = format(((format_price/price_before)*100 - 100), '.3f')
#                 await msg_sender(f'Price of {symbol} token increase ⬆️ {percent} % '
#                                  f'Now price is {format_price}')
                
#             if (100 - (format_price/price_before)*100) > 0.2:
#                 percent = format((100 - (format_price/price_before)*100), '.3f')
#                 await msg_sender(f'Price of {symbol} token decrease ⬇️{percent} % '
#                                  f'Now price is {format_price}')
                
#             price_before = format_price
#             await asyncio.sleep(350)
#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#         return e

url = 'https://api.binance.com/api/v3/ticker/price'
params = {
        'symbol': 'APTUSDT'
        }
symbol = 'APT'


async def get_aptos_price():
    try:
        price_before = 8.5
        while True:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                price = response.json()
            else:
                return None

            format_price = float(price['price'])

            if ((format_price/price_before)*100 - 100) > 0.2:
                percent = format(((format_price/price_before)*100 - 100), '.3f')
                await msg_sender(f'Price of {symbol} token increase ⬆️ {percent} % '
                                 f'Now price is {format_price}')
                
            if (100 - (format_price/price_before)*100) > 0.2:
                percent = format((100 - (format_price/price_before)*100), '.3f')
                await msg_sender(f'Price of {symbol} token decrease ⬇️{percent} % '
                                 f'Now price is {format_price}')
                
            price_before = format_price
            await asyncio.sleep(350)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e
   

async def msg_sender(msg):
    with open("id.txt") as file:
        lines = file.readlines()
        print(lines)
        for chat in lines:
            await sender.send_message(chat, msg)
        
    

    