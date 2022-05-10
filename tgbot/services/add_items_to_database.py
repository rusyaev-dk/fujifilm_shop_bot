from tgbot.services.db_api.quick_commands import add_item
from tgbot.services.items_captions import *


async def add_items():
    await add_item(name="Sigma 14-24mm",
                   category_name="Sigma", category_code="sigma",
                   subcategory_name="Объективы", subcategory_code="lens",
                   price=1300, photo=sigma14_24_ph, caption=sigma14_24_cap)
    await add_item(name="Sigma 50mm",
                   category_name="Sigma", category_code="sigma",
                   subcategory_name="Объективы", subcategory_code="lens",
                   price=1300, photo="-", caption=sigma50_cap)
    await add_item(name="Sigma 18-35mm",
                   category_name="Sigma", category_code="sigma",
                   subcategory_name="Объективы", subcategory_code="lens",
                   price=720, photo="-", caption=sigma18_35_cap)
    await add_item(name="Fujifilm X-T3",
                   category_name="Fujifilm", category_code="fuji",
                   subcategory_name="Камеры", subcategory_code="cameras",
                   price=2000, photo="-", caption=fuji_xt3_cap)
    await add_item(name="Fujifilm X-T4",
                   category_name="Fujifilm", category_code="fuji",
                   subcategory_name="Камеры", subcategory_code="cameras",
                   price=2000, photo="-", caption=fuji_xt4_cap)
    await add_item(name="FUJINON XF35mm",
                   category_name="Fujifilm", category_code="fuji",
                   subcategory_name="Объективы", subcategory_code="lens",
                   price=2000, photo="-", caption=fuji_xf35_cap)
    await add_item(name="FUJINON XF33mm",
                   category_name="Fujifilm", category_code="fuji",
                   subcategory_name="Объективы", subcategory_code="lens",
                   price=2000, photo="-", caption=fuji_xf33_cap)
    await add_item(name="Pro Light PV-610",
                   category_name="Manfrotto", category_code="manfr",
                   subcategory_name="Сумки", subcategory_code="bags",
                   price=0, photo="-", caption=manf_PV_610_cap)
