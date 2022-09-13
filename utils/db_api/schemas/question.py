from sqlalchemy import Column, BigInteger, String, sql, PickleType

from utils.db_api.db_gino import TimedBaseModel


class Question(TimedBaseModel):
    __tablename__ = 'question'
    id = Column(BigInteger(), primary_key=True)
    question_text = Column(String(500), nullable=True)
    question_audio = Column(PickleType(), nullable=True)
    question_voice = Column(PickleType(), nullable=True)

    query: sql.select
