from sqlalchemy import Column, BigInteger, String, sql

from tgbot.services.db_api.db_gino import TimeBaseModel


class User(TimeBaseModel):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    notification = Column(String(100))

    query: sql.Select
