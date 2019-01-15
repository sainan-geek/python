import requests
import json
import sys
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
post_url="http://music.zhuolin.wang/api.php?callback=jQuery111309083136632077478_1547551953222"

query_string = sys.argv[1]

post_data = {
    "types": "search",
    "count":"20",
    "source": "netease",
    "pages":"1",
    "name":query_string
}
r = requests.post(post_url,data=post_data,headers=headers)
# print(r.content.decode())
dict_ret = json.loads(r.content.decode())
# ret = dict_ret
print("result is :"+ dict_ret)