from aiogram import F, Router, types, html
from aiogram.filters import CommandStart, Command, or_f

from price_checker import get_aptos_price
from keyboards import reply


user_router = Router()


@user_router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {message.from_user.full_name}! Write any message to get APT price",
                          reply_markup=reply.start_keyboard)


@user_router.message(F.text.lower() == 'get apt price')
@user_router.message(or_f(Command('APT','apt','Apt'), (F.text.lower() == 'apt')))
async def price_handler(message: types.Message) -> None:
    try:
        # Send APT price
        await message.answer(get_aptos_price())
        
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Error")



@user_router.message(F.text)
async def smile_answer(message: types.Sticker) -> None:
    
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Error")


@user_router.message(F.sticker)
async def smile_answer(message: types.Sticker) -> None:
    
    try:
        await message.answer("emoji")
    except TypeError:
        await message.answer("Error")