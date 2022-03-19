from aiogram import types, Dispatcher

from tgbot.keyboards.default.main_menu_kb import main_menukb
from tgbot.keyboards.inline.callback_datas import brand_choice_callback
from tgbot.keyboards.inline.fujifilm_product_range_kb import fujifilm_product_typekb
from tgbot.keyboards.inline.manfrotto_product_range_kb import manfrotto_product_typekb
from tgbot.keyboards.inline.product_range_kb import brands
from tgbot.keyboards.inline.sigma_product_range_kb import sigma_product_typekb


async def action_with_brand_choice(call: types.CallbackQuery, callback_data: dict):
    action_type = callback_data.get("type")
    user_id = call.from_user.id
    if action_type == "cancel_1":
        await call.bot.delete_message(chat_id=user_id,
                                      message_id=call.message.message_id)
        await call.message.answer("Главное меню:", reply_markup=main_menukb)
    elif action_type == "sigma":
        await call.bot.edit_message_text(text="Выберите тип товара:",
                                         reply_markup=sigma_product_typekb,
                                         chat_id=user_id,
                                         message_id=call.message.message_id)
    elif action_type == "fujifilm":
        await call.bot.edit_message_text(text="Выберите тип товара:",
                                         reply_markup=fujifilm_product_typekb,
                                         chat_id=user_id,
                                         message_id=call.message.message_id)
    elif action_type == "manfrotto":
        await call.bot.edit_message_text(text="Выберите тип товара:",
                                         reply_markup=manfrotto_product_typekb,
                                         chat_id=user_id,
                                         message_id=call.message.message_id)
    elif action_type == "colorama":
        await call.bot.edit_message_text(text="Выберите тип товара:",
                                         chat_id=user_id,
                                         message_id=call.message.message_id)


def register_process_product_range(dp: Dispatcher):
    dp.register_callback_query_handler(action_with_brand_choice,
                                       brand_choice_callback.filter(type=brands), state="*")
