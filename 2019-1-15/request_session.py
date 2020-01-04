import requests

session = requests.session()

post_url = "http://www.renren.com/PLogin.do"
post_data = {"email":"","passwd":""}
headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"}

#使用session发送post请求，cookie保存在其中
session.post(post_url,data=post_data,headers =headers)
#在使用session进行请求登陆之后才能访问的地址
r = session.get("http://www.renren.com/327550029/profile",headers=headers)
#保存页面
with open("renren1.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())