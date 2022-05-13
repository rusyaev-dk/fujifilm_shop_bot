from sqlalchemy import Column, Integer, String, sql, Sequence

from tgbot.services.db_api.db_gino import BaseModel


class Item(BaseModel):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    category_code = Column(String(20))
    category_name = Column(String(50))

    subcategory_code = Column(String(20))
    subcategory_name = Column(String(50))

    name = Column(String(50))
    price = Column(Integer)
    photo = Column(String(200))
    caption = Column(String(1000))
    detailed_inf = Column(String(200))

    query: sql.select

#     def __repr__(self):
#         return f"""
#     <b>{self.name}</b>\n\n
#     {self.caption}
# """
