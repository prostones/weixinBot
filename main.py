# coding=utf-8

import itchat
import time
from itchat.content import *
from get_temp import getDataMust


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    data = getDataMust()
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    if(len(msg and 'temp') or len(msg and u'温度')):
        msg.user.send("[" + nowtime + "]"
                      + u'当前温度是' + data.temp + u'摄氏度,'
                      + u'适度是' + data.wet)
    else:
        msg.user.send('%s: %s' % (msg.type, msg.text))


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        mymsg = ''
        data = getDataMust()
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S',
                                time.localtime(time.time()))
        if(len(msg and 'temp') or len(msg and u'温度')):
            mymsg = "[" + nowtime + "]" + u'当前温度是' + \
                data.temp + u'摄氏度,' + u'适度是' + data.wet
            msg.user.send(u'@%s\u2005Hi: %s' %
                          (msg.actualNickName, mymsg))


# itchat.auto_login(True)
itchat.auto_login(enableCmdQR=True)

itchat.run(True)
