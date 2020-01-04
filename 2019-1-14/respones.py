import requests
response = requests.get("http://www.baidu.com")
r = response.status_code
print(r)
q = response.headers
print(q)
x = response.request.url
print(x)
