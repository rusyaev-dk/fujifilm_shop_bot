from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.inline.callback_datas import colorama_product_type_callback

colorama_product_typekb = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Фоны",
                                 callback_data=colorama_product_type_callback.new(type="colorama_backgrounds"))
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад",
                                 callback_data=colorama_product_type_callback.new(type="colorama_cancel"))
        ]
    ]
)

clrmpt = ["colorama_backgrounds", "colorama_cancel"]
