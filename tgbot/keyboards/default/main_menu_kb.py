from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menukb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="📷 Ассортимент")
        ],
        [
            KeyboardButton(text="📞 Контактная информация"),
            KeyboardButton(text="✍️ Оставить отзыв")
        ]
    ]
)
