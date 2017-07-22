# coding=utf-8

import itchat
import time
from itchat.content import *
from get_temp import getDataMust
from core import Info


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    data = Info(msg)
    msg.user.send(data.msgbody)
    #msg.user.send('%s: %s' % (msg.type, msg.text))

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
        data = Info(msg)
        msg.user.send(u'@%s\u2005Hi: %s' %
                          (msg.actualNickName, data.msgbody))


# itchat.auto_login(True)
itchat.auto_login(enableCmdQR=True)
itchat.run(True)
