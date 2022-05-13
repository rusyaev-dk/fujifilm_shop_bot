from asyncpg import UniqueViolationError
from sqlalchemy.exc import IntegrityError

from tgbot.services.db_api.quick_commands import add_item
from tgbot.services.items_info import *


async def add_items():
    await add_item(id=1, name="Sigma 14-24mm",
                   category_name="Sigma", category_code="sigma",
                   subcategory_name="Объективы", subcategory_code="lens",
                   price=1300, photo=sigma14_24_ph, caption=sigma14_24_cap, detailed_inf=sigma14_24_inf)
    await add_item(id=2, name="Sigma 50mm",
                   category_name="Sigma", category_code="sigma",
                   subcategory_name="Объективы", subcategory_code="lens",
                   price=1300, photo=sigma50_ph, caption=sigma50_cap, detailed_inf=sigma50_inf)
    await add_item(id=3, name="Sigma 18-35mm",
                   category_name="Sigma", category_code="sigma",
                   subcategory_name="Объективы", subcategory_code="lens",
                   price=720, photo=sigma18_35_ph, caption=sigma18_35_cap, detailed_inf=sigma18_35_inf)
    await add_item(id=4, name="Fujifilm X-T3",
                   category_name="Fujifilm", category_code="fuji",
                   subcategory_name="Камеры", subcategory_code="cameras",
                   price=2000, photo="-", caption=fuji_xt3_cap)
    await add_item(id=5, name="Fujifilm X-T4",
                   category_name="Fujifilm", category_code="fuji",
                   subcategory_name="Камеры", subcategory_code="cameras",
                   price=2000, photo="-", caption=fuji_xt4_cap)
    await add_item(id=6, name="FUJINON XF35mm",
                   category_name="Fujifilm", category_code="fuji",
                   subcategory_name="Объективы", subcategory_code="lens",
                   price=2000, photo="-", caption=fuji_xf35_cap)
    await add_item(id=7, name="FUJINON XF33mm",
                   category_name="Fujifilm", category_code="fuji",
                   subcategory_name="Объективы", subcategory_code="lens",
                   price=2000, photo="-", caption=fuji_xf33_cap)
    await add_item(id=8, name="Pro Light PV-610",
                   category_name="Manfrotto", category_code="manfr",
                   subcategory_name="Сумки", subcategory_code="bags",
                   price=0, photo="-", caption=manf_PV_610_cap)
    await add_item(id=9, name="Pro Light PV-6102",
                   category_name="Manfrotto", category_code="manfr",
                   subcategory_name="Сумки", subcategory_code="bags",
                   price=0, photo="-", caption=manf_PV_610_cap)
