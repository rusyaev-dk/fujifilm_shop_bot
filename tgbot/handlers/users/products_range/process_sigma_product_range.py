from aiogram import types, Dispatcher

from tgbot.keyboards.inline.callback_datas import sigma_product_type_callback
from tgbot.keyboards.inline.product_range_kb import choose_brandkb
from tgbot.keyboards.inline.sigma_product_range_kb import spt


async def action_with_sigma_products(call: types.CallbackQuery, callback_data: dict):
    action_type = callback_data.get("type")
    user_id = call.from_user.id
    if action_type == "sigma_cancel":
        await call.bot.edit_message_text(text="Выберите бренд:",
                                         reply_markup=choose_brandkb,
                                         chat_id=user_id,
                                         message_id=call.message.message_id)
    elif action_type == "sigma_lenses":
        await call.bot.edit_message_text(text="Тут будут объективы",
                                         chat_id=user_id,
                                         message_id=call.message.message_id)

    elif action_type == "sigma_etc":
        await call.bot.edit_message_text(text="Тут будут аксессуары",
                                         chat_id=user_id,
                                         message_id=call.message.message_id)


def register_process_sigma_product_range(dp: Dispatcher):
    dp.register_callback_query_handler(action_with_sigma_products,
                                       sigma_product_type_callback.filter(type=spt), state="*")
