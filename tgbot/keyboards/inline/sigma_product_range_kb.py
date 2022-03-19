from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.inline.callback_datas import sigma_product_type_callback

sigma_product_typekb = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Объективы",
                                 callback_data=sigma_product_type_callback.new(type="sigma_lenses"))

        ],
        [
            InlineKeyboardButton(text="Прочие аксессуары",
                                 callback_data=sigma_product_type_callback.new(type="sigma_etc"))
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад",
                                 callback_data=sigma_product_type_callback.new(type="sigma_cancel"))
        ]
    ]
)

spt = ["sigma_lenses", "sigma_etc", "sigma_cancel"]
