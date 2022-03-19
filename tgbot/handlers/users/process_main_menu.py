from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove

from tgbot.keyboards.default.write_review_kb import review_menu
from tgbot.keyboards.inline.callback_datas import brand_choice_callback
from tgbot.keyboards.inline.product_range_kb import choose_brandkb
from tgbot.misc.states import Review


async def show_product_range(message: types.Message):
    await message.answer("ТРататара", reply_markup=ReplyKeyboardRemove())
    await message.answer("Выберите бренд:", reply_markup=choose_brandkb)


async def write_review(message: types.Message):
    await message.answer("📨 Напишите свой отзыв:",
                         reply_markup=review_menu)
    await Review.Q1.set()


def register_process_main_menu(dp: Dispatcher):
    dp.register_message_handler(show_product_range, text="📷 Ассортимент", state="*")
    dp.register_message_handler(write_review, text="✍️ Оставить отзыв", state="*")
