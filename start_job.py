# -*- coding: utf-8 -*-
import time

from grabworld.job import job_manager

if __name__ == '__main__':
    job_manager.job_start()
    while True:
        time.sleep(10)
