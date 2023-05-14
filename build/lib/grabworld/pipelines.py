# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from grabworld import session, mysql_engine
from grabworld.models.proxy_model import ProxyPool
from grabworld.utils.Utils import datetime_lib
from sqlalchemy.dialects.mysql import insert

class GrabworldPipeline:
    def process_item(self, item, spider):
        item.insert_mysql()
        return item


class ProxyPipline:
    def process_item(self, item, spider):
        item.insert_mysql()
        # do_insert = insert(ProxyPool).values(**item)
        # on_dup = do_insert.on_duplicate_key_update(update_time=datetime_lib.now)
        # session.execute(on_dup)
        # session.commit()
        # proxy = ProxyPool()
        # # proxy.id = item.get('id')
        # proxy.ip = item.get('ip')
        # proxy.port = item.get('port')
        # proxy.location = item.get('location')
        # proxy.proxy_type = item.get('proxy_type', 'http')
        # proxy.anonymous_type = item.get('anonymous_type')
        # proxy.is_useful = item.get('is_useful')
        # proxy.create_time = item.get('create_time')
        # proxy.update_time = item.get('update_time')
        # session.add(proxy)
        # session.commit()
        return item
