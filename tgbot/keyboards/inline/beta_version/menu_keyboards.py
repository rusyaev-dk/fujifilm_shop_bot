from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from tgbot.services.db_api import quick_commands as commands

menu_callback = CallbackData("show_menu", "level", "category", "subcategory", "item_id")
buy_item_callback = CallbackData("buy", "item_id")


def make_callback_data(level, category="0", subcategory="0", item_id="0"):
    return menu_callback.new(level=level, category=category,
                             subcategory=subcategory, item_id=item_id)


async def categories_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=2)

    categories = await commands.get_categories()
    for category in categories:
        button_text = f"{category.category_name}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=category.category_code)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    return markup


async def subcategories_keyboard(category):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=2)

    subcategories = await commands.get_subcategories(category)
    for subcategory in subcategories:
        button_text = f"{subcategory.subcategory_name}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=category,
                                           subcategory=subcategory.subcategory_code)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        # level = ... Мы передали тот уровень НА КОТОРЫЙ хотим переместиться
        InlineKeyboardButton(text="⬅️ Назад",
                             callback_data=make_callback_data(level=CURRENT_LEVEL - 1))
    )
    return markup


async def items_keyboard(category, subcategory):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=1)
    items = await commands.get_items(category, subcategory)
    for item in items:
        button_text = f"{item.name} - {item.price}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=category,
                                           subcategory=subcategory,
                                           item_id=item.id)

        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        # level = ... Мы передали тот уровень НА КОТОРЫЙ хотим переместиться
        InlineKeyboardButton(text="⬅️ Назад",
                             callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                                              category=category))
    )
    return markup


def item_keyboard(category, subcategory, item_id):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(text="Купить",
                             callback_data=buy_item_callback.new(item_id=item_id))
    )
    markup.row(
        InlineKeyboardButton(text="⬅️ Назад",
                             callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                                              category=category,
                                                              subcategory=subcategory))
    )
    return markup

