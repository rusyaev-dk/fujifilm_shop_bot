from aiogram import types, Dispatcher

from tgbot.keyboards.inline.callback_datas import colorama_product_type_callback
from tgbot.keyboards.inline.colorama_product_range_kb import clrmpt
from tgbot.keyboards.inline.product_range_kb import choose_brandkb


async def action_with_colorama_products(call: types.CallbackQuery, callback_data: dict):
    action_type = callback_data.get("type")
    user_id = call.from_user.id
    if action_type == "colorama_cancel":
        await call.bot.edit_message_text(text="Выберите бренд:",
                                         reply_markup=choose_brandkb,
                                         chat_id=user_id,
                                         message_id=call.message.message_id)
    elif action_type == "colorama_backgrounds":
        await call.bot.edit_message_text(text="Тут будут фоны",
                                         chat_id=user_id,
                                         message_id=call.message.message_id)


def register_process_colorama_product_range(dp: Dispatcher):
    dp.register_callback_query_handler(action_with_colorama_products,
                                       colorama_product_type_callback.filter(type=clrmpt), state="*")
