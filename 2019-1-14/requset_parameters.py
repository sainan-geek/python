# 发送带参数的请求
# https://www.baidu.com/s?wd=python
# https://www.baidu.com/s?wd=%E5%9B%BE%E7%89%87   百分号 url编码
import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# p = {"wd":"图片"}
# url_temp = "https://www.baidu.com/s?" 
# r = requests.get(url_temp,headers=headers,params=p)
# print(r.status_code)
# print(r.request.url)
url = "https://www.baidu.com/s?wd={}".format("图片")  # format 格式化字符串
r = requests.get(url,headers=headers)
print(r.status_code)
print(r.request.url)