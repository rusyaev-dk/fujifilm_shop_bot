from aiogram import types, Dispatcher
from tgbot.services.db_api.quick_commands import delete_items


async def delete_shop_items(message: types.Message):
    await delete_items()
    await message.answer("Таблица с товарами очищена!")


def register_process_delete_items(dp: Dispatcher):
    dp.register_message_handler(delete_items, commands="delete_items", is_admin=True, state="*")
