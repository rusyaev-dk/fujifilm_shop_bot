from aiogram import types, Dispatcher

from tgbot.keyboards.inline.callback_datas import fujifilm_product_type_callback
from tgbot.keyboards.inline.fujifilm_product_range_kb import fjpt
from tgbot.keyboards.inline.product_range_kb import choose_brandkb


async def action_with_fujifilm_products(call: types.CallbackQuery, callback_data: dict):
    action_type = callback_data.get("type")
    user_id = call.from_user.id
    if action_type == "fujifilm_cancel":
        await call.bot.edit_message_text(text="Выберите бренд:",
                                         reply_markup=choose_brandkb,
                                         chat_id=user_id,
                                         message_id=call.message.message_id)
    elif action_type == "fujifilm_cameras":
        await call.bot.edit_message_text(text="Тут будут камеры",
                                         chat_id=user_id,
                                         message_id=call.message.message_id)
    elif action_type == "fujifilm_lenses":
        await call.bot.edit_message_text(text="Тут будут объективы",
                                         chat_id=user_id,
                                         message_id=call.message.message_id)
    elif action_type == "fujifilm_etc":
        await call.bot.edit_message_text(text="Тут будет прочее",
                                         chat_id=user_id,
                                         message_id=call.message.message_id)


def register_process_fujifilm_product_range(dp: Dispatcher):
    dp.register_callback_query_handler(action_with_fujifilm_products,
                                       fujifilm_product_type_callback.filter(type=fjpt), state="*")
