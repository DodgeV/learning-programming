import requests,os,re,json
from bs4 import BeautifulSoup
import codecs
encode = codecs.utf_8_encode
#from retrying import retry

user_agent=['Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50']
proxies=[{"http": "http://10.10.1.10:3128","https":"http://10.10.1.10:1080"},{"http": "http://10.10.1.11:3128"}]

#requests    
def getHTMLtext(url):
	try:
		kw={'User-Agent':user_agent[0],'Host':'mail.126.com'}
		#如果只有user不够，再加其他的referer或者Cookies
		Cookie = "mail_health_check_time=1573466790663; nts_mail_user=xzc126126@126.com:-1:1; MAIL_PINFO=xzc126126@126.com|1573975046|0|mail126|00&99|jis&1573736741&mail126#jis&320100#10#0#0|&0|mail126&imooc|xzc126126@126.com; locale=; face=js6; starttime=; df=mail163_letter; mail_upx=t4bj.mail.126.com|t1bj.mail.126.com|t2bj.mail.126.com|t3bj.mail.126.com; mail_upx_nf=; mail_idc=; Coremail=fb3d6fd51a995%gAkoTvRcfURueSXjteccemDgmNsMKYQS%g3a29.mail.126.com; MAIL_MISC=xzc126126@126.com; cm_last_info=dT14emMxMjYxMjYlNDAxMjYuY29tJmQ9aHR0cHMlM0ElMkYlMkZtYWlsLjEyNi5jb20lMkZqczYlMkZtYWluLmpzcCUzRnNpZCUzRGdBa29UdlJjZlVSdWVTWGp0ZWNjZW1EZ21Oc01LWVFTJnM9Z0Frb1R2UmNmVVJ1ZVNYanRlY2NlbURnbU5zTUtZUVMmaD1odHRwcyUzQSUyRiUyRm1haWwuMTI2LmNvbSUyRmpzNiUyRm1haW4uanNwJTNGc2lkJTNEZ0Frb1R2UmNmVVJ1ZVNYanRlY2NlbURnbU5zTUtZUVMmdz1odHRwcyUzQSUyRiUyRm1haWwuMTI2LmNvbSZsPS0xJnQ9LTEmYXM9dHJ1ZQ==; MAIL_SINFO=1573975046|0|#3&80#|xzc126126@126.com; secu_info=1; mail_entry_sess=a120d8096fe99db267e545b4ce7f1d3b1e1829b5d3ecd3f5e592169c5dcf5e082fdbf9c7c7047500963bcb2e47f7f7431ca614bcc45185412b9e20e73432a05d25339ed42e7d3b886da2beec0ff1243f6a6bf66b9fb230a5b1e517dad7ee07aa3a2f648d58588bc7eda015b2e7b92e63e45b7a1db2153d7f23ec2674dcda0f0a2612da104f16bca53503bd90f8eea2bdeb85f7eb83e6c67232733f01790965067c9dee94f6e3ac10fbf72b2b76752857bb78af6ace87dfb77fa1f82edb09482b; JSESSIONID=274A7C1074A164DD65BE45DA42758312; mail_style=js6; mail_uid=xzc126126@126.com; mail_host=mail.126.com; Coremail.sid=rAwKzWzHfFtJruvfhiHHrsdkiVsmcgFz; BAIDU_SSP_lcr=https://reg.163.com/Logout.jsp?username=xzc126126@126.com&url=https://mail.126.com/logout.htm?showAd=1%23126|xzc126126|1573975012518|false; NTES_SESS=3FXqwnjPZ.DR0JqzzdXQzQO7wqzWPtEWJGebAwK_Hc3zl.DwlvG8Q0Dm.dZxbT0V20e4oZKGMybMlwz4MxzygbBb6HePT3w9ZLupTcir_daWPDQ1fhH4Cfz8IuH6F4B6N2Yq3YVx8A7dKPjmCGLccwATpliu7xHxMeSxq4SDs0dNAVuxvHTSAnK3uFgjdbv5L4ACWNlanc9pdXCh90N9J_wE_; S_INFO=1573975046|0|#3&80#|xzc126126@126.com; P_INFO=xzc126126@126.com|1573975046|0|mail126|00&99|jis&1573736741&mail126#jis&320100#10#0#0|&0|mail126&imooc|xzc126126@126.com; MAIL_SESS=3FXqwnjPZ.DR0JqzzdXQzQO7wqzWPtEWJGebAwK_Hc3zl.DwlvG8Q0Dm.dZxbT0V20e4oZKGMybMlwz4MxzygbBb6HePT3w9ZLupTcir_daWPDQ1fhH4Cfz8IuH6F4B6N2Yq3YVx8A7dKPjmCGLccwATpliu7xHxMeSxq4SDs0dNAVuxvHTSAnK3uFgjdbv5L4ACWNlanc9pdXCh90N9J_wE_"
		cookie_dict = {i.split('=')[0]:i.split('=')[-1] for i in Cookie.split('; ')}
		#url = 'https://www.baidu.com/s'
		#params = {"code":"S_OK","var":{"citycode":58238}} 
		#response = requests.post(url,data = params,headers = kw)
        #'''从响应里面找到一样的翻译,再从参数里面找表单字典'''
		#dict1 = {'wd'='jpython'}
		#@retry(stop_max_attempt_number=3)'''尝试三次未成功后才会报错'''
		response = requests.request('GET',url,headers = kw,cookies = cookie_dict,verify = False,proxies=proxies[1])
		#发送请求时 verify 参数设置为 False 表示不验证CA证书
        #proxies = {"http":"http://IP地址:端口号","https":"https://IP地址:端口号"}定义代理服务器
		#auth 传入元组，支持HTTP认证功能
		#files 向服务器传入文件
		#json = {} 向服务器提交内容
		#data = {} 向服务器提交文件
		#timeout = 30 控制时间
		#params = {'wd':'jpython'} 利用params加上问号后面的参数 将url补充成https://www.baidu.com/s?wd=jpython
		#allow_redirects  默认为True，表示允许对url进行重定向
		#stream  默认为True,表示对获取内容进行立即下载
		#cert  保存本地SSL证书路径
		response.raise_for_status()
        #print(response.status_code) isn't 200,return error
		#print(type(response));print(response.headers);print(response.request.headers);print(response.reason)
        #response.url与requests.url不一样
		response.encoding = response.apparent_encoding
		#print(response.content.decode('gbk'))
		#print(response.json())
		#print(response.status_code)
		print('网站源码:',response.text)
	except exceptions.Timeout as e:
		print(e.message)

