# -*- coding: utf-8 -*-
import time

from grabworld import job_scheduler
from grabworld.utils.Utils import logger, datetime_lib
from grabworld.job.proxy_job import ProxyJob


class JobManager(object):

    def __init__(self):
        logger.info("开始初始化任务管理器...")
        job_list = self.job_list()
        logger.info(f"任务列表:{job_list}")
        # self.job_start()

    def job_start(self):
        job_scheduler.add_job(ProxyJob.proxy_update_job, 'interval', minutes=5, next_run_time=datetime_lib.now,
                              replace_existing=True)
        job_scheduler.add_job(ProxyJob.proxy_judge_job, 'interval', minutes=5, next_run_time=datetime_lib.now,
                              replace_existing=True)
        job_scheduler.start()
        return

    def job_list(self):
        _job_list = job_scheduler.get_jobs()
        return _job_list

    def job_delete(self):
        job_scheduler.remove_all_jobs()
        logger.info("后台任务已停止")
        return

    def job_stop(self):
        return


job_manager = JobManager()
if __name__ == '__main__':
    job_manager.job_start()
    while True:
        time.sleep(10)