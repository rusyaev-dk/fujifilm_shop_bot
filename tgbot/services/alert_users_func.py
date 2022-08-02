import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from tgbot.misc.states import AlertUsers
from tgbot.services.db_api import quick_commands as db_commands


async def alert_users(message: types.Message, state: FSMContext):
    await message.answer("Что отправим пользователям?")
    await AlertUsers.Q1.set()


async def get_alert_content(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if message.photo:
        await message.bot.send_photo(chat_id=user_id, photo=message.photo[-1].file_id,
                                     caption=message.caption)
        await state.update_data(photo_id=message.photo[-1].file_id, caption=message.caption)
    elif message.text:
        await message.answer("❗️ Ваш текст на отправку пользователям:\n\n"
                             f"{message.text}")
        await state.update_data(alarm_text=message.text)
    await message.answer("Напишите <b>\"Да\"</b>, чтобы подтвердить отправку, или <b>\"Нет\"</b>, чтобы отменить"
                         " отправку:")
    await AlertUsers.next()


async def alert_confirmation(message: types.Message, state: FSMContext):
    if message.text == "Да" or message.text == "да":
        all_users = await db_commands.select_all_users()
        async with state.proxy():
            data = await state.get_data()
        photo_id = data.get("photo_id")
        if photo_id is not None:
            caption = data.get("caption")
            for user in all_users:
                await asyncio.sleep(0.3)
                await message.bot.send_photo(chat_id=user.id, photo=photo_id, caption=caption)
        else:
            text = data.get("alarm_text")
            for user in all_users:
                await asyncio.sleep(0.3)
                await message.bot.send_message(chat_id=user.id, text=text)
    else:
        await message.answer("❌ Отправка отменена.")
    await state.finish()


def register_alert_users_function(dp: Dispatcher):
    dp.register_message_handler(alert_users, commands=["send_to_users"], state="*", is_admin=True)
    dp.register_message_handler(get_alert_content, content_types=[types.ContentType.TEXT, types.ContentType.PHOTO],
                                state=AlertUsers.Q1, is_admin=True)
    dp.register_message_handler(alert_confirmation, content_types=types.ContentType.TEXT,
                                state=AlertUsers.Q2, is_admin=True)
