from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command, or_f
from aiogram.enums import ParseMode

from price_checker import get_aptos_price
from keyboards import reply


user_router = Router()


@user_router.message(or_f(CommandStart(), (F.text.lower() == 'start')))
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello,<b> {message.from_user.full_name}!</b> Use the menu to get"
                         f" APT price or write /apt command",
                          reply_markup=reply.start_keyboard_3.as_markup(
                              resize_keyboard=True,
                              input_field_placeholder='What do you want?'  
                          ))
    

@user_router.message(or_f(Command('delete'), (F.text.lower() == 'delete')))
async def kb_dlt(message: types.Message) -> None:
    try:
        await message.answer("Deleted", reply_markup=reply.new_kbrd)
    except TypeError:
        await message.answer("Error")


@user_router.message(F.text.lower() == 'get apt price')
@user_router.message(or_f(Command('APT','apt','Apt'), (F.text.lower() == 'apt')))
async def price_handler(message: types.Message) -> None:
    try:
        # Send APT price
        await message.answer(get_aptos_price())      
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Error")


@user_router.message(F.text.lower() == 'about')
async def smile_answer(message: types.Sticker) -> None:    
    try:
        await message.answer("This is the bot to get APT price "
                             "use the Coinmarketcup API")
    except TypeError:
        await message.answer("Error")

