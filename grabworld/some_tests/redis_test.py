# -*- coding: utf-8 -*-
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
res = r.sadd('test', *('123', '456'))
print(res)
print(r.smembers('test'))
r.srem('test', '123')
print('删除完了')
print(r.smembers('test'))
