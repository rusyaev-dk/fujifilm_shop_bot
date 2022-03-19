from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.inline.callback_datas import fujifilm_product_type_callback

fujifilm_product_typekb = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Камеры",
                                 callback_data=fujifilm_product_type_callback.new(type="fujifilm_cameras")),
            InlineKeyboardButton(text="Объективы",
                                 callback_data=fujifilm_product_type_callback.new(type="fujifilm_lenses"))
        ],
        [
            InlineKeyboardButton(text="Прочие аксессуары",
                                 callback_data=fujifilm_product_type_callback.new(type="fujifilm_etc"))
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад",
                                 callback_data=fujifilm_product_type_callback.new(type="fujifilm_cancel"))
        ]
    ]
)

fjpt = ["fujifilm_cameras", "fujifilm_lenses", "fujifilm_etc", "fujifilm_cancel"]
