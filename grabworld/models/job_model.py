# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from grabworld.models import BaseModel


# 定义model对象:
class Job(BaseModel):
    # 表的名字:
    __tablename__ = 'job'

    # 表的结构:
    id = Column(String(64), primary_key=True)
    job_name = Column(String(32), comment='任务名称')
    finished = Column(String(8), comment='是否完成,0-完成 1-未完成')
    fail_reason = Column(String(128),nullable=True, comment='失败原因')
    create_time = Column(DATETIME, comment='创建时间', default=datetime.now)
    finish_time = Column(DATETIME, comment='完成时间')


if __name__ == '__main__':
    job = Job('spider')
    job.create_table()
