import re
from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_marked_section, Bold, as_list
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


from price_checker import get_aptos_price
from keyboards import reply

class Subscribe(StatesGroup):
    sign_in = State()


user_router = Router()


@user_router.message(or_f(CommandStart(), (F.text.lower() == 'start')))
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """ 
    text_answer = as_list(
        as_marked_section(
            Bold("Hello, ", message.from_user.full_name, "!"),
            "You can get APT price",
            "Get info about the bot",
            marker="✅"
        ),
        "Or you can just relax",
        sep="\n-------------------------\n"
    )

    await message.answer(text_answer.as_html(),
                          reply_markup=reply.start_keyboard_3.as_markup(
                              resize_keyboard=True,
                              input_field_placeholder='What do you want?',
                          ))
    

@user_router.message(or_f(Command('delete'), (F.text.lower() == 'delete')))
async def kb_dlt(message: types.Message) -> None:
    """
        Unsubscribe and delete keyboard
    """
    try:
        await message.answer("You're sucsessfully unsubscribe", reply_markup=reply.new_kbrd)
        with open('id.txt') as file:
            lines = file.readlines()

        pattern = re.compile(re.escape(str(message.chat.id)))
        with open('id.txt', 'w') as file:
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    file.write(line)
    except TypeError:
        await message.answer("Error3")


@user_router.message(F.text.lower() == 'get apt price')
@user_router.message(or_f(Command('apt'), (F.text.lower() == 'apt')))
async def price_handler(message: types.Message, state: FSMContext) -> None:

    with open("id.txt", "r") as file:
        content = file.read()
    with open("id.txt", "a") as file:
        if str(message.chat.id) not in content:
            file.write(str(message.chat.id) + "\n")

    # Send APT price
    await state.set_state(Subscribe.sign_in)
    try:
        await get_aptos_price()   
    except TypeError:
        await message.answer("Error1")


@user_router.message(F.text.lower() == 'about')
async def smile_answer(message: types.Sticker) -> None:    
    try:
        await message.answer("This is the bot to get APT price "
                             "use Coinmarketcup API")
    except TypeError:
        await message.answer("Error2")

