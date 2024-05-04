import asyncio
import logging
import sys
import threading

#Libraries for Coinmarketcup
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


#Libraries for tg bot
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import Sticker

from bt_tkn import TOKEN, CMC_API_KEY



url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'id':'21794',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': CMC_API_KEY,
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

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}! Write any message to get APT price")



@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    if message.text == '😂':
        await message.answer("STICKER MTFC")
        return None
    
    try:
        # Send APT price
        await message.answer(get_aptos_price())
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")



@dp.message()
async def smile_answer(message: Sticker) -> None:
    
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")

def price_checker():
    threading.Timer(10.0, price_checker).start()
    get_aptos_price()


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    price_checker()
    asyncio.run(main())

