# -*- coding: utf-8 -*-
from enum import Enum


class JobName(Enum):
    PROXY_UPDATE = 'Redis代理池更新'
    PROXY_JUDGE = '代理可用性研判'
