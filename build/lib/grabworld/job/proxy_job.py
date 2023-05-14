# -*- coding: utf-8 -*-
import re
import traceback
import requests
from sqlalchemy.sql import and_, or_
from grabworld import redis_store, session
from grabworld.models.proxy_model import ProxyPool
from grabworld.utils.Utils import job_record, datetime_lib, logger
from grabworld.enum.job_enum import JobName


class ProxyJob(object):
    @staticmethod
    def proxy_update_job_inner(http_type):
        try:
            match http_type:
                case 'http':
                    query_proxy_available = session.query(ProxyPool).filter(
                        or_(ProxyPool.is_useful == '1', ProxyPool.is_useful == '3')).limit(100).all()
                    redis_store.delete(http_type)
                    proxy_available = [obj.proxy() for obj in query_proxy_available]
                    redis_store.sadd(http_type, *proxy_available)
                    return
                case 'https':
                    query_proxy_available = session.query(ProxyPool).filter(
                        or_(ProxyPool.is_useful == '2', ProxyPool.is_useful == '3')).limit(100).all()
                    redis_store.delete(http_type)
                    proxy_available = [obj.proxy() for obj in query_proxy_available]
                    redis_store.sadd(http_type, *proxy_available)
                    return
                case _:
                    return
        except:
            return

    @staticmethod
    @job_record
    def proxy_update_job():
        logger.info(f"开始激活任务:{JobName.PROXY_UPDATE.value}")
        # 更新并维护 Redis 内可用代理,每5分钟执行一次
        try:
            ProxyJob.proxy_update_job_inner('http')
            ProxyJob.proxy_update_job_inner('https')
            # proxy_available_https = session.query(ProxyPool).filter(
            #     and_(ProxyPool.is_useful == '1', ProxyPool.proxy_type == 'https')).limit(100).all()
            # proxy_available_http = session.query(ProxyPool).filter(
            #     and_(ProxyPool.is_useful == '1', ProxyPool.proxy_type == 'http')).limit(100).all()
            # redis_store.delete('http')
            # redis_store.delete('https')
            # redis_store.sadd('http', *proxy_available_http)
            # redis_store.sadd('https', *proxy_available_https)
            # Job.create_obj(id=uuid_lib.uuid_1, job_name=JobName.PROXY_UPDATE.name, finished=0, fail_reason=None,
            #                create_time=start_time, finish_time=finish_time)
            return 0, None, JobName.PROXY_UPDATE.name
        except BaseException as e:
            # Job.create_obj(id=uuid_lib.uuid_1, job_name=JobName.PROXY_UPDATE.name, finished=1, fail_reason=e,
            #                create_time=start_time, finish_time=None)
            print(traceback.format_exc())
            return 1, e, JobName.PROXY_UPDATE.name

    @staticmethod
    @job_record
    def proxy_judge_job():
        logger.info(f"开始激活任务:{JobName.PROXY_JUDGE.value}")
        try:
            def judge_http_proxy(proxy):
                proxies = {
                    "http": f"http://{proxy}"
                }
                try:
                    # logger.info(f'正在研判ip:http://{proxy}')
                    resp = requests.get('http://www.baidu.com/', proxies=proxies, timeout=5)
                    logger.info('http success!')
                    return 1 if int(resp.status_code) == 200 else 0
                except BaseException as e:
                    logger.error(e)
                    return 0

            def judge_https_proxy(proxy):
                proxies = {
                    "https": f"http://{proxy}"
                }
                try:
                    resp = requests.get('https://www.baidu.com/', proxies=proxies, timeout=5)
                    logger.info('https success!')
                    return 2 if int(resp.status_code) == 200 else 0
                except BaseException as e:
                    logger.error(e)
                    return 0

            proxy_need_judge = session.query(ProxyPool).filter(ProxyPool.is_useful == '0').limit(100).all()
            for _proxy_obj in proxy_need_judge:
                logger.info(f'test ip :{_proxy_obj.proxy()}')
                http_status = judge_http_proxy(_proxy_obj.proxy())
                https_status = judge_https_proxy(_proxy_obj.proxy())
                status = https_status + http_status
                mat_obj = re.match(r'(.*):(.*)', _proxy_obj.proxy())
                query_obj = session.query(ProxyPool).filter(
                    and_(ProxyPool.ip == mat_obj.group(1), ProxyPool.port == mat_obj.group(2))).first()
                query_obj.update_time = datetime_lib.now
                query_obj.is_useful = status if status != 0 else -1
                session.add(query_obj)
                session.commit()
            logger.info('mysql commit!')
            # session.commit()
            return 0, None, JobName.PROXY_JUDGE.name
        except BaseException as e:
            return 1, e, JobName.PROXY_JUDGE.name
        finally:
            session.commit()
