import requests
url ='https://space.bilibili.com/363216828/favlist'
data = requests.get(url).txt
print('网站源码',data)
