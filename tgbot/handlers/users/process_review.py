from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.default.main_menu_kb import main_menukb
from tgbot.keyboards.default.write_review_kb import review_stars
from tgbot.misc.states import Review
from tgbot.services.notifications.notify_admins import bot_admins


async def back_to_menu_review(message: types.Message, state: FSMContext):
    await message.answer("Главное меню:", reply_markup=main_menukb)
    await state.finish()


async def w_review(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer("⭐️ Пожалуйста, оцените бота по пятибалльной шкале, "
                         "выбрав кнопку ниже:",
                         reply_markup=review_stars)
    await Review.next()


async def pick_stars(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer, mention=message.from_user.get_mention())
    await message.answer("📩 Спасибо, Ваш отзыв был отправлен!",
                         reply_markup=main_menukb)
    async with state.proxy() as data:
        mention = data.get("mention")
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    await state.finish()
    await message.bot.send_message(chat_id=bot_admins[0], text=f"Пользователь {mention} прислал отзыв: {answer1}\n"
                                                               f"Его оценка: {answer2}", parse_mode="HTML")


def register_process_review(dp: Dispatcher):
    dp.register_message_handler(back_to_menu_review, text="⬅️ Назад", state=Review.Q1)
    dp.register_message_handler(w_review, content_types=types.ContentType.TEXT, state=Review.Q1)
    dp.register_message_handler(pick_stars, content_types=types.ContentType.TEXT, state=Review.Q2)
