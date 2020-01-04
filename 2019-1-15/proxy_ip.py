import requests

proxies = {"http":"http://119.101.112.250:9999"}

headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"}

r = requests.get("http://baidu.com",proxies = proxies,headers = headers)
print(r.status_code)