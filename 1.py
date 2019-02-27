
import itchat
import time
import datetime

def send_news(message):
    my_friend = itchat.search_friends(name=u'xxx')
    name = my_friend[0]["UserName"]
    #itchat.send(message, toUserName=name)
    itchat.send(message, toUserName='filehelper')

itchat.auto_login(hotReload=True)

while 1 :
    now = datetime.datetime.now()
    str = now.strftime('%Y%m%d %H%M%S')[9:]
    print('\r{}'.format(str),end="")
    
    message = "xxx"

    if str == "140000":
        send_news(message) 
    
    #if int(str) % 10000 == 0:
    #    send_news(str)
    time.sleep(1)
