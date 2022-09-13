from sqlalchemy import Column, BigInteger, String, sql, Boolean

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True, unique=True)
    full_name = Column(String(200))
    address = Column(String(200))
    phone = Column(String(50), primary_key=True, unique=True)
    answer = Column(String(500), nullable=True)
    is_admin = Column(Boolean())

    query: sql.select
