from tgbot.services.db_api.quick_commands import add_item
from tgbot.services.items_captions import sigma14_24_cap, sigma50_cap


async def add_items():
    await add_item(id=1, name="Sigma 14-24mm", photo="-", price=1300, caption=sigma14_24_cap)
    await add_item(id=2, name="Sigma 50mm", photo="-", price=0, caption=sigma50_cap)

