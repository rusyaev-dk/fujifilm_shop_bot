from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

review_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Назад"),

        ],
    ],
    resize_keyboard=True
)

review_stars = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⭐️⭐️⭐️⭐️⭐️")
        ],
        [
            KeyboardButton(text="⭐️⭐️⭐️⭐️")
        ],
        [
            KeyboardButton(text="⭐️⭐️⭐️")
        ],
        [
            KeyboardButton(text="⭐️⭐️")
        ],
        [
            KeyboardButton(text="⭐️")
        ],

    ],
    resize_keyboard=True
)
