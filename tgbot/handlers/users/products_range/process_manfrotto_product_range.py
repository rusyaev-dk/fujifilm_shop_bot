from aiogram import types, Dispatcher

from tgbot.keyboards.inline.callback_datas import manfrotto_product_type_callback
from tgbot.keyboards.inline.manfrotto_product_range_kb import manfpt
from tgbot.keyboards.inline.product_range_kb import choose_brandkb


async def action_with_manfrotto_products(call: types.CallbackQuery, callback_data: dict):
    action_type = callback_data.get("type")
    user_id = call.from_user.id
    if action_type == "manfrotto_cancel":
        await call.bot.edit_message_text(text="Выберите бренд:",
                                         reply_markup=choose_brandkb,
                                         chat_id=user_id,
                                         message_id=call.message.message_id)
    elif action_type == "manfrotto_studio":
        await call.bot.edit_message_text(text="Тут будет все для студии",
                                         chat_id=user_id,
                                         message_id=call.message.message_id)
    elif action_type == "manfrotto_bags":
        await call.bot.edit_message_text(text="Тут будут сумки",
                                         chat_id=user_id,
                                         message_id=call.message.message_id)


def register_process_manfrotto_product_range(dp: Dispatcher):
    dp.register_callback_query_handler(action_with_manfrotto_products,
                                       manfrotto_product_type_callback.filter(type=manfpt), state="*")
