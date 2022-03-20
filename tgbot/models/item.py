from sqlalchemy import Column, Integer, String, sql, Sequence

from tgbot.services.db_api.db_gino import BaseModel

# beta version:
# class Item(BaseModel):
#     __tablename__ = "products"
#
#     id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
#     category_code = Column(String(20))
#     category_name = Column(String(50))
#
#     subcategory_code = Column(String(20))
#     subcategory_name = Column(String(50))
#
#     name = Column(String(50))
#     photo = Column(String(100))
#     caption = Column(String(500))
#     price = Column(Integer)
#
#     query: sql.select


class Item(BaseModel):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Integer)
    photo = Column(String(100))
    caption = Column(String(500))

    query: sql.select
