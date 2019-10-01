import codecs
encode = codecs.utf_8_encode
import requests
url ='http://www.nipic.com/index.html'
data = requests.get(url).text
print('网站源码',data)
