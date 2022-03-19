from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.inline.callback_datas import brand_choice_callback

choose_brandkb = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sigma",
                                 callback_data=brand_choice_callback.new(type="sigma")),
            InlineKeyboardButton(text="Fujifilm",
                                 callback_data=brand_choice_callback.new(type="fujifilm"))
        ],
        [
            InlineKeyboardButton(text="Manfrotto",
                                 callback_data=brand_choice_callback.new(type="manfrotto")),
            InlineKeyboardButton(text="Colorama",
                                 callback_data=brand_choice_callback.new(type="colorama"))
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад",
                                 callback_data=brand_choice_callback.new(type="cancel_1"))
        ]
    ]
)

brands = ["sigma", "fujifilm", "manfrotto", "colorama", "cancel_1"]
