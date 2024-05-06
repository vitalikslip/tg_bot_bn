from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="About"),
            KeyboardButton(text="Get APT Price",),
        ],
        [
            KeyboardButton(text="Test",),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='What do you want?'
)