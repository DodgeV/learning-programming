# 0. 准备
* 专业的抓包工具我喜欢用wireshark，不过这篇没用多少抓包技巧
* 编辑器用的是pycharm2020.1.1
* python版本是win10子系统自带的3.6
* 一堆第三方库都是用pycharm装的，很方便

# 1. 抓包
* 百度图片官网https://image.baidu.com/ ，随机在首页搜索一个关键字
![图片1](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-19%20095644.png)

* 然后F12观察，点一下左上角的垃圾桶图标，

![图片2](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/Inked%E6%89%B9%E6%B3%A8%202020-08-19%20095739_LI.jpg)

* 然后F5刷新一下，经过观察，我们要找的触发源是XHR中的html类型文件

![图片--30](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-19%20101308.png)

* 轻轻往下一滑，发现，`pn`参数里面存在规律，步长为30递增

![图片--60](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-19%20101351.png)

![图片--90](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-19%20101422.png)

* 然后将该请求中所有的参数都copy下来，打成一个字典，作为params,** 注意这里的最后一个参数1597926642252，每天都在变**
* 由于每页30个图片，将30作为迭代步长，做成列表

![图片--代码列表](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-20%20215708.png)

# 2. 简单爬取以下

![图片--代码](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-20%20215837.png)

* 由于没加UA也没加代理，只爬到了一个200的状态值。。。。
* 再次观察这个请求的response，提取每一张图片的url，此处可考虑用bs4、re，笔者只是简单使用字符串的识别

![图片--响应预览](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-20%20203655.png)

![图片--代码](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-20%20213853.png)

# 3. 面向对象

先将爬取、下载图片两步分别封装为两个函数，然后使用面向对象的特性，将整个爬虫写成一个类
过程是先有getPages方法获取每一页的图片url，然后返回一个url列表给downloadJpg下载函数逐条下载
![图片--getPages](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-20%20214803.png)

![图片--download](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-20%20220349.png)

# 4. 转换颜色

利用numpy，将图片转换为灰度照片，具体代码如下，没啥好说的，不懂的翻一下官方帮助文档

![图片--convert](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-20%20215126.png)

以上代码已经将转换颜色也封装为一个函数，然后添加到类方法中，转换之后的图片存储在另一个文件夹中，完整类代码如下

```python
# -*- coding: utf-8 -*-
import requests
import os
import random
from PIL import Image
from bs4 import BeautifulSoup
import numpy

user_agent = ['Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
              'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
              'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
              'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
              'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,'
              'likeGecko)Chrome/17.0.963.56Safari/535.11',
              'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)',
              'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
              'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727'
              ';SE2.XMetaSr1.0)',
              'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
              'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,'
              'likeGecko)Version/5.1Safari/534.50']


class GetBaiduImg(object):
    kw = {'Host': 'image.baidu.com'}
    urls = list()

    def __init__(self, result, n):
        """
        :param result: 输入百度图片搜索的关键词
        :param n: 输入要爬取的页数
        """
        self.downloadJpg(datalist=self.getPages(result, n))
        self.convertColor('./baidu')

    def getPages(self, keyword, pages):
        try:
            GetBaiduImg.kw['user-agent'] = random.choice(user_agent)
            param = list()
            for i in range(30, pages * 30 + 30, 30):
                param.append({'tn': 'resultjson_com', 'ipn': 'rj',
                              'ct': '201326592', 'is': '', 'fp': 'result', 'queryWord': keyword, 'cl': '2',
                              'lm': '-1', 'ie': 'utf-8', 'oe': 'utf-8', 'adpicid': '', 'st': '-1',
                              'z': '', 'ic': '0', 'hd': '', 'latest': '', 'copyright': '',
                              'word': keyword, 's': '', 'se': '', 'tab': '', 'width': '', 'height': '',
                              'face': '0', 'istype': '2', 'qc': '', 'nc': '1', 'fr': '', 'expermode': '',
                              'force': '', 'pn': i, 'rn': '30', 'gsm': '1e', '1597926642252': ''})
            start_url = 'https://image.baidu.com/search/acjson'
            for i in param:
                res = requests.request(method='get', url=start_url, headers=GetBaiduImg.kw, params=i,
                                       proxies={"http": "175.43.58.44:9999"})
                res.raise_for_status()
                res.encoding = res.apparent_encoding
                response = res.content.decode('utf-8')
                for a in response.split('"'):
                    if "https://ss" and ".jpg" and "bdstatic" in a:
                        GetBaiduImg.urls.append(a)
            return set(GetBaiduImg.urls)
        except requests.RequestException as e:
            print('mistake info==>', str(e))

    def downloadJpg(self, datalist, direct='./baidu'):
        if not os.path.exists(direct):
            os.mkdir(direct)
        x = 1
        for data in datalist:
            if len(data):
                print(f'downloading img {data}')
                try:
                    resp = requests.request(method='get', url=data, proxies={"http": "175.43.58.44:9999"})
                    open(f'{direct}/{x}.jpg', 'wb').write(resp.content)
                    x += 1
                except Exception as exp:
                    print("misktake info==>",str(exp))

    def convertColor(self, direct):
        for i in os.listdir(direct):
            im = numpy.array(Image.open(direct + '/' + f'{i}').convert('L')).astype('float')
            print(f"converting img {i} with ", im.shape, im.dtype)
            depth = 10
            grad = numpy.gradient(im)
            grad_x, grad_y = grad
            grad_x = grad_x * depth / 100
            grad_y = grad_y * depth / 100
            A = numpy.sqrt(grad_x ** 2 + grad_y ** 2 + 1)
            uni_x = grad_x / A
            uni_y = grad_y / A
            uni_z = 1 / A
            vec_el = numpy.pi / 2.2
            vec_az = numpy.pi / 4
            dx = numpy.cos(vec_el) * numpy.cos(vec_az)
            dy = numpy.cos(vec_el) * numpy.sin(vec_az)
            dz = numpy.sin(vec_el)
            b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
            a = b.clip(0, 255)
            im = Image.fromarray(a.astype('uint8'))
            im.save(direct + '/' + f'[灰度照]{i}')


if __name__ == "__main__":
    baiduimg = GetBaiduImg(result="郁金香", n=1)
```

最后贴上运行结果

![图片--结果](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-20%20220810.png)

![图片--爬取结果](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-20%20220940.png)

![图片--灰度照](https://github.com/DodgeV/learning-programming/blob/master/for_ex/my_spider_baiduimg/%E6%89%B9%E6%B3%A8%202020-08-20%20221012.png)