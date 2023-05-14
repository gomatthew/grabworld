# -*- coding: utf-8 -*-

from grabworld import session, Base
from grabworld import get_mysql_engine


class BaseModel(Base):
    __abstract__ = True

    def __init__(self, database='spider', **kwargs):
        self.engine = get_mysql_engine(database)
        if kwargs:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    @classmethod
    def create_obj(cls, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()

    def create_table(self):
        Base.metadata.drop_all(bind=self.engine, tables=[self.__table__], checkfirst=True)
        Base.metadata.create_all(bind=self.engine, tables=[self.__table__], checkfirst=True)
