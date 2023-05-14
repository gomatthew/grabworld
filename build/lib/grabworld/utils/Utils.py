# -*- coding: utf-8 -*-
import uuid
import logging
import requests
from datetime import datetime
from grabworld import redis_store
from grabworld.models.job_model import Job
from grabworld.enum.job_enum import JobName


class Uuid():

    @property
    def uuid_1(self):
        return str(uuid.uuid1())


uuid_lib = Uuid()


def get_ip(proxy_type='https'):
    proxy = redis_store.srandmember(proxy_type, '1')
    return proxy


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
