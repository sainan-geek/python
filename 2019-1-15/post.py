import requests

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
data = {
    "from":"en",
    "to":"zh",
    "query":"hol",
    "transtype":"translang",
    "simple_means_flag":"3",
    "sign":"372549.85108",
    "token":"f2954bbdb57c41321bb952deb77bc095"
}
post_url = "https://fanyi.baidu.com/v2transapi"
r = requests.post(post_url,data = data,headers=headers)
print(r.content.decode())