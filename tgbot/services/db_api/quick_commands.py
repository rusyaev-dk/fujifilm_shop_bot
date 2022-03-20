from typing import List

from asyncpg import UniqueViolationError
from sqlalchemy import and_

from tgbot.models.item import Item
from tgbot.services.db_api.db_gino import db
from tgbot.models.user import User


async def add_user(id: int, name: str, notification: str = None):
    try:
        user = User(id=id, name=name, notification=notification)
        await user.create()
    except UniqueViolationError:
        print("Пользователь уже есть в базе данных!")
        pass


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


# async def add_item(**kwargs):
#     try:
#         item = Item(**kwargs)
#         await item.create()
#     except Exception as e:
#         print(e)
#         pass


# async def get_items(category, subcategory) -> List[Item]:
#     items = await Item.query.where(
#         and_(Item.category == category,
#              Item.subcategory == subcategory)
#     ).gino.all()
#     return items
async def add_item(**kwargs):
    new_item = await Item(**kwargs).create()
    return new_item


async def get_categories() -> List[Item]:
    return await Item.query.distinct(Item.category_name).gino.all()


# Функция для вывода товаров с РАЗНЫМИ подкатегориями в выбранной категории
async def get_subcategories(category) -> List[Item]:
    return await Item.query.distinct(Item.subcategory_name).where(Item.category_code == category).gino.all()


# Функция вывода всех товаров, которые есть в переданных категории и подкатегории
async def get_items(category_code, subcategory_code) -> List[Item]:
    item = await Item.query.where(
        and_(Item.category_code == category_code,
             Item.subcategory_code == subcategory_code)
    ).gino.all()
    return item


# Функция для получения объекта товара по его айди
async def get_item(item_id) -> Item:
    item = await Item.query.where(Item.id == item_id).gino.first()
    return item
