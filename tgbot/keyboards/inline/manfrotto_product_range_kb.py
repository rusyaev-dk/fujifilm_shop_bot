from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.inline.callback_datas import manfrotto_product_type_callback

manfrotto_product_typekb = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Всё для студии",
                                 callback_data=manfrotto_product_type_callback.new(type="manfrotto_studio")),
            InlineKeyboardButton(text="Сумки",
                                 callback_data=manfrotto_product_type_callback.new(type="manfrotto_bags"))
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад",
                                 callback_data=manfrotto_product_type_callback.new(type="manfrotto_cancel"))
        ]
    ]
)

manfpt = ["manfrotto_studio", "manfrotto_bags", "manfrotto_cancel"]
