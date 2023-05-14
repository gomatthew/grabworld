# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, DATETIME, Float, DATE

from grabworld.models import BaseModel


# 定义User对象:
class StockModel(BaseModel):
    # 表的名字:
    __tablename__ = 'stock_tong_hua_shun'

    def __init__(self):
        super(StockModel, self).__init__('spider')

    id = Column(Integer, autoincrement=True, primary_key=True, comment='id编码')
    code = Column(String(32), comment='股票代码')
    stock_name = Column(String(32), comment='股票名称')
    price = Column(Float(), nullable=False, comment='价格')
    price_date = Column(DATE, nullable=False, comment='价格日期')
    rase_fall_percent = Column(Float(), nullable=False, comment='涨跌幅(百分比)')
    rase_fall_price = Column(Float(), nullable=False, comment='涨跌')
    rase_fall_speed = Column(Float(), nullable=False, comment='涨速(百分比)')
    turn_over = Column(Float(), nullable=False, comment='换手(百分比)')
    equivalent_ratio = Column(String(32), comment='量比')
    amplitude = Column(Float(), comment='振幅(百分比)')
    transaction_volume = Column(String(32), comment='成交额')
    floating_stock = Column(String(32), comment='流通股')
    circulation_market_value = Column(String(32), comment='流通市值')
    pe_ratio = Column(String(32), comment='市盈率')
    create_time = Column(DATETIME, comment='创建时间')
    update_time = Column(DATETIME, comment='更新时间')

    def show_profile(self):
        return "{0}:{1}:{2}:{3}".format(self.price_date, self.code, self.stock_name, self.price)


if __name__ == '__main__':
    table_model = StockModel()
    table_model.create_table()
