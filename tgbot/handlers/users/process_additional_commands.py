from aiogram import types, Dispatcher


async def help_command(message: types.Message):
    await message.answer("🔹 Если у Вас возникли проблемы с использованием бота, попробуйте перезапустить его, "
                         "нажав на /start.\n\n"
                         "👨‍💻 Если это не помогло, обратитесь в поддержку - @dnrvv, мы онлайн 24/7!")


def register_process_additional_commands(dp: Dispatcher):
    dp.register_message_handler(help_command, commands="help", state="*")
