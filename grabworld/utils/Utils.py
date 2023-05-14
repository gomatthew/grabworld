# -*- coding: utf-8 -*-
import uuid
import time
import logging
import random
import requests
from datetime import datetime
from grabworld import redis_store, session
from grabworld.models.job_model import Job
from grabworld.settings import DOWNLOAD_DELAY
from grabworld.models.proxy_model import ProxyPool
from sqlalchemy import and_

class Uuid():

    @property
    def uuid_1(self):
        return str(uuid.uuid1())


uuid_lib = Uuid()


def get_ip(proxy_type='https', num=1, domin=''):
    # proxies = redis_store.srandmember(proxy_type, num)
    proxies = redis_store.sdiff("http", f"{domin}:blacklist")
    if proxies:
        proxies = random.sample(proxies, k=num)
        for p in proxies:
            last_use_time = int(redis_store.get(f"{domin}:{p}")) if redis_store.get(f"{domin}:{p}") else None
            # available_proxy = redis_store.sdiff("http", f"{domin}:blacklist")
            # if available_proxy:
            # black_list = redis_store.sismember(f"{domin}:blacklist", f"{proxy_type}://{p}")
            if last_use_time and round(time.time()) - last_use_time < DOWNLOAD_DELAY:
                # 上次用了，还没到时间
                proxies.remove(p)
                if len(proxies) == 0:
                    return get_ip(proxy_type, num, domin)
        proxy = [proxy_ for proxy_ in proxies]
        [redis_store.set(f"{domin}:{x}", round(time.time()), ex=DOWNLOAD_DELAY) for x in proxies]
        # [redis_store.hset(domin, x, round(time.time())) for x in proxies]
        return proxy[0] if num == 1 and proxy else proxy
    return


def set_proxy_blacklist(domin, proxy):
    redis_store.sadd(domin, proxy)
    ip,port = proxy.split('//')[-1].split(':')
    proxy_obj = session.query(ProxyPool).filter(and_(ProxyPool.ip == ip,ProxyPool.port==port)).first()
    proxy_obj.is_useful = -1
    session.commit()
    return


def get_proxy_count(proxy_type='https'):
    count = redis_store.scard(proxy_type)
    return count if count else 1


class DateTimeLib(object):

    @property
    def now(self):
        return datetime.now().strftime('%Y-%m-%d %X')

    @property
    def today(self):
        return datetime.now().strftime('%Y-%m-%d')


datetime_lib = DateTimeLib()


def judge_proxy_available(proxy):
    def http_test():
        proxies = {
            "http": f'http://{proxy}'
            # "https":"https://ip:端口号"
        }
        try:
            resp = requests.get('http://www.baidu.com/', proxies=proxies, timeout=5)
            code = resp.status_code
            if 200 <= code < 300:
                code = 200
        except:
            logging.info(f'{proxy} is not available!')
            return 500
        return code

    def https_test():
        proxies = {
            "https": f'https://{proxy}'
            # "https":"https://ip:端口号"
        }
        try:
            resp = requests.get('https://www.baidu.com/', proxies=proxies)
            code = int(resp.status_code)
            if 200 <= code < 300:
                code = 200
        except:
            logging.info(f'{proxy} is not available!')
            return 500
        return code

    http_code = http_test()
    # https_code = https_test()
    return http_code  # {'http':'200','https':'500'}


# 记录任务执行结果
def job_record(job):
    def inner():
        start_time = datetime_lib.now
        finished, fail_reason, job_name = job()
        finish_time = datetime_lib.now
        # 记录执行结果
        Job.create_obj(id=uuid_lib.uuid_1, job_name=job_name, finished=finished,
                       fail_reason=fail_reason, create_time=start_time, finish_time=finish_time)

    return inner


# 日志相关
logging.basicConfig(
    # 1、日志输出位置：1、终端 2、文件
    # filename='access.log', # 不指定，默认打印到终端

    # 2、日志格式
    # format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    format='%(asctime)s - %(levelname)s -%(module)s:  %(message)s',

    # 3、时间格式
    datefmt='%Y-%m-%d %H:%M:%S %p',

    # 4、日志级别
    # critical => 50
    # error => 40
    # warning => 30
    # info => 20
    # debug => 10
    level=20,
)
logger = logging.getLogger(__name__)
