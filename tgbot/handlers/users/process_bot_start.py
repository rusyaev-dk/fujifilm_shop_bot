from aiogram import Dispatcher
from aiogram.types import Message


from tgbot.keyboards.inline.additional_keyboards import main_menu_kb
from tgbot.misc.throttling_function import rate_limit
from tgbot.services.db_api import quick_commands as commands


@rate_limit(5)
async def user_start_bot(message: Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!\n"
                         f"Главное меню:",
                         reply_markup=main_menu_kb)

    await commands.add_user(id=message.from_user.id,
                            name=message.from_user.full_name)


def register_process_bot_start(dp: Dispatcher):
    dp.register_message_handler(user_start_bot, commands=["start"], state="*")
