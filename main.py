#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from qqbot import QQBot

# import jieba
import requests

myqqbot = QQBot()

@myqqbot.On('qqmessage')
def handler(bot, message):
    if message.content == '-stop':
        bot.SendTo(message.contact, 'QQ机器人已关闭')
        bot.Stop()
    else:
        # x = jieba.cut(message.content)
        # bot.SendTo(message.contact,"\ ".join(x))
        url = "http://www.tuling123.com/openapi/api"
        data = {
            "key": "xxxxxx",
            "info": message.content
        }
        r = requests.post(url,data)
        res = eval(r.content)
        bot.SendTo(message.contact, res['text'])
        print res['text']

myqqbot.Login()
myqqbot.Run()