url = "https://mail.126.com/js6/main.jsp?sid=gAkoTvRcfURueSXjteccemDgmNsMKYQS&df=mail163_letter"
getHTMLtext(url)

"""
#在爬取百度搜索中的链接时，发现获取的链接都是经过百度加密过的
#第1部分是所有的百度搜索链接的头，第2部分是搜索结果的url加密部分，第3部分是搜索者id相关的数据，可以删除
#将g[0]中的id部分删除得real_url
real_url = "http://www.baidu.com/baidu.php?url=Ks00000EAMrnlPLIy8LX5nV5UHK-AG29y9ymFOTcHjY5DGIXk3GTcZJaISuJvykSv0Xs81FEgY02u3JnuNjf6XgeqQirKrHSd2fyMF8bPfNjBKS_xmBT3uucJGfKPpw1ZhPsyXInbx5aH1vU3XmHUMgpQPl2mxWbFP7QRwwhqrOUiv2JeoP6Rycr-x-LxpfsQqMti_iELwm8rfUszBgJwiuNVGkr.7D_imcM8BtohTd1ruDjPd7tgUzYFhmCqpuExEohIG3DL_IhHFMeXj5gMsSX1jeptr13T5Mvmxgu9LSLj4e_5VttrOv3x5Gse5U9Le_rH4mx5_sS81jlS8Z1vmxg_sSLGsSxH9vUn5o33ILdOPtrZFt_5M_sSvEj_SZj4qhZdvmIOVseEosTZK9zXx6s45-Wsg3TMMaeHdEu9eTDd76gn4ohTzn5Zgz32AM-WHG4TH7IIhektxZTGyAp7WFblIvwf.U1Yk0ZDqsEQ2lfKspynqnfKY5Tvtz8b0pyYqnW0Y0ATqUvwlnfKdpHdBmy-bIfKspyfqnHb0mv-b5H00UgfqnH0kPdtknjD4g1DsPjuxn1msnfKopHYs0ZFY5HT3P6K-pyfqnHf1P-tznHDsrNtzrHRvr7tzrHTsn7tzrHcznfKBpHYsg1Ddr7tznjf0UynqnH61n1cLPjf4n7tknj0kg1Dsn-ts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qPj04P1D3P1TLPsK8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqPsK8IjYs0ZPl5fK9TdqGuAnqTZnVuyPJ0A-bm1dribGH0Z"
response1 = requests.get(real_url) #再经过一次response拟爬取,返回的url才是真正的当当网url
h = []
def request_dangdang():
	try:
		headers1={'User-Agent':user_agent[0],'Host':'databack.dangdang.com',
				 'Host':'www.dangdang.com','Accept':'text/css,*/*;q=0.1','Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
				 'Accept-Encoding':'gzip, deflate','Referer':'http://www.dangdang.com/','Connection':'keep-alive',
                 'cookie':'__permanent_id=20191119191332318896837878453532479;from=422-kw-1-%D0%D0%D2%B5%B6%A8%CD%B6-%D6%F7%D5%CB%BB%A7_PC-%B9%D9%CD%F8_m.dangdang.com; order_follow_source=P-422-kw-1%7C%231%7C%23www.baidu.com%252Fbaidu.php%253Fsc.Kf0000K5cNxA6dzipUCHYZMaGd2o7UolvAh0iKOdsipsRmhQNZJ-qcrgW3IB0HBOiP1PxpLs4%7C%230-%7C-; __ddc_24h=1574403966%7C!%7C_utm_sem_id%3D11057663; __ddc_15d=1574403966%7C!%7C_utm_sem_id%3D11057663; __ddc_15d_f=1574336260%7C!%7C_utm_sem_id%3D11057663; __rpm=%7Cmix_317715.3208532..1574408572285; ddscreen=2; dest_area=country_id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_id%3D0%26town_id%3D0; __ddc_1d=1574403966%7C!%7C_utm_sem_id%3D11057663; __visit_id=20191122152035564627145627864449317; __out_refer=;__trace_id=20191122154255247217934144828279368'}
		params={'expose_url':'http://a.dangdang.com/api/data/cpx/img/39470001/1'}
        response1=requests.get(response1.url,headers = headers1,params = params) #返回的Response1对象的url属性就是真实的url(当当网)
        response1.raise_for_status()#在网页上找到编码为GB2312
        soup1=BeautifulSoup(response1.content.decode('GB2312'),'html.parser')
        for i in soup1.find_all('a'):#分析网页源码,找出特征代码,定位目标url
            if i.get_text() == '运动户外': #因为当当首页的url是经过加工的，没有'图书'对应的url，所以选择首页另外一个子页面，之后再转回'图书'页面
                h.append(i['href'])
        headers2 = {'Host':'e.dangdang.com','User-Agent':user_agent[1],
		  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		  'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		  'Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive'}
        response2=requests.get(h[1],headers=headers2,params={'siteid':'dd_1000','v':'nt6.93','t':'2019.03.11_160449'})
        response2.raise_for_status()
        response2.encoding = response2.apparent_encoding
        soup2=BeautifulSoup(response2.content.decode('gb2312'),'html.parser')
        for i in soup2.find_all('a',target="_blank"):
            if i.get_text() == '图书':  #转回'图书'页面
                headers3={'Host':'book.dangdang.com','User-Agent':user_agent[2],
        	    'Accept':'text/css,*/*;q=0.1','Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        	    'Accept-Encoding':'gzip, deflate','Connection':'keep-alive'}
                response3=requests.get(i['href'],headers=headers3)
                response3.raise_for_status()
                soup3=BeautifulSoup(response3.content.decode('gbk'),'html.parser')
                for i in soup3.find_all('ul',dd_name="商品",class_="product_ul"): #经过分析，选择特征，爬取'新书上架'的所有图书及对应url
                        for d in i.find_all('a',class_="img"):
                                with open('book.txt','a',encoding = 'utf-8') as f:
                                        f.write(d['title']+d['href']+'\n')
	except requests.RequestException:
		return None
request_dangdang()
#urllib
def get_code(wd):
	import urllib.request 
	import urllib.parse 
	import http.cookiejar#import urllib.error,urllib.robotparser
	cj = http.cookiejar.CookieJar()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))#some url must cookie (proxyHandler HTTPSHandler HTTPRedirectHandler) 
	#urllib.request.install_opener(opener)
	url = "https://www.baidu.com/s?wd="#定义请求地址
	headers = {'User-Agent':'Mozilla/5.0 3578.98 Safari/537.36',}#定义自定义请求头
	request = urllib.request.Request(url=url + urllib.parse.quote(wd),headers=headers)#定义请求对象
	response = urllib.request.urlopen(request,timeout = 15)#take a time发送请求
	#url = ur.Request('http://ac.scmor.com/')
	#url.add_data('a','1')
	#url.add_header('User-Agent','Mozilla/5.0')
	html = response.read() # 300 words
	print(html.decode('utf-8'))#print(response.getcode())print(response.info())
	#print(cj)
	response.close()
if __name__ == '__main__':
	wd = input("请输入查询内容：")
	#u = 'http://data.europa.eu/euodp/en/data/'
	get_code(wd)

#bs4
soup = BeautifulSoup(response.text,'html.parser') #lxml,xml,html5lib
print(soup.prettify()) #结果更加美观，树形结构更为直观
#soup.find_all() 可以简写成 soup()
for i in soup.find_all('a'):  #也可用在标签上
    print(i.prettify())
for i in soup.find_all(True,recursive = False,string = '网易云课堂'):  
    print(i.name) #取所有的标签的名,再取所有子节点,其中满足字符要求的部分
#for i in soup.find_all('a',target="_blank")
#for i in soup.find_all('a','_blank')
#for i in soup.find_all('a',target=re.compile('link')) #正则表达式可以检索包含link的字符串
#find() find_parents() find_parent() find_next_siblings
#find_next_sibling() find_previous_siblings() find_previous_sibling()
print(soup.title,soup.name)
tag = soup.a #只能获得第一个a标签
print(tag,tag.name,tag.parent.name,tag.parent.parent.name) #父类标签
print(tag.attrs) #所有属性,返回字典类对象
print(tag.attrs['href'])
tag2 = soup.p
print(tag2.string) #返回字符内容,若为注释则返回一个注释类型
print(tag2.comment) #注释内容

#下行遍历
len(soup.body.contents)
'''
for i in soup.body.children:
    print(i)
    
for i in soup.body.descendants:
    print(i)
'''
#上行遍历
for i in soup.title.parents:  #遍历所有的父标签
    if i is None:   #遍历到soup本身时会返回None
        print(i)
    else:
        print(i.name)

#平行遍历必须发生在同一个父节点下
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling)
for i in soup.head.next_siblings:  #遍历所有后续节点
    print(i)
for i in soup.a.previous_siblings:  #遍历所有前续节点
    print(i)
#json    信息有类型，适合程序处理，较xml简洁，无注释，一般用在程序对接口的部分
#xml  最早的通用信息标记语言，可扩展性好但繁琐，用于Internet上的信息交互与传递
#YAML  信息无类型，文本信息比例最高，可读性好，用于各类系统的配置文件，有注释易读
