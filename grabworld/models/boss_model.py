# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, String
from grabworld import Base


# 定义User对象:
class Boss(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
