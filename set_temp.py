# coding=utf-8

import redis

r = redis.Redis(host='localhost', port=6379, db=0)
for i in range(1, 10000):
    r.lpush('temp:23:34:' + str(i), 'zhangsan')  # 添加
