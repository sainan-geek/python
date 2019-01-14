#发送header请求
import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
resposnse =requests.get("https://www.baidu.com",headers = headers)
a = resposnse.content.decode()
print(a)