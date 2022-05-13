from aiogram import types, Dispatcher


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Перезапустить бота"),
            types.BotCommand("help", "Помощь"),
        ]
    )
