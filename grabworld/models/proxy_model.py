# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, DATETIME

from grabworld.models import BaseModel


# 定义User对象:
class ProxyPool(BaseModel):
    # 表的名字:
    __tablename__ = 'proxy_pool'
    id = Column(Integer, nullable=False, comment='id编码', unique=True, autoincrement=True, )
    ip = Column(String(32), primary_key=True, comment='ip地址')
    port = Column(String(8), comment='端口')
    location = Column(String(32), comment='代理位置')
    proxy_type = Column(String(4), comment='代理类型')
    anonymous_type = Column(String(4), comment='匿名类型')
    is_useful = Column(String(4), comment='0-默认的,1-可用,-1 -不可用')
    create_time = Column(DATETIME, comment='创建时间')
    update_time = Column(DATETIME, comment='更新时间')

    def proxy(self):
        return "{0}:{1}".format(self.ip, self.port)


if __name__ == '__main__':
    proxy_pool = ProxyPool()
    proxy_pool.create_table()
