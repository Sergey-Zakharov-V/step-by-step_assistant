from sqlalchemy import Column, BIGINT, String

from database import Base


class Users(Base):
    __tablename__ = "Users"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    telegram_id = Column(String, unique=True, nullable=False)
    friend = Column(String, nullable=True)
    link_royalfamily = Column(String, nullable=True)
    link_roboforex = Column(String, nullable=True)
    link_forex4you = Column(String, nullable=True)
