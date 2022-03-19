from asyncpg import UniqueViolationError

from tgbot.services.db_api.db_gino import db
from tgbot.models.user import User


async def add_user(id: int, name: str, notification: str = None):
    try:
        user = User(id=id, name=name, notification=notification)
        await user.create()
    except UniqueViolationError:
        print("Пользователь уже есть в базе данных!")
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total
