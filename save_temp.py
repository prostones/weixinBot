# coding=utf-8

import redis
from get_temp import getDataMust

r = redis.Redis(host='localhost', port=6379, db=0)
data = getDataMust()
r.lpush('temp', data.temp)

if __name__ == '__main__':
    print(U'最新获取的温度是 ' + r.lindex("temp", 0))
