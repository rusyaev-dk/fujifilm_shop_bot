from typing import Union

from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove

from tgbot.keyboards.default.write_review_kb import review_menu
from tgbot.keyboards.inline.generate_keyboards import item_keyboard, subcategories_keyboard, categories_keyboard, \
    items_keyboard, menu_callback
from tgbot.misc.states import Review
from tgbot.services.db_api import quick_commands as commands


async def show_product_range(message: types.Message):
    await message.answer("Наш магазин является официальным дистрибьютором таких"
                         " брендов, как: Fujifilm, Sigma, Colorama, Manfrotto.", reply_markup=ReplyKeyboardRemove())
    await list_categories(message)


async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await categories_keyboard()
    if isinstance(message, types.Message):
        await message.answer("Выберите бренд:", reply_markup=markup)
    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_text(text="Выберите бренд:", reply_markup=markup)


async def list_subcategories(call: types.CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)
    await call.message.edit_text(text="Выберите категорию:", reply_markup=markup)


async def list_items(call: types.CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category, subcategory)
    await call.message.edit_text("Выберите продукт:", reply_markup=markup)


async def show_item(call: types.CallbackQuery, category, subcategory, item_id):
    markup = item_keyboard(category=category, subcategory=subcategory, item_id=item_id)

    item = await commands.get_item(item_id=item_id)
    text = f"Купи {item.name}"
    await call.message.edit_text(text, reply_markup=markup)


async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get("level")
    category = callback_data.get("category")
    subcategory = callback_data.get("subcategory")
    item_id = int(callback_data.get("item_id"))
    cancel = callback_data.get("cancel")

    levels = {
        "0": list_categories,
        "1": list_subcategories,
        "2": list_items,
        "3": show_item
    }

    current_level_function = levels[current_level]

    await current_level_function(call, category=category,
                                 subcategory=subcategory, item_id=item_id)


async def write_review(message: types.Message):
    await message.answer("📨 Напишите свой отзыв:",
                         reply_markup=review_menu)
    await Review.Q1.set()


def register_process_main_menu(dp: Dispatcher):
    dp.register_message_handler(show_product_range, text="📷 Ассортимент", state="*")
    dp.register_callback_query_handler(navigate, menu_callback.filter(), state="*")
    dp.register_message_handler(write_review, text="✍️ Оставить отзыв", state="*")
