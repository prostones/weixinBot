# coding=utf-8

import redis

def getTemp():
    r = redis.Redis(host='localhost', port=6379, db=0)
    print('the first temp is 'r.lindex("temp",0) )
    return r.lindex("temp",0) 

if __name__ == '__main__':
    getTemp()


