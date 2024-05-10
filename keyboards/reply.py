from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="About"),
            KeyboardButton(text="Get APT Price",),
        ],
        [
            KeyboardButton(text="Delete",),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='What do you want?'
)

delete_keyboard = ReplyKeyboardRemove()

new_kbrd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Start"),
        ],
    ],
    resize_keyboard=True,
)

start_keyboard_2 = ReplyKeyboardBuilder()

start_keyboard_2.add(
    KeyboardButton(text="Get APT Price"),
    KeyboardButton(text="Delete"),
)
start_keyboard_2.adjust(2,1)

start_keyboard_3 = ReplyKeyboardBuilder()

start_keyboard_3.attach(start_keyboard_2)

start_keyboard_3.row(KeyboardButton(text="About"))