import asyncio
import logging
import sys

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

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

# dp = Dispatcher()


# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     """
#     This handler receives messages with `/start` command
#     """
#     await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


    


# @dp.message()
# async def echo_handler(message: Message) -> None:
#     """
#     Handler will forward receive a message back to the sender

#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     if message.text == '😂':
#         await message.answer("STICKER MTFC")
#         return None
    
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#         print(type(message.text))
#         print(message)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")



# @dp.message()
# async def smile_answer(message: Sticker) -> None:
    
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("Nice try!")



# async def main() -> None:
#     # Initialize Bot instance with default bot properties which will be passed to all API calls
#     bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#     # And the run events dispatching
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())

