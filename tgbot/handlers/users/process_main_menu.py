from typing import Union

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.inline.generate_keyboards import item_keyboard, subcategories_keyboard, categories_keyboard, \
    items_keyboard, menu_callback
from tgbot.keyboards.inline.additional_keyboards import main_menu_callback, mm_sections, contacts_kb, review_kb, \
    main_menu_kb
from tgbot.misc.states import Review
from tgbot.services.db_api import quick_commands as commands


async def back_to_main_menu(call: types.CallbackQuery, category="0", subcategory="0", item_id="0"):
    await call.bot.edit_message_text(text="Главное меню:", chat_id=call.from_user.id,
                                     message_id=call.message.message_id, reply_markup=main_menu_kb)


async def main_menu_navigate(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    section = callback_data.get("section")
    if section == "stock":
        await list_categories(call)
    elif section == "contacts":
        await call.bot.edit_message_text(text="Тут будет контактная информация...", chat_id=call.from_user.id,
                                         message_id=call.message.message_id, reply_markup=contacts_kb)
    elif section == "review":
        await Review.Q1.set()
        await call.bot.edit_message_text(text="📨 Напишите свой отзыв:", chat_id=call.from_user.id,
                                         message_id=call.message.message_id, reply_markup=review_kb)
        await state.update_data(msg_to_del=f"{call.message.message_id}")


async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await categories_keyboard()
    if isinstance(message, types.Message):
        await message.answer("🔹 Выберите бренд:", reply_markup=markup)
    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_text(text="🔹 Выберите бренд:", reply_markup=markup)


async def list_subcategories(call: types.CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)
    await call.message.edit_text(text="🔹 Выберите категорию:", reply_markup=markup)


async def list_items(call: types.CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category, subcategory)
    # await call.bot.delete_message(chat_id=call.from_user.id,
    #                               message_id=call.message.message_id)
    # await call.message.answer(text="🔹 Выберите продукт:",
    #                           reply_markup=markup)
    await call.message.edit_text(text="🔹 Выберите продукт:",
                                 reply_markup=markup)


async def show_item(call: types.CallbackQuery, category, subcategory, item_id):
    markup = await item_keyboard(category=category, subcategory=subcategory, item_id=item_id)
    user_id = call.from_user.id
    item = await commands.get_item(item_id=item_id)
    text = (f"<b>{item.name}</b>\n\n"
            f"{item.caption}")
    photo = f"{item.photo}"
    await call.bot.delete_message(chat_id=user_id,
                                  message_id=call.message.message_id)
    await call.bot.send_photo(photo=photo,
                              chat_id=user_id,
                              caption=text)
    await call.message.answer(text="🔹 Выберите действие:",
                              reply_markup=markup)


async def global_navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get("level")
    category = callback_data.get("category")
    subcategory = callback_data.get("subcategory")
    item_id = int(callback_data.get("item_id"))

    levels = {
        "-1": back_to_main_menu,
        "0": list_categories,
        "1": list_subcategories,
        "2": list_items,
        "3": show_item
    }

    current_level_function = levels[current_level]

    await current_level_function(call, category=category,
                                 subcategory=subcategory, item_id=item_id)


def register_process_main_menu(dp: Dispatcher):
    dp.register_callback_query_handler(main_menu_navigate, main_menu_callback.filter(section=mm_sections), state="*")
    dp.register_callback_query_handler(global_navigate, menu_callback.filter(), state="*")
