from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

main_menu_callback = CallbackData("action", "section")
contacts_callback = CallbackData("action", "action")
review_callback = CallbackData("action", "action")


mm_sections = ["stock", "contacts", "review"]
main_menu_kb = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📷 Ассортимент",
                                 callback_data=main_menu_callback.new(section="stock"))
        ],
        [
            InlineKeyboardButton(text="📞 Контактная информация",
                                 callback_data=main_menu_callback.new(section="contacts"))
        ],
        [
            InlineKeyboardButton(text="✍️ Оставить отзыв",
                                 callback_data=main_menu_callback.new(section="review"))
        ]
    ]
)

contacts_actions = ["cancel_contacts"]
contacts_kb = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Назад",
                                 callback_data=contacts_callback.new(action="cancel_contacts"))
        ]
    ]
)

review_actions = ["cancel_review"]
review_kb = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="❌ Отмена",
                                 callback_data=review_callback.new(action="cancel_review"))
        ]
    ]
)
