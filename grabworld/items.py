# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from sqlalchemy.dialects.mysql import insert
from grabworld import session
from grabworld.models.proxy_model import ProxyPool
from grabworld.models.stock_model import StockModel
from grabworld.utils.Utils import datetime_lib


class GrabworldItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    brief = scrapy.Field()
    text = scrapy.Field()

    create_time = scrapy.Field()
    update_time = scrapy.Field()


class ProxyItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    location = scrapy.Field()
    proxy_type = scrapy.Field()
    anonymous_type = scrapy.Field()
    is_useful = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()

    def insert_mysql(self):
        do_insert = insert(ProxyPool).values(**dict(self.items()))
        # {'ip': self.ip, 'port': self.port, 'location': self.location, 'proxy_type': self.proxy_type,
        #  'anonymous_type': self.anonymous_type,'is_useful':self.is_useful,'create_time':self.create_time,'update_time':self.update_time })
        on_dup = do_insert.on_duplicate_key_update(update_time=datetime_lib.now)
        session.execute(on_dup)
        session.commit()


class StockItem(scrapy.Item):
    id = scrapy.Field()
    code = scrapy.Field()
    stock_name = scrapy.Field()
    price = scrapy.Field()
    price_date = scrapy.Field()
    rase_fall_percent = scrapy.Field()
    rase_fall_price = scrapy.Field()
    rase_fall_speed = scrapy.Field()
    turn_over = scrapy.Field()
    equivalent_ratio = scrapy.Field()
    amplitude = scrapy.Field()
    transaction_volume = scrapy.Field()
    floating_stock = scrapy.Field()
    circulation_market_value = scrapy.Field()
    pe_ratio = scrapy.Field()
    source_page = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()

    def insert_mysql(self):
        do_insert = insert(StockModel).values(**dict(self.items()))
        # {'ip': self.ip, 'port': self.port, 'location': self.location, 'proxy_type': self.proxy_type,
        #  'anonymous_type': self.anonymous_type,'is_useful':self.is_useful,'create_time':self.create_time,'update_time':self.update_time })
        on_dup = do_insert.on_duplicate_key_update(update_time=datetime_lib.now)
        session.execute(on_dup)
        session.commit()


class BaseItemLoader(ItemLoader):
    pass
