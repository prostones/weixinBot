# coding=utf-8

import redis

r = redis.Redis(host='localhost', port=6379, db=0)

for i in range(1, 10000):
    r.lpush('temp', str(i), 'zhangsan')  # 添加

if __name__ == '__main__':
    return ''
