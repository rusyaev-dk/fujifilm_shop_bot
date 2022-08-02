from aiogram import types, Dispatcher
from tgbot.services.db_api import quick_commands as commands


async def statistics(message: types.Message):
    amount_of_users = await commands.count_users()
    await message.answer(f"В боте зарегистрировано<b>{amount_of_users}</b> пользователей")


def register_statistics_function(dp: Dispatcher):
    dp.register_message_handler(statistics, commands=["statistics"], is_admin=True, state="*")
