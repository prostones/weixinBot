# coding=utf-8
import time
from get_temp import getDataMust

class Info:
    def __init__(self, msg):
        self.msg = msg
        self.datatime = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.msgbody = "[" + self.datatime + "]" + u'你好！'

        if(len(msg and 'temp') or len(msg and u'温度')):
            self.join_temp_data()
        else:
            self.join_default()

    def join_temp_data(self):
        data = getDataMust()
        self.msgbody += u'当前温度：' + data.temp + u'摄氏度,' + u'湿度：' + data.wet

    def join_default(self):
        self.msgbody += u'可以尝试问我当前温度'

if __name__ == '__main__':
    nowdata = Info('')
    print(nowdata.msgbody)