from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.inline.additional_keyboards import main_menu_kb, review_callback, review_actions, \
    contacts_callback, contacts_actions
from tgbot.misc.states import Review
from tgbot.services.notifications.notify_admins import bot_admins


async def review_navigate(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    action_type = callback_data.get("action")
    if action_type == "cancel_review":
        await call.answer(text="❌ Отправка отзыва отменена", show_alert=False)
        await call.bot.edit_message_text(text="Главное меню:", chat_id=call.from_user.id,
                                         message_id=call.message.message_id, reply_markup=main_menu_kb)
        await state.finish()


async def send_review(message: types.Message, state: FSMContext):
    answer = message.text
    mention = message.from_user.get_mention()
    async with state.proxy():
        data = await state.get_data()
    msg_to_del = int(data.get("msg_to_del"))
    await message.bot.delete_message(chat_id=message.from_user.id, message_id=msg_to_del)
    await message.answer("📩 Спасибо, Ваш отзыв был отправлен администрации!\n"
                         "Главное меню:",
                         reply_markup=main_menu_kb)
    await message.bot.send_message(chat_id=bot_admins[0], text=f"Пользователь {mention} прислал отзыв: {answer}\n")
    await state.finish()


async def contacts_navigate(call: types.CallbackQuery, callback_data: dict):
    action_type = callback_data.get("action")
    if action_type == "cancel_contacts":
        await call.bot.edit_message_text(text="Главное меню:", chat_id=call.from_user.id,
                                         message_id=call.message.message_id, reply_markup=main_menu_kb)


def register_process_mm_sections(dp: Dispatcher):
    dp.register_callback_query_handler(review_navigate, review_callback.filter(action=review_actions), state=Review.Q1)
    dp.register_message_handler(send_review, content_types=types.ContentType.TEXT, state=Review.Q1)
    dp.register_callback_query_handler(contacts_navigate, contacts_callback.filter(action=contacts_actions), state="*")
