import asyncio
import logging
import sys
import os


#Libraries for tg bot
from aiogram import Bot, Dispatcher, types

from dotenv import find_dotenv, load_dotenv
from handlers.users import user_router
from command_list import private

load_dotenv(find_dotenv())

UPDATES = ['message','edited_message']


dp = Dispatcher()
dp.include_router(user_router)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=os.getenv('TOKEN'), parse_mode="HTML")
    # And the run events dispatching
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private,scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=UPDATES)



if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    

