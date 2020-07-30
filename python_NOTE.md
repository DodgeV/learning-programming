# 基础知识
* 编译器 编译型语言 统一翻译 一起执行 速度更快 
* 解释器 解释型语言 读取一行 翻译一行 执行一行 跨平台更有优势
> + 其他解释器:CPython Ipython Jpython PyPy
* IDE 集成开发环境 图形用户界面 代码编辑器(Editor) 编译器/解释器 调试器 控制台(console)
* 文件开头一般会指定解释器的路径，以及文件的编码
```python
# !/usr/bin/python
# -*- coding: UTF-8 -*-
```
* python程序执行原理:操作系统先让CPU把python解释器加载到内存 python解释器根据语法规则从上到下让CPU翻译python程序中的代码 CPU再来执行翻译后的代码
* QQ软件在运行之前是保存在硬盘中的 运行之后就会加载到内存中 并获得专属的内存空间 登录时将号码和密码保存之后 发给腾讯服务器 并分配一些内存空间来保存号码和密码 使用别名(变量名)来标记号码和密码
* 使用import导入模块python解释器将模块源码转换为字节码的pyc二进制文件 以提高速度 
```python
import py_compile    
py_compile.compile('hello.py') # 将hello.py编译为hello.pyc的文件
```
* 将py程序变为可执行程序，需要第三方库`PyInstaller`
* `PyInstaller -F XXX.py`
* `PyInstaller -i snowflake.ico -F XXX.py`

## crawler
* 通用爬虫是搜索引擎用的爬虫:百度快照也是一种爬虫可以爬存和文本相关的内容 不能爬取图片电影二进制文件等
* 通过url访问 将域名通过DNS解析 返回给浏览器一个IP地址 再将IP地址发给服务器访问对应网站 也可以直接访问ip 就是没有经过DNS技术的转化 直接访问目标服务器
* 新的网站诞生第一天 各大搜索引擎如何获取新网址的url：
* 1.主动提交给百度 2.在其他网址设置网站的外链
* 3.搜索引擎会和DNS服务商合作 快速收录新网址的url
* Robots.txt 只是一个协议 一般只有大型的搜索引擎爬虫才会有很多限制
* 协议://ip或域名[:端口]/路径/.../[?参数][#锚 用于跳转到网页指定锚点]
* https协议是由SSL和HTTP共同构建的可进行加密传输、身份认证的网络协议 需要ca申请证书,一般需要收费 并由具有安全性的ssl加密传输
* 二者端口不一样 http-80 https-443
* http的连接很简单是无状态的 是基于tcp的一种规范、协议  规定客户端和服务器的互联
* 发起请求的时候 请求(request)分为header和body     
* header中至少含有GET /(要访问的文件名) HTTP/1.1    其中Host是本机IP 
* 若没有特别的写要访问的文件 就是访问的网站的主页
* 服务器返回给浏览器的内容(response)包括2个部分:headers和body 2者用空行分开
* <u>headers</u>中含有set-cookie 即服务器给浏览器的设置，可能包含用户的浏览痕迹 还有反馈连接协议和状态的 HTTP/1.1 200 OK 以及规定解码的charset=utf-8/....
* <u>body</u>中含有前端的所有html/css/js等 是浏览器要展示的东西
* http 1.0 短链接 每一次请求都重新3次握手创建新的套接字
* http 1.1 长链接 先得到整个页面的数据 后一次性请求所有需要的数据
* 本机 [IP查询](http://www.ip138.com/)
* ip地址:用来标记网络上的一台电脑 
+ windows:ipconfig linux/mac/unix:ifconfig 出现2个网卡 想与别人通信用以太网 自己联网用本地 sudo ifconfig ens40 down 把通信网关掉
* 分类:ipv4/ipv6 v指版本  ipv6 正在发展
* ipv4 更常用 4组数 总共有256 * 256 * 256 * 256 种
> * C类地址前3个标记网络号 同一个局域网前3个3位数一样 最后一个标记主机号 0和255用于广播 不能随便用
> * A类IP地址第1组当作网络号 后3组当作主机号 B类前2后2 C类前3后1
> * D类主要用于多点广播 E类地址保留仅用于实验
* 端口号(port)类似软件的IP 可以理解为门牌号 一个程序没有运行叫程序 运行起来叫进程
> * 知名端口(小于1024)是众所周知的 大家默认都使用的端口 不能随便用 比如80端口分配给HTTP 21端口分给FTP
> * 动态端口(1024到65535) 可以随意使用
## 网络通信基础：使用网络的目的是联机
### socket是一种进程的通信方式
### 网络-udp 写信模型 每一封信都需要署名收信人和寄信人 但是并不安全 数据可能丢 udp是面向无连接的通信

```python
import socket # socket.socket(AddressFamilly(协议族ipv4),Type(udp/tcp))
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # tcp套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # udp套接字
# 给套接字设置固定端口
local_addr = (' ',7788) # ip一般不写,表示本机任何一个ip
udp_socket.bind(local_addr) # 必须绑定自己电脑的IP 但不可以占用其他进程的端口 不绑定操作系统就会给一个随机端口
dest_ip = '192.168.0.147'
dest_sort = 7788
recv_data = udp_socket.recvfrom(1024) # 接收数据,默认接受元组,具有阻塞的特性,操作系统收到数据会先存起来,等待程序的调用来取数据
print(recv_data)
data = 'hello'
udp_socket.sendto(data.encode('utf-8'),(dest_ip,dest_sort)) #后接ip和port的元组
#若是发不通则试一下ping 192.168.0.147
#若是电脑有几个IP则把虚拟网卡VMware关掉
udp_socket.close()
```

+ 单工:收音机 只能收
+ 半双工:对讲机 可以收发，但同一时刻只能收或发
+ 全双工:电话 同一时刻可以同时收发 socket套接字是全双工
# 用udp实现半双工聊天器
```python
import socket
print('XXX聊天器'.center(50,'='))
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_socket.bind(('192.168.0.147',7788))

def send_msg(udp_socket):
    data = input('send some data:')
    udp_socket.sendto(data.encode('utf-8'),('192.168.0.147',7799))    

def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    print(\%s:%s\ % (str(recv_data[1]),recv_data[0].decode('utf-8')))

while True:
    print('1-send message')
    print('2-recieve message')
    choice = input('choose your function:')
    if choice == '1':
        send_msg(udp_socket)
    elif choice == '2':
        recv_msg(udp_socket)
    else:
        break
    udp_socket.close()
```
# udp聊天器 优化版
```python
import socket,threading
def send_msg(udp_socket):
    while True:
        data = input('send some data:')
        udp_socket.sendto(data.encode('utf-8'),('192.168.0.147',7799))    

def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(\%s:%s\ % (str(recv_data[1]),recv_data[0].decode('utf-8')))

print('XXX聊天器'.center(50,'='))
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_socket.bind(('192.168.0.147',7788))

t1 = threading.Thread(target=send_msg,args=(udp_socket,))
t2 = threading.Thread(target=recv_msg,args=(udp_socket,))

t1.start()
t2.start()

#udp_socket.close() 将最后一行注释掉否则会报错
```

### 网络-tcp 传输控制协议 较为安全 更稳定 类似打电话 tcp是面向链接的通信
> * 发送应答机制:在传输前必须建立链接(拨号) 发出数据后可以知道对方收到没有
> * 超时重传
> * 错误校验 检验是否有误
> * 流量控制和阻塞管理 
> * 严格区分客户端和服务器 服务器离主机越远越卡
> * 客户端 eg:APP     
> * 3次握手 (双方都在准备资源)客户端先发syn 服务器准备好资源后返回ack和新的syn 客户端准备好后返回ack
> * 4次挥手 (双方都在释放资源)(全双工套接字有两个通道 收和发都要关)  客户端向服务器发close关闭发送通道\\ 服务器关闭接收通道并告诉客户端已收到 \\ 服务器再关闭发送通道并向客户端发close\\ 客户端关闭接收通道并告诉服务器已收到 
> * 因为第2次挥手是为了确认服务器收到并对new_socket.recv解堵塞  第3次是为了服务器关闭发送通道new_socket.close  在程序中二者之间可以time.sleep()延迟 所以这2次不能简化为1次
> * 谁先调close谁就会保留资源 一直等到超时重传时间过去了  即数据包在网络上能存活的时间的两倍  如果没有重发过来 就释放资源
> * 服务器不能先close 因为保留的资源 会影响下一次connect 即端口被占
> * 如果服务器想要重新利用套接字 则需要加一行代码:            
`tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)`
> * 客户端可以先close 原因是客户端一般不绑定端口 每一次重连都会用新的端口号

### tcp客户端 一般不绑定端口 先发
### 两台QQ客户端可以都不绑定 通过第三方服务器来交换信息
```python
# 模拟下载
from socket import *
tcp_client_socket = socket(AF_INET,SOCK_STREAM)
server_ip = input('请输入要链接的服务器IP')
server_port = input('请输入要链接的服务器port')
# 链接服务器
tcp_client_socket.connect((server_ip,server_port))
send_data = input('输入要下载的文件:')
tcp_client_socket.send(send_data.encode('gbk'))
recvdata = tcp_client_socket.recv(1024) #1024个字节为1K 1024*1024为1M
if recvdata:
	with open('[新]'+send_data,'wb') as f:
	    f.write(recv_data)
	print('接收到的数据为',recvdata.decode('utf-8'))
	tcp.client.socket.close()
```

### tcp服务器 先收
```python
from socket import *
tcp_server_socket = socket(AF_INET,SOCK_STREAM)
address = ('',7788)
tcp_server_socket.bind(address) # 服务器需要绑定ip和端口,方便客户端链接
# listen使套接字变为可以被动链接,从而可以接收别人的链接
tcp_server_socket.listen(128) # 128与同一时刻链接的客户端有关 与操作系统有关
while True: # 循环接受客户端,为客户端服务
print('等待新客户端连接.....')
# accept等待客户端的链接connect,默认如果没有客户端链接则会一直等待,产生新的套接字client_socket为这个客户端服务
# clientaddr 是这个客户端的信息IP和port
# tcp_server_socket就可以省下来专门等待其他新客户端的链接
client_socket,clientaddr = tcp_server_socket.accept()
while True: # 为同一个客户端服务多次
    print('{0}客户端连接成功'.format(clientaddr))
    # 接收和发送数据
    recvdata = client_socket.recv(1024)
    print('客户端送过来的的数据为',recvdata.decode('utf-8'))
    # 如果recv解堵塞可能是
    # 1.客户端发送来数据
    # 2.客户端close
    if not recvdata:
	client_socket.send('continue'.encode('utf-8'))
    else:
	client_socket.send('goodbye'.encode('utf-8'))
	break

    client_socket.close() #关闭套接字不再为这个客户端服务
    print('已经为这个客户端服务完毕')

tcp_server_socket.close() # 最后关服务器
```

```python
from socket import *
def send_file_2_client(new_client_socket,client_addr):
    recvdata = new_client_socket.recv(1024).decode('utf-8')
    print('客户端要下载的数据为',recvdata)
    file_content = None
    try:
        f = open(recvdata,'rb')
        file_content = f.read()
        f.close()
    except Exception as e:
        print('没有要下载的文件{}'.format(revcdata))
    if file_content:
        client_socket.send(file_content)

def main():
    tcp_server_socket = socket(AF_INET,SOCK_STREAM)
    tcp_server_socket.bind((\\,7890)) 
    tcp_server_socket.listen(128)
    print('等待新客户端连接.....')
    while True:
        client_socket,clientaddr = tcp_server_socket.accept()        
        print('{0}客户端连接成功'.format(str(clientaddr)))
        send_file_2_client(client_socket,clientaddr)

        client_socket.close() #关闭套接字不再为这个客户端服务
        print('已经为这个客户端服务完毕')
    tcp_server_socket.close() 
main()
```
# tcp模型模拟实现http服务器 返回固定页面
```python
from socket import *
tcp_server_socket = socket(AF_INET,SOCK_STREAM)
tcp_server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) # 设定套接字选项 保证服务器可以先close
address = ('',7788)
tcp_server_socket.bind(address) 
tcp_server_socket.listen(128) 
while True: 
    print('等待新客户端连接.....')
    client_socket,clientaddr = tcp_server_socket.accept()
    while True: 
        print('IP端口号为{0}的客户端连接成功'.format(clientaddr))
        ''' 接收请求头'''
        request = client_socket.recv(1024) # 客户端不只是发送请求的页面 还有超链接
        print('客户端送过来的的请求为\\n',request.decode('utf-8'))
        ''' 返回headers和body'''
        headers = \HTTP/1.1 200 OK\\r\\n\ # 每一行后面都有一个换行
        konghang = \\\r\\n\   # 2者中空一行
        f = open('baidu.html','r')
        body = f.read()
        f.close()
        # body = \<h1>this is a headline</h1>\
        response = headers + body
        client_socket.send(response.encode('utf-8'))
        client_socket.close() #关闭套接字不再为这个客户端服务
        print('已经为这个客户端服务完毕')
        break
    tcp_server_socket.close() # 最后关服务器的监听套接字
```
# 应用多进程多线程协程改进tcp模拟http服务器
```python
from socket import *
import re,multiprocessing,threading
#import gevent
#from gevent import monkey
#monkey.patch_all()
def service_client(client_socket):
    ''' 接收请求头'''
    request = client_socket.recv(1024).decode('utf-8')
    print(request)
    request_lines = request.splitlines()
    ret = re.search(r\/[^/1|\\D]*[^\\s]*\,request_lines[0]) if len(request_lines) else None
    file_name = ret.group(0) if ret else \baidu.html\
    print(\请求访问\,file_name)
    try:
        f = open(file_name[1:],'rb')
    except:
        headers = \HTTP/1.1 404 NOT FOUND\\r\\n\
        headers = headers + \\\r\\n\
        client_socket.send(headers.encode('utf-8'))
    else:
        body = f.read()
        f.close()
        ''' 打开成功就返回状态码200'''
        headers = \HTTP/1.1 200 OK\\r\\n\ 
        konghang = \\\r\\n\   
        headers = headers + konghang
        client_socket.send(headers.encode('utf-8'))
        client_socket.send(body)
    client_socket.close()
    
def main():
    tcp_server_socket = socket(AF_INET,SOCK_STREAM)
    tcp_server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) 
    tcp_server_socket.bind((\192.168.0.147\,7788)) 
    tcp_server_socket.listen(128) 
    while True: 
        print('等待新客户端连接.....')
        client_socket,clientaddr = tcp_server_socket.accept()
        print('IP端口号为{0}的客户端连接成功'.format(clientaddr))
        #gevent.spawn(service_client,client_socket) # 协程
        #t = threading.Thread(target=service_client,args = (client_socket,)) # 多线程
        #t.start()  # 注意多线程不会复制资源 所以不用client_socket.close()
        p = multiprocessing.Process(target=service_client,args=(client_socket,)) # 多进程
        p.start()
        client_socket.close() # 多进程会复制之前定义的所有变量 这里需要先关一次主进程的 之后再关的子进程才会指向fd文件描述符 然后才会开始4次挥手
    tcp_server_socket.close() # 最后关服务器的监听套接字

if __name__ == '__main__':
    main()
```
# 单进程 单线程 利用列表遍历 实现同时服务多个客户端
```python
from socket import *
import time
tcp_server_tcp = socket(AF_INET,SOCK_STREAM)
tcp_server_tcp.bind(\\,7890)
tcp_server_tcp.listen(128)
tcp_server_tcp.setblocking(False) # 设置套接字为非堵塞
client_socket_list = list()
while True:
    time.sleep(1)
    try:
        new_socket, new_addr = tcp_server_tcp.accept()
    except Exception as ret:
        print('----没有新的客户端到来----')
    else:
        print('----只要没有产生异常，就意味着有新客户端连接成功')
        new_socket.setblocking(False) # 设置套接字为非堵塞方式
        client_socket_list.append(new_socket)
    for client_socket in client_socket_list:
        try:
	        recv_data = client_socket.recv(1024) 
        # 每一次recv并不是直接从对方客户端拿数据 而是从操作系统的缓存区域拿数据
        except Exception as ret:
      		print('----这个客户端没有发送数据')
        else:
		if recv_data:
		    print('----这个客户端发送来数据')
		    print(str(recv_data))
		else:
		    print('客户端调用close')
		    client_socket_list.remove(client_socket)
	client_socket.close()
```
# 利用单进程 单线程 遍历实现 长链接
```python
from socket import *
import re
def service_client(client_socket, request):
    ''' 接收请求头'''
    #request = client_socket.recv(1024).decode('utf-8')
    #print(request)
    request_lines = request.splitlines()
    ret = re.search(r\/[^/1|\\D]*[^\\s]*\,request_lines[0]) if len(request_lines) else None
    file_name = ret.group(0) if ret else \baidu.html\
    print(\请求访问\,file_name)
    try:
        f = open(file_name[1:],'rb')
    except:
        headers = \HTTP/1.1 404 NOT FOUND\\r\\n\
        headers = headers + \\\r\\n\
        client_socket.send(headers.encode('utf-8'))
    else:
        content = f.read()
        f.close()
        ''' 打开成功就返回状态码200'''
        response_body = content
        response_header = \HTTP/1.1 200 OK\\r\\n\
        response_header += \Content-Length:%d\\r\\n\% len(response_body) 
    # 在长连接的链接中 规定内容长度来验证每一次的请求 是否接收完数据
        response_header += \\\r\\n\
        response = response_header.encode(\utf-8\) + response_body
        client_socket.send(response)
    #client_socket.close() # 不断开保持长连接
def main():
    tcp_server_socket = socket(AF_INET,SOCK_STREAM)
    tcp_server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) 
    tcp_server_socket.bind((\127.0.0.1\,7788)) 
    tcp_server_socket.listen(128) 
    tcp_server_socket.setblocking(False)
    client_socket_list = list()
    while True: 
        print('等待新客户端连接.....')
        try:
        client_socket,clientaddr = tcp_server_socket.accept()
        print('IP端口号为{0}的客户端连接成功'.format(clientaddr))
        except Exception as ret:
        print('----没有新的客户端到来----')
        else:
        print('----只要没有产生异常，就意味着有新客户端连接成功')
        client_socket.setblocking(False) # 设置套接字为非堵塞方式
        client_socket_list.append(client_socket)
        for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024).decode(\utf-8\) 
            # 每一次recv并不是直接从对方客户端拿数据 而是从操作系统的缓存区域拿数据
        except Exception as ret:
            print('----这个客户端没有发送数据')
        else:
            if recv_data:
            service_client(client_socket, recv_data)
            else:
            print('客户端调用close')
            client_socket_list.remove(client_socket)
            client_socket.close() 
    tcp_server_socket.close() # 最后关服务器的监听套接字
    
if __name__ == '__main__':
    main()
```
    
* 操作系统的内存分为 内核的内存 和 普通进程使用的
* 每一次调用应用程序 就是把普通进程使用的内存中的内容 复制到内核内存区 查找调用相关内容
* 单进程单线程的效率瓶颈与 遍历一遍列表所需的时间有关 即轮询(Select)
* epoll ：有一个内存空间是http服务器和kernel共享的(内存映射) 减少复制的过程 并且所有套接字不通过轮询 而是通过事件通知来提高效率
* epoll仅支持linux 不支持Windows

```python
from socket import *
import re
import select
def service_client(client_socket, request):
    ''' 接收请求头'''
    #request = client_socket.recv(1024).decode('utf-8')
    #print(request)
    request_lines = request.splitlines()
    ret = re.search(r\/[^/1|\\D]*[^\\s]*\,request_lines[0]) if len(request_lines) else None
    file_name = ret.group(0) if ret else \baidu.html\
    print(\请求访问\,file_name)
    try:
        f = open(file_name[1:],'rb')
    except:
        headers = \HTTP/1.1 404 NOT FOUND\\r\\n\
        headers = headers + \\\r\\n\
        client_socket.send(headers.encode('utf-8'))
    else:
        content = f.read()
        f.close()
        ''' 打开成功就返回状态码200'''
        response_body = content
        response_header = \HTTP/1.1 200 OK\\r\\n\
        response_header += \Content-Length:%d\\r\\n\% len(response_body) 
# 在长连接的链接中 规定内容长度来验证每一次的请求 是否接收完数据
        response_header += \\\r\\n\
        response = response_header.encode(\utf-8\) + response_body
        client_socket.send(response)
    #client_socket.close() # 不断开保持长连接
def main():
    tcp_server_socket = socket(AF_INET,SOCK_STREAM)
    tcp_server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) 
    tcp_server_socket.bind((\127.0.0.1\,7788)) 
    tcp_server_socket.listen(128) 
    tcp_server_socket.setblocking(False)
    # 创建一个epoll对象
    epl = select.epoll()
    epl.register(tcp_server_socket.fileno(),select.EPOLLIN)
    client_socket_list = list()
    fd_event_dict = dict()
    while True: 
        fd_event_list = epl.poll() #默认堵塞 直到os检测到数据到来 通过事件通知方式告诉程序 解堵塞 返回列表中的每一个值都是元组[(fd,event),(套接字对应的文件描述符，这个文件描述符到底是什么事件 例如可以调用recv接收等)]
        for fd,event in fd_event_list:
            if fd == tcp_server_socket.fileno():
                client_socket,clientaddr = tcp_server_socket.accept()
                print('IP端口号为{0}的客户端连接成功'.format(clientaddr))
                epl.register(client_socket.fileno(),select.EPOLLIN)
                fd_event_dict[client_socket.fileno()] = client_socket
            elif event == select.EPOLLIN:
                # 判断已经连接的客户端是否有数据发送过来
                recv_data = fd_event_dict[fd].recv(1024).decode(\utf-8\) 
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    print('客户端调用close')
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]
    tcp_server_socket.close() # 最后关服务器的监听套接字
if __name__ == \__main__\:
    main()
```
    
## tcp/ip协议族  --- 一类协议的简称
* 应用层 HTTP协议/QQ 原始套接字可以从应用层直接到IP(网络攻击) (加请求头 包装请求体)
* 传输层 TCP / UDP 二者端口号可以重复 (加原/目的端口)
* 网际层 IP / 域名 / ICMP (加原/目的IP)
* 网络接口层 (加原/目的mac地址)

## OSI协议族分7层 但还是源于tcp/ip
* 应用层 表示层 会话层 对应应用层
* 传输层 对应传输层
* 网络层 对应网际层
* 数据链路层 物理层 对应网络接口层

## 两台电脑之间可以通过网络连接直接通信,但需要设置好IP和网络掩码,IP地址需要控制在同一网段
* 子网掩码用于确定网络号和主机号 确定处于同一局域网的IP
* 192              168                  0                147
* 1100 0000       1010 1000          0000 0000         1001 0011
* 默认生成子网掩码
* 255  \t           \t255 \t\t     255\t\t         0
* 1111 1111       1111 1111       1111 1111          0000 0000
* 按位与 与子网掩码的每一个二进制比较  只有全是1 才输出1 否则输出0 
* 1100 0000       1010 1000         0000 0000            0000 0000
* 192\t         \t168\t          \t    0\t            \t0
* 最后转为十进制就可以看出前两组数为网络号，后组为主机号
* 想要连接多个电脑形成网络，不能拆网线，应该加设备，比如hub集线器缺点是一直在广播，容易卡
* 交换机更强，该广播的时候广播，该单播的时候单播、
* 发送数据时必须带上对方的mac地址，对方用于识别是否丢掉接收到的数据
* 首先看arp广播列表中有没有对方的mac地址，若没有则通过arp广播，发给交换机，然后通过共有的mac地址(ff:ff:ff:ff:ff)传给所有连接的电脑
* 传到IP层通过特殊方法识别出正确的目的地，对方返回给发送者，获得对方IP的mac地址，之后通过单播发送数据
* 路由器最核心的功能是链接2个以上的网(交换机)形成1张大网，即1个路由器里面有多个网卡，分别链接多个网络
* 把具有接发数据能力的机器称为网关，一般就是路由器
* 在发送给路由器的数据包中，会带上原IP和原mac以及路由器的mac和目标IP，传到路由器之后由路由器转换为目标IP的mac地址
* 在传送的过程中，每经过1次转换mac地址就变1次，IP地址不变，因为IP地址仅仅是在逻辑上标记
* 每个大区都有自己的DNS服务器
* 浏览器向服务器发送请求大致过程如下
1. 解析域名：先通过arp获得默认网关的mac地址-向网关发送带有域名的请求-经过一层层互联网的mac地址的转换-传到DNS服务器查找对应IP地址-回送接收
2. 向服务器发送tcp 3次握手
3. 发送http的请求数据以及等待服务器的应答
4. 发送tcp 4次挥手

* 单核CPU 时间片轮转 只要转的够快就可以模拟多线程
* 并行：真的多任务
* 并发：假的多任务 CPU核数小于任务数
* 线程 是操作系统调度的单位 依赖于进程
* 多线程 一个程序执行起来后会有一个执行的箭头 称之为线程
* 多线程是指在一个进程(一坨资源)里面有多个箭头
### 多线程适用于:大量密集的I/O处理,输入输出操作,比如文件读写,网络爬虫操作
```python

import time,threading
def sing():
    for i in range(5):
        print('sing{0}....线程号{1}'.format(i,threading.current_thread()))
        time.sleep(1)
    # 如果创建Thread时执行的函数运行结束 那么意味着这个子线程结束

def dance():
    for i in range(10):
        print('dance{0}....线程号{1}'.format(i,threading.current_thread()))
        time.sleep(1)

def main():
    #tlist = list()
    t1 = threading.Thread(target=sing) #只写函数名 相当于传入一个变量名 确定该函数的位置
    t2 = threading.Thread(target=dance)
    t1.start() # 主线程会生出一个子线程 单独运行    
    t2.start() # 主线程生出第二个子线程 单独运行 但线程的先后运行是随机的
    #tlist.append(t1)
    #tlist.append(t2)
    #[n.join() for n in tlist] # 也可以用join()来调用线程 适用于1个函数 多次调用
    while True:
        print(threading.enumerate()) #查看当前的所有线程数
        if len(threading.enumerate())==2: #只有在指定函数执行完成之后 子线程才会结束
            break
        time.sleep(2)
        
def main2():
    print(threading.enumerate())
    t1 = threading.Thread(target=sing) #只是实例化一个对象 不会创建线程
    print(threading.enumerate())
    t1.start() # 当调用start方法时 才会创建线程以让这个线程开始运行
    print(threading.enumerate())
    
main()
#main2()

```

# 在一个函数中对全局变量进行修改可能不需要加global 
# 如果让全局变量指向了一个新的值 必须使用global

```python

import threading,time
class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm"+self.name+'@'+str(i)
            print(msg)
    
t = MyThread() #创建一个实例对象 只能对应一个子线程
t.start()

#I'mThread-12@0
#I'mThread-12@1
#I'mThread-12@2

```

* 多线程之间全局变量共享 改变一个则都变 但是不能两个都改 即同一时刻对变量操作
* 资源竞争 CPU会把语句命令复杂化 多个线程的命令会复杂化执行
* 同步 协同步骤 按预定步骤的先后顺序进行运行
* 互斥锁 保证多个线程几乎同时修改某个共享数据时 进行同步控制 解决资源竞争
* 死锁 二者都在等待对方解锁
* 避免死锁的方法：1.程序设计尽量避免(银行家算法) 2.添加超时时间

```python

import threading,time
g_num = 0
def test1(num):
    global g_num
    # 上锁，如果之前没有上锁，上锁成功
    # 如果之前已经有锁，则阻塞在这里直到对方解锁
    mutex.acquire()    
    for i in range(num):
        g_num += 1
    mutex.release() # 解锁
    print(f'----in test1 g_num={g_num}')
def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1  # 上锁部分越少越好
        mutex.release()
    print('-----in test2 g_num=%s'%(g_num))
mutex = threading.Lock()
def main():
    t1 = threading.Thread(target=test1,args=(1000000,))# args中传入参数元组
    t2 = threading.Thread(target=test2,args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(10)
    print('-----in main g_num=%s'%(g_num))
    
main()

# ----in test1 g_num=1000000
# -----in test2 g_num=2000000
# -----in main g_num=2000000

```

* 程序是静态的 在没有运行的时候 没有网络资源 而进程 是一坨资源的总称 
### 进程是资源分配的单位  多进程最稳定
* 一个进程里面最少有一个主线程 程序的执行由线程负责
### 线程是操作系统调度的单位  多线程稳定性一般
* 每创建一个子进程都会copy一份代码和资源 单独给子进程使用 
### 因此进程占用资源比线程多
* copy时代码和内存不会变 可以共享 但是数据可能改变 因此多进程全局变量不共享
* 写时拷贝 写的时候再拷贝
* 可以将进程理解为工厂的一条流水线 而其中的线程就是这个流水线上面的工人
* 不同的流水线之间 不共享全局变量
### 因此多进程适用于:大量的密集并行计算
* 下示使用多进程实现多任务 每一个资源里面有一个箭头"

```python

import multiprocessing
import time,os

def sing(n):
    for i in range(n):
        print('sing{0}....进程号:{1}'.format(os.getpid()))
        time.sleep(1)

def dance(n):
    for i in range(n):
        print('dance0}....进程号:{1}'.format(os.getpid()))
        time.sleep(1)
        
if __name__ == '__main__':
    #tlist = list()
    t1 = multiprocessing.Process(target=singargs=(5))
    t2 = multiprocessing.Process(target=danceargs=(5))
    t1.start()
    #tlist.append(t1)
    t2.start()
    #tlist.append(t2)
    #[n.join() for n in tlist] # 也可以用join方法调用进程 该方法适合1个函数 多次调用

# windows 系统只有在powershell中或cmd中运行才会有结果
# 在power shell中输入 ps 查看所有进程 kill 中止进程

```

# 多进程之间通信可以通过 socket 或 访问本地硬盘的文件 或 Queue队列(解耦 降低耦合性)

```python

from multiprocessing import Queue
q = Queue(3) # 最多接收3条消息 放多了或取多了都会堵塞 如果不传入参数 系统自动放最大
q.put('消息1')
q.put('消息2')
print(q.full()) #False
q.put('消息3')
print(q.full()) #True
print(q.qsize()) #获取队列长度
print(q.empty()) #False 非空
print(q.get()) # 消息1  block默认为True
# 如果队列为空，block=True，不会结束，会进入阻塞状态 直到队列有新的值
# 如果队列为空，block=False，会弹出一个Queue.empty()的异常
print(q.get_nowait()) # 消息2

```
```python

import multiprocessing
from multiprocessing import Queue
def download(q):
    '''模拟从网上下载数据'''
    data = [11,22,33,44]
    '''像队列中写入数据'''
    for i in data:
        q.put(i)
    print('下载完毕 并存入队列中')

def analysis(q):
    '''数据处理'''
    waitting_analysis = list()
    while True:
        data = q.get()
        waitting_analysis.append(data)
        if q.empty():
            break
    print(waitting_analysis)
    
def main():
    '''创建队列'''
    q = multiprocessing.Queue()
    '''创建多个进程，将队列的引用当作实参进行传递到里面'''
    t1 = multiprocessing.Process(target=download,args=(q,))
    t2 = multiprocessing.Process(target=analysis,args=(q,))
    t1.start()
    t2.start()
    
main()

```
```python
from multiprocessing.dummy import Pool # 在线程池中产生了异常 并不会抛出异常
import os,time,random
def worker(msg):
    t_start = time.time()
    print('%s开始执行,进程号为%d'%(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕,耗时%0.2f"%(t_stop-t_start))

po = Pool(3) # 最大进程数为3
for i in range(8):
    '''要调用的目标，需要的参数元组
    每次循环将会用空闲出来的子进程去调用目标'''
    po.apply_async(worker,(i,))
print("start".center(20,'-'))
po.close() # 关闭进程池 关闭后再开始执行 关闭后po不再接收新的请求
po.join() # 等待进程池中的所有子进程执行完毕 必须放在close语句之后
print("end".center(20,'-'))

```
```
-------start--------0
开始执行,进程号为131561
开始执行,进程号为13156
2开始执行,进程号为13156
1 执行完毕,耗时0.29
3开始执行,进程号为13156
3 执行完毕,耗时0.21
4开始执行,进程号为13156
2 执行完毕,耗时0.75
5开始执行,进程号为13156
4 执行完毕,耗时0.60
6开始执行,进程号为13156
6 执行完毕,耗时0.26
7开始执行,进程号为13156
0 执行完毕,耗时1.60
5 执行完毕,耗时1.64
7 执行完毕,耗时1.63
--------end---------0
```
    
### copy文件实例
```python
from multiprocessing.dummy import Pool
from multiprocessing import Manager,Queue
import os, time

def copy_file(queue,file_name, old_folder_name, new_folder_name):
    """完成文件的复制"""
    # print(\"=====>模拟copy[%s]文件:从%s--->%s\" % (file_name, old_folder_name, new_folder_name))
    old_f = open(os.getcwd() + '\\' + old_folder_name + '\\' + file_name,'rb')
    content = old_f.read()
    old_f.close()
    new_f = open(new_folder_name+'\\'+file_name,'wb')
    new_f.write(content)
    new_f.close()
    '''拷贝完文件之后就向队列写入一个消息'''
    queue.put(file_name)

def main():
    global new_folder_name
    old_folder_name = input('请输入要copy的文件夹')
    queue = Manager().Queue()
    try:
        new_folder_name = old_folder_name + "[附件]"
        os.mkdir(new_folder_name)
    except:
        print('wrong')

    po = Pool(5)
    for i in os.listdir(os.getcwd() + '\\\\' + old_folder_name):
        po.apply_async(copy_file, args=(queue,i, old_folder_name, new_folder_name))

    po.close()
    copy_ok_num = 0
    while True:
        # print('已经完成copy:',queue.get())
        copy_ok_num += 1
        print('\\r拷贝进度为%.2f %%'%(copy_ok_num*100/len(os.listdir(os.getcwd() + '\\\\' + old_folder_name))),end='')
        if len(os.listdir(os.getcwd() + '\\\\' + old_folder_name))==copy_ok_num:
            break
    # po.join()

if __name__ == "__main__":
    main()
```
# 实现进程池和线程池的另一种方法
```python

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from threading import Thread
import os,threading,time

def work(n):
    print('call:{0},process num:{1},thread num:{2}'.format(n,os.getpid(),threading.current_thread()))
    time.sleep(2)
    print('call {0} finished,process num:{1},thread num:{2}'.format(n,os.getpid(),threading.current_thread()))
# for i in ['a','b','c']:
#     work(i)

#创建线程池/进程池
pool = ThreadPoolExecutor(max_workers=3)
#pool = ProcessPoolExecutor(max_workers=3)
#循环指派任务
[pool.submit(work,user) for user in ['a','b','c']]
#关闭线程池
pool.shutdown()   

```
```
call:a,process num:1556,thread num:<Thread(ThreadPoolExecutor-0_0, started daemon 8916)>
call:b,process num:1556,thread num:<Thread(ThreadPoolExecutor-0_1, started daemon 4204)>
call:c,process num:1556,thread num:<Thread(ThreadPoolExecutor-0_2, started daemon 11656)>
call a finished,process num:1556,thread num:<Thread(ThreadPoolExecutor-0_0, started daemon 8916)>
call b finished,process num:1556,thread num:<Thread(ThreadPoolExecutor-0_1, started daemon 4204)>
call c finished,process num:1556,thread num:<Thread(ThreadPoolExecutor-0_2, started daemon 11656)>
```
# 迭代器
#### 可迭代对象 iterable 列表 元组 字典 字符串
* 迭代器只是存储生成数值的方法 因此占用内存更少 因此可以节省内存空间
* 不仅可以代替for循环使用 还可以节省类型转换所需要的内存 而类型转换其实也是利用迭代重新生成一个新的对象
```python
nums = list()
a,b = 0,1
i = 0
while i<10:
    nums.append(a)
    a,b = b,a+b    
    i+=1
for i in nums:
    print(i)
    
class Fibnacci:
    def __init__(self,num):
        self.num = num
        self.col_num = 0
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        if self.col_num < self.num:
            res = self.a
            self.a,self.b = self.b,self.b+self.a
            self.col_num += 1
            return res
        else:
            raise StopIteration
fib = Fibnacci(10)
for i in fib:
    print(i) # 结果一样
```
```python
from collections import Iterable,Iterator
# class Classmate(object): # 可迭代的不一定是迭代器
#     def __init__(self):
#         self.names = list()
#     def add(self,name):
#         self.names.append(name)
#     def __iter__(self):
#         '''加入该方法 变为可迭代对象 并且必须返回一个含有iter和next方法的实例'''
#         return ClassIterator(self) # 返回一个迭代器
# class ClassIterator:
#     def __init__(self,obj):
#         self.obj = obj
#         self.num = 0
#     def __iter__(self):
#         pass
#     def __next__(self):
#         if self.num < len(self.obj.names):
#             res = self.obj.names[self.num]
#             self.num += 1
#             return res
#         else:
#             raise StopIteration

class Classmate: # 迭代器一定可以迭代 迭代器里面存储的不是数值 而是生成数值的方法
    def __init__(self):
        self.names = list()
        self.num = 0
    def __iter__(self):
        return self
    def add(self,name):
        self.names.append(name)
    def __next__(self):
        if self.num < len(self.names):
            res = self.names[self.num]
            self.num += 1
            return res
        else:
            raise StopIteration

classmate = Classmate()
classmate.add('a')
classmate.add('b')
classmate.add('c')
# print(isinstance(classmate,Iterable)) # 判断该对象是否是可迭代对象
# print(isinstance(iter(classmate),Iterator)) # 判断__iter__方法的返回值是否是迭代器
# print(next(iter(classmate)))

for i in classmate:
    print(i)
# 1.判断是否有__iter__2.判断调用iter()函数得__iter__方法的返回值是否是迭代器
# 3.每迭代一次调用一次next()函数 返回一次__next__方法的返回值

```
```
a
b
c
```
```python

from collections import deque
queue = deque(range(10)) # 队列，先进先出
queue.append(88)
print(queue) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 88])
queue.popleft() # 0

ll = [1,2,3,4]
ll.append(8) #堆栈，后进先出
print(ll) # [1, 2, 3, 4, 8]
print(ll.pop()) # 8

```
  
# 生成器 是一种特别的迭代器 可以用于暂停函数并保留数据
## 将列表推导式的方括号改为圆括号
```python
a = [i*2 if pow(i*2,1/2)%2 == 0 else None for i in range(1,11)]
print(type(a)) # list 
b = (i*2 if pow(i*2,1/2)%2 == 0 else None for i in range(1,11))
print(type(b)) # generator
```
## 函数中只要有yield关键字就不是函数而是生成器
```python

def create_num(all_num):
    print('1'.center(10,'-'))
    a, b = 0, 1
    num = 0
    while num < all_num:
        print('2'.center(10,'-'))
        # print(a)
        # yield a
        ret = yield a
        print(ret)
        print('3'.center(10,'-'))
        a, b = b, a+b
        num += 1
        print('4'.center(10,'-'))
    return 'done'.center(10,'-')
obj = create_num(4) # 创建一个生成器对象,可以创建多个对象，之间互不影响

# 用循环调用生成器
#for i in obj:
#    print(i)
print(iter(obj))

# 用next调用生成器,每一次会在执行过程中，遇到yield就中断，下次又继续执行
while True:
    try:
        print(next(obj))
    except StopIteration as m:# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
        print('Generator return value:',m.value) 
        break

# 用send调用生成器 可以传入参数作为生成器内部的参考 影响生成器的取值
obj.send(None) # 无法将非None值传给一个刚创建的生成器
print(next(obj))
obj.send('ret') # 送到并赋值给yield左边的变量 ret只被传一次 因此第二次是None
print(next(obj))

```
```python
<generator object create_num at 0x00000210AE1C49A8>

----1-----

----2-----

None

----3-----

----4-----

----2-----

1

ret

----3-----

----4-----

----2-----

None

----3-----

----4-----

----2-----

2
```
* 所谓协同程序就是可以运行的独立函数调用，函数可以暂停或挂起，并在需要的时候从程序离开的地方继续或重新开始
```python
iterA = iter([1,2,3,4])
print(next(iterA)) # 每调用一次访问一个元素，一直到访问完抛出stopiteration
```
# 协程稳定性最差 但最快
* 协程耗费的资源小于线程  是依托于线程的
* 协程 yield 实现多任务并发(假的并行)
* 协程是利用线程开发中 等待堵塞的时间来执行其他任务
* 因此在很多需要等待的任务中 比如爬虫下载网络数据 优先用协程
```python
import time
def task_1():
    while True:
        print('--1--')
        time.sleep(0.1)
        yield
def task_2():
    while True:
        print('--2--')
        time.sleep(0.1)
        yield
def main():
    t1 = task_1()
    t2 = task_2()
    while True:
        next(t1)
        next(t2)
main()
```
```python
from greenlet import greenlet # greenlet对yield实行了封装 用起来更为方便
import time
def task_1():
    while True:
        print('--1--')
        gr2.switch()
        time.sleep(0.1)
def task_2():
    while True:
        print('--2--')
        gr2.switch()
        time.sleep(0.1)
gr1 = greenlet(task_1)
gr2 = greenlet(task_2)
gr1.switch()
```
```python
import gevent  # 凡是需要用到延时操作的，都需要把堵塞的方法换成gevent里面对应的方法
from gevent import monkey 
monkey.patch_all()  # 或者打个补丁
def f1(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(0.5)
def f2(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(0.5)
g1 = gevent.spawn(f1,5)
g2 = gevent.spawn(f2,5)
g1.join() # 遇到演示操作就会创建协程 执行其他语句
g2.join()
gevent.joinall([
    gevent.spawn(f1,5),gevent.spawn(f2,5)  # 更简洁的方法是将对象放在一起调用
])
```
* GIL是全局解释器锁，会保证多线程程序同一时刻只有一个线程在跑
* 只有cpython因为历史原因有GIL，如果不是cpython而是其他解释器就可以用多线程实现并行来节省资源
* 主线程死循环，单线程占满cpu中的1个核
```python
while True:
    pass
```
* 多线程只是假的并发,并不会占用CPU多核,虽然节省了资源，但速度比不上多进程,可以用htop检验发现2个核都只占了一半
```python
import threading

def test():
    while True:
        pass

t1 = threading.Thread(target=test)
t1.start()  # 子线程死循环

while True:  # 主线程死循环
    pass
```
* 多线程还是要比单线程要快，计算密集型--大量计算/挖矿(用多进程)，io密集型--U盘读写/网络读写(用多线程或协程)
* 多进程才是真正的多核并行，可以htop检验发现2个核都占满了
```python
import multiprocessing

def deadLoop():
    while True:
        pass

#子进程死循环
p1 = multiprocessing.Process(target=deadLoop)
p1.start()

#主进程死循环
deadLoop()
```
* 想要解决GIL带来的问题，真正用多线程实现多核并行，可以换一个解释器或换一种语言
* 比如c语言
```C
#include<stdio.h>

void DeadLoop()
{
    while(1)
    {
        ;
    }
}

int main(int argc, char **argv)
{
        printf("编译型语言需要先进行gcc编译成二进制文件a.out,才能执行\n");
        return 0;
}
```
* 或者用python调用C
```python
from ctypes import *
from threading import Thread

#把一个ｃ语言文件编译成一个动态库的命令（linux平台下）:
# gcc xxx.c -shared -o libxxxx.so

#加载动态库libdead_loop.so
lib = cdll.LoadLibrary(\"./libdead_loop.so\")

#创建一个子线程，让其执行ｃ语言编写的函数，此函数是一个死循环
t = Thread(target=lib.DeadLoop)
t.start()

#主线程
while True:
    pass
```
* 抓包工具:[千峰fiddler](https://www.bilibili.com/video/av45394845?p=7)&[传智播客fiddler](https://www.bilibili.com/video/av62303270?p=4)&[千峰charles](https://www.bilibili.com/video/av76899389?p=3)
* [wireshark](https://www.bilibili.com/video/av81257032/?p=86):From top to bottom are the number of packets,the contents of the packets, and the specific hexadecimal display of the packets in memory.

* 动态页面的技术<u>javascript jquery Ajax DHTML</u>
1. 直接从Javascript 代码里面采集内容(费时费力)
2. 用第三方库运行JavaScript，直接采集在浏览器看到的页面
* Selenium 需要与第三方浏览器结合使用 支持所有主流的浏览器 可以进行截屏
* 可以用无界面浏览器教程：[PhantomJS-千峰](https://www.bilibili.com/video/av45394845?p=58)
* 因为PhantomJS无人维护 也可以用无头谷歌浏览器参考教程[headless chrome-千峰](https://www.bilibili.com/video/av45394845?p=65)
* 因为selenium不再支持PhantomJS 故采用headless firefox [geckodriver](https://github.com/mozilla/geckodriver)

* 验证码的解决
* 把图片下载下来 人眼识别input
* ORC库 图像光学识别 只能识别简单的
>* Tesseract在官网安装 是一个python的命令行工具 在web使用 一般用于验证码登录
>* 先在系统中设置新的环境变量 然后放一份tessdata在Tesseract目录下
>* `pip install pytesseract` 安装python版本的Tesseract 结合PIL使用

* 云打码 注册普通用户、开发者 参考教程[千峰](https://www.bilibili.com/video/av45394845?p=78)
>* 使用云打码时 在我的软件中新加一个软件"

# urllib
```python
import urllib.request, urllib.parse, urllib.error, urllib.robotparser
import http.cookiejar
try:
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    # some url must cookie (proxyHandler HTTPSHandler HTTPRedirectHandler)
    # urllib.request.install_opener(opener)
    url = \"https://www.baidu.com/s?wd=\"  # 定义请求地址
    headers = {'User-Agent': 'Mozilla/5.0 3578.98 Safari/537.36', }  # 定义自定义请求头
    postdata = urllib.parse.urlencode().encode('utf-8')
    request = urllib.request.Request(url=url + urllib.parse.quote(wd), headers=headers)  # 定义请求对象
    response = urllib.request.urlopen(request, timeout=15)  # take a time发送请求
    # url = ur.Request('http://ac.scmor.com/')
    # url.add_data('a','1')
    # url.add_header('User-Agent','Mozilla/5.0')
    # urllib.request.urlretrieve('https://www.baidu.com','baidu.html')直接将百度页面的html保存到文件中
    # urllib.request.urlcleanup()清除缓存
    html = response.read()  # 300 words
    print(html.decode('utf-8')) 
    # print(response.getcode())print(response.info())print(response.geturl())
    # print(cj)
    response.close()
except urllib.error.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    elif hasattr(e, 'reason'):
        print(e.reason)
```
 
## requests
+ 拟爬取: [your name的图片](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1580960249421&di=fc1d6365ad60bdc379752936d2aec931&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2F4b742d8ba786c6d7041278073633b396150d779a32e86-705oar_fw658) 
+ 并利用numpy修改图片灰度值
* ![your name](https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1581990576&di=a0c074ab281601ca59a581f660e3823a&src=http://cdn.vox-cdn.com/thumbor/3gx7OvAytfYj70moLh8Kax-1eDw=/0x0:1920x1080/1200x0/filters:focal(0x0:1920x1080):no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/8303383/yournamecomet.jpg)"

# Analysis
## numpy,scipy,pandas,matploblib,seaborn
## plotly 是 github 上面的动态图像处理项目 在后端绘制  兼容matplotlib和pandas 
* 爬取西刺代理
```python
import random
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
headers={'user-agent':random.choice(user_agent),'Host':'timgsa.baidu.com',
         'Accept':'text/plain, */*; q=0.01', # 一般不写accept 以防接收到的文件受限
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding':'gzip, deflate, br',
'Referer':'https://www.baidu.com/index.php?tn=monline_3_dg',
'X-Requested-With':'XMLHttpRequest','Connection':'keep-alive'}

class get_proxies:
    proxies = [{"https": "https://222.95.144.120:3000"},
               {"https": "https://175.42.122.109:9999"}]

    def __init__(self, num):
        self.main(num)

    def xici_ip(self, page):
        for num_page in range(1, page + 1):
            url_part = "https://www.xicidaili.com/wn/"
            # 爬取西刺代理的IP，此处选的是国内https
            # 构建爬取的页面URL
            url = url_part + str(num_page)
            r = requests.get(url, headers={'User-Agent': random.choice(user_agent)})
            r.raise_for_status()
            soup = BeautifulSoup(r.text, 'lxml')
            trs = soup.find_all('tr')
            for i in range(1, len(trs)):
                tr = trs[i]
                tds = tr.find_all('td')
                ip_item = tds[1].text + ':' + tds[2].text
                # print('抓取第'+ str(page) + '页第' + str(i) +'个：' + ip_item)
                self.proxies.append({'HTTPS': 'HTTPS://' + ip_item})
            #                 time.sleep(1)
            print('存储成功')

    def check_ip(self):
        try:
            headers = {'user-agent': random.choice(user_agent)}
            for item in self.proxies:
                r = requests.get('http://httpbin.org/ip', headers=headers,
                                 proxies=item)
                r.raise_for_status()
                r.encoding = r.apparent_encoding
                if not r.json()['origin'].split(',')[0] == '125.80.138.167':
                    self.proxies.remove(item)
                    print('获取IP无效')
        except Exception as e:
            print(e)

    def main(self, n):
        self.xici_ip(n)  # 抓取第n页，一页100个url
        try:
            self.check_ip()
        except Exception as e:
            print(e)
            self.check_ip()
```

```python
from lxml import etree
url = 'http://e.dangdang.com/new_original_index_page.html'
headers = {'user-agent':random.choice(user_agent),'Host':'img61.ddimg.cn'}
proxies_2 = get_proxies(1)
response = requests.request("get",url,headers=headers,
                            proxies=random.choice(proxies_2.proxies))
response.raise_for_status()
response.encoding = response.apparent_encoding
html = etree.HTML(response.text)
basic_url = html.xpath('/html/body/div[5]/div[1]/div[1]/div[1]/ul/li[2]/a/@href')[0]
url2 = "http://e.dangdang.com"+basic_url[1:]
print(url2)
headers = {'user-agent':random.choice(user_agent),'Host':'img61.ddimg.cn'}
response = requests.request("get",url2,headers=headers,
                            proxies=random.choice(proxies_2.proxies))
response.raise_for_status()
html2 = etree.HTML(response.text)
print(html2.xpath('//*[@id="book_list"]')) # js动态生成的网址爬不到

# 需要基础抓包分析
# 观察F12中的XHR类型文件的响应(response)是否符合动态生成的内容
url = 'http://e.dangdang.com/media/api.go?action=mediaCategoryLeaf&promotionType=1&deviceSerialNo=html5&macAddr=html5&channelType=html5&permanentId=20200204092203962235681531963345504&returnType=json&channelId=70000&clientVersionNo=5.8.4&platformSource=DDDS-P&fromPlatform=106&deviceType=pconline&token=&start=0&end=20&category=KHLY&dimension=sale'
headers = {'user-agent':random.choice(user_agent),'Host':'e.dangdang.com'}
response = requests.request("get",url,headers=headers,
                            proxies=random.choice(proxies_2.proxies))
response.raise_for_status()
for i in range(21):
    print(response.json()['data'].get('saleList')[i]['mediaList'][0]['coverPic'])
    # json.loads(response.text) # json==>python
    # json.dump(response.text,open('json.txt','w',encoding = 'utf-8'))
    # json.load(open('json.txt','r',encoding='utf-8')) # 从文件中读取json==>python
```
* `selenium`无头浏览器爬取动态页面
```python
from selenium import webdriver
# 调用键盘按键操作时需要引入的Keys包
from selenium.webdriver.common.keys import Keys

profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.http', '120.83.107.146')
profile.set_preference('network.proxy.http_port', 9999)  # int
profile.update_preferences()
# 如果没有配置环境变量 则需指定Firefox位置
driver = webdriver.Firefox(executable_path="",firefox_profile=profile)
driver.get('http://httpbin.org/ip')

driver.get("http://www.baidu.com/")
# 获取页面名为 wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text
# 生成当前页面快照并保存
driver.save_screenshot("baidu.png")
# id="kw"是百度搜索输入框，输入字符串"长城"
driver.find_element_by_id("kw").send_keys(u"长城")
# id="su"是百度搜索按钮，click() 是模拟点击
driver.find_element_by_id("su").click()
# 获取新的页面快照
driver.save_screenshot("长城.png")
# 清除输入框内容
driver.find_element_by_id("kw").clear()
# 输入框重新输入内容
driver.find_element_by_id("kw").send_keys("itcast")
# 模拟Enter回车键
driver.find_element_by_id("su").send_keys(Keys.RETURN)

# 打印网页渲染后的源代码
print(driver.page_source)
# 获取当前页面Cookie
print(driver.get_cookies())
# 打印页面标题 "百度一下，你就知道"
print(driver.title)
# 获取当前url
print(driver.current_url)

# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')

# find_element_by_id
# find_elements_by_name
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector
# find_elements_by_xpath # 输入xpath匹配

# 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()

# 关闭浏览器
driver.quit()
```
  
```python
# 配置环境变量的时候需要 配置tessdata 的位置
from pytesseract import *
from PIL import Image
image = Image.open("XXX.png") # 打开图片文件
text = image_to_string(image) # 调用函数图片转字符串
print(text)
img = image.convert('L')
img.show()
threshold = 140
table = list()
for a in range(256):
    if a < threshold:
        table.append(0)
    else:
        table.append(1)
out = img.point(table,'1')
out.show()
```
  
```python
import unittest
from selenium import webdriver

class douyu(unittest.TestCase):
    def setUp(self):
        # 初始化无头浏览器
        self.driver = webdriver.Firefox(executable_path="",firefox_profile=profile)
    def testXX(self):
        self.driver.get("XXX")
        while True:
            if self.driver.page_source.find("XXX") != -1:
                break
            self.driver.find_element_by_xpath("XXX").click()
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()
```
  
```python
from lxml import etree
start_url = "https://www.bilibili.com"
'''
User-agent: *
Disallow: /include/
Disallow: /mylist/
Disallow: /member/
Disallow: /images/
Disallow: /ass/
Disallow: /getapi
Disallow: /search
Disallow: /account
Disallow: /badlist.html
Disallow: /m/
'''
kw = {"user-agent":random.choice(user_agent),'Host':'message.bilibili.com'}
try:
    response1 = requests.request('get',start_url,headers = kw,
                                 proxies = random.choice(proxies_2.proxies))
    response1.raise_for_status()
    response1.encoding = response1.apparent_encoding
except Exception as e:
    print(str(e))
html1 = etree.HTML(response1.text)
print(html1.xpath('/html/body/div[2]'))
url2 = "https://www.bilibili.com/video/av45394845?p=81"
```
  
```python
url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1580960249421&di=fc1d6365ad60bdc379752936d2aec931&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2F4b742d8ba786c6d7041278073633b396150d779a32e86-705oar_fw658'
response = requests.request("get",url,headers=headers,
                            proxies=random.choice(get_proxies(2).proxies))
response.raise_for_status()
response.encoding = response.apparent_encoding
#response.text  response.content.decode('utf-8')
direct = 'c:/Users/向致承/Desktop/'
open(direct+'your_name.jpg','wb').write(response.content)
open(direct+'your_name2.jpg','wb').write(response.content)
#RGB色彩模式(0-255),需要PIL库,pip install pillow
from PIL import Image
import numpy
im = numpy.array(Image.open(direct+'your_name2.jpg').convert('L')).astype('float') 
#convert成灰度图片,在转换可得黑白图
print(im.shape,im.dtype) #图像由三维数组表示,高度，宽度，像素RGB
depth = 10
grad = numpy.gradient(im)
grad_x ,grad_y = grad
grad_x = grad_x * depth/100
grad_y = grad_y * depth/100
A = numpy.sqrt(grad_x**2 + grad_y**2 +1)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1/A
vec_el = numpy.pi/2.2
vec_az = numpy.pi/4
dx  = numpy.cos(vec_el)*numpy.cos(vec_az)
dy = numpy.cos(vec_el)*numpy.sin(vec_az)
dz = numpy.sin(vec_el)
b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)
a = b.clip(0,255)
# a = 255 - im #换成黑白图
# a = (100/255)*im + 150 # 区间变换
# a = 255 * (a/255)**2 #像素平方
im = Image.fromarray(a.astype('uint8'))
im.save(direct+'your_name2.jpg')
```
  
* json    信息有类型，适合程序处理，较xml简洁，无注释，一般用在程序对接口的部分
* YAML  信息无类型，文本信息比例最高，可读性好，用于各类系统的配置文件，有注释易读
* xml  最早的通用信息标记语言，可扩展性好但繁琐，用于Internet上的信息交互与传递
## jsonpath(json path)
* [参考blog](https://blog.csdn.net/luxideyao/article/details/77802389)
* [参考视频-千峰1](https://www.bilibili.com/video/av45394845?p=55)
* [参考视频-传智播客](https://www.bilibili.com/video/av62303270?p=22)
* [参考视频-千峰2](https://www.bilibili.com/video/av76899389?p=20)"

# re
+ [在线验证正则:regex](https://regex101.com/)
```python
import re
# 模式修正符flags=
# A 使转义字符\\w,\\b,\\s,\\d只能匹配ASCII字符
# I 匹配时忽略大小写
# M 多行匹配 影响 ^$
# L 本地化识别匹配,支持当前的地区语言
# U 根据Unicode字符集解析字符。这个标志影响 \\w, \\W, \\b, \\B.
# S 让.匹配包括换行符
# X 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
print(re.search('Pyt', 'python', re.I).group(0))  # pyt
print(re.search('Pyt', 'python', re.I).start())  # 0
print(re.search('Pyt', 'python', re.I).end())  # 3
print(re.search('Pyt', 'python', re.I).span())  # (0,3)
print(re.search('Pyt', 'python', re.I).string)  # python
print(re.search('Pyt', 'python', re.I).re)  # re.compile(r'Pyt', re.UNICODE)
print(re.search('Pyt', 'python', re.I).pos)  # 0
print(re.search('Pyt', 'python', re.I).endpos)  # 6

print(re.split(r'\\d', '123abc', maxsplit=1, flags=re.U))  # ['', '23abc']
# 将字符按照正则表达式进行分割,此处匹配到的数字会被切掉,超出最大分割数的部分作为最后一个元素被输出
re.findall(r'\\d', 'iloveyou531tosimida')  # 规则,字符串,['5','3','1']
# 当使用转义字符时在前面加个'r'若使用string模块则需要用\\\\d表示\\d
re.findall(r'\\d{3}', 'iloveyou531tosimida')  # ['531']
print(next(re.finditer(r'\\d', 'iiii44ii')))  # 只能看到第一个
print(list(re.finditer(r'\\d', 'iirr44rr4')))  # 可以看到一个对象列表
print(next(re.finditer(r'44', 'iiii44ii')))
for i in re.finditer(r'44', 'iiii44ii'):
    print(i.group(), re.S)
res = re.match(r'ilove', 'iloveyou', flags=0)  # 从头开始匹配只匹配开头一次,返回None或者match对象,flags=0表示单行匹配
print(res, res.group(), res.span())  # group返回字符串,span返回下标
rep = re.search(r'love', 'iloveyou', flags=0)
# 不从头开始匹配 只匹配一次,返回None或者match对象,flags=0表示单行匹配
print(bool(re.sub(r'\\d', 'i', '2loveyou', count=1) == re.sub(r'\\d{2}', 'i', '22loveyou', count=1)))  # count代表匹配的最大替换数
def add(temp):
    strNum = temp.group()
    num = int(strNum)+1
    return str(num)
ret = re.sub(r\"\\d+\",add,\"python = 997\")
print(ret) #将匹配到的对象作为参数传到add函数中 再将结果替换到字符串中
str1 = 'iloveeyou44tosimi67da'
reg = re.compile(r'\\d{2}')
print(reg.findall(string=str1))
print(reg.search(str1).group())

var = '\\n$_2 iloveyou5211'
res = r'love'
print(re.search(res, var).group())  # 'love'

# \\可以解除字符的特殊功能, \\.表示匹配点号本身
# 引用字符的ASCII码的八进制 来匹配该字符
re.search('\\{}'.format(oct(ord('b'))[-3:]), 'b').group()  # 'b'
# 引入1-99表示匹配字符对应的序号
re.search(r'(fishc)\\1', 'fishcfishcfishc').group()  # 'fishcfishc'
# '\\w' 单个字母/数字/下划线
# '\\W' 单个非字母/非数字/非下划线
# '\\D' 单个非十进制数字
# '\\s' 单个的空格符/制表符
# '\\S' 单个非空格符/非制表符
# '\\w\\w\\w\\w\\d' 组合使用连续4个加1个数字
# \\A 匹配字符串开始
# \\Z 匹配字符串结束,如果是存在换行,只匹配到换行前的结束字符串。
# \\z 匹配字符串结束
# \\G 匹配最后匹配完成的位置。
# \\b 匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\\b' 可以匹配\"never\" 中的 'er'，但不能匹配 \"verb\" 中的 'er'。
# \\B 匹配非单词边界。'er\\B' 能匹配 \"verb\" 中的 'er'，但不能匹配 \"never\" 中的 'er'。
# \\n  匹配一个换行符
# \\t  匹配一个制表符
print(re.search(r'\\w', var).group())  # _
print(re.search(r'\\w{2,5}', var).group())  # 必须匹配次数的区间,返回最大次数
print(re.search('[a-z,A-Z,0-9,_]', var).group())  # 中括号代表范围,此处等同于\\w
# [...] 规则如下
# 注1：连字符 - 如果出现在字符串中间表示字符范围描述；如果如果出现在首位则仅作为普通字符
# 注2：特殊字符仅有反斜线 \\ 保持特殊含义，用于转义字符。其它特殊字符如 *、+、? 等均作为普通字符匹配
# 注3：脱字符 ^ 如果出现在首位则表示匹配不包含其中的任意字符；如果 ^ 出现在字符串中间就仅作为普通字符匹配
# [abc] -- a或b或c    [^abc] -- 非a非b和非c
# pyth[^a]n -- python或pythbn...
# pyth{:3}n -- pytn或pythn或pythhn或pythhhn 
# pyth{2,}on -- h至少2次
# pyth{2,4}on -- h至少2次至多4次
# ^[A-Za-z]+$ -- 任意连续个数的字母
# ^[A-Za-z0-9]+$ -- 任意连续数字的字母或数字
# ^-?\\d+$ -- 整数形式的字符串
# ^[0-9]*[1-9][0-9]*+$ -- 正整数形式的字符串
# [1-9]\\d{5} -- 中国境内邮编 6位
# [\\u4e00-\\u9fa5] -- 匹配中文字符
# \\d{3}-\\d{8}|\\d{4}-\\d{7} -- 电话号码
# IP地址范围为[0-255],分成四段
# (([1-9]?\\d|1\\d{2}|2[0-4]\\d|25[0-5])\\.){3}([1-9]?\\d|1\\d{2}|2[0-4]\\d|25[0-5])
print(re.search('\\w+\\d{4}', var).group())
print(re.search('\\w+(\\d{4})', var).group())  # 返回整体匹配内容
# ()代表子组,括号中的表达式首先作为整个正则的一部分另外会把符合小括号的内容单独提取 可以用于避免|引发的错误 规定了|发挥的范围
# \\1...\\9  匹配第n个分组的内容。如果它经匹配。否则指的是八进制字符码的表达式。
print(re.search(r'<(\\w*)>.*</\\1>','<h1>hahha</h1>').group())
#\\1意思是第一个括号里面的匹配的是啥 此处就必须一样
# 为了避免匹配序列的错误 可以将匹配字符命名
print(re.search(r'<(?P<A>h1)>.*</(?P=A)>','<h1>hashh</h1>').group()
# (?P<A>这里写正则表达式) 把这个分组匹配到的字符命名为A (?P=A) 再匹配这个子组的字符时就可以用A代替 而不是\\1
print(re.search('\\w+(\\d{4})', var).groups())  # 返回小括号的匹配内容('5211',)
print(re.search('(\\w+(\\d{4}))', var).groups())  # ('iloveyou5211', '5211')
print(re.search('^2\\d{3}', '2345').group())  
# ^匹配开头 $匹配结尾     
# ^abc -- abc且在一个字符开头 abc$ -- abc且在一个字符结尾
# '.' 任意字符除了换行符
# '*' 代表匹配次数,可为任意次(可为0)
# 如果符合就一直匹配直到不符合,一开始就不符合那么就返回空,任务完成
# abc* -- ab或abc或abcc... abc+ -- abc或abcc或abccc...
print(re.search('\\w*', ' hello').group())
# '+' 代表匹配次数,至少匹配一次任务才算完成,如果一开始就不符合那么往后找
# 如果一直符合就一直往后
print(re.search('\\w+', ' hello').group())
# '?' 拒绝贪婪,前面的要求只要达成就返回,表示前一个字符0或1次的扩展
# ab? -- ab或abb
print(re.search('\\w+?', 'hello world').group())  # 'h'
print(re.search('\\w*?', 'hello world').group())  # ''
print(re.search(r'Py??', 'pythonpython', re.I).group())  # 'p'
print(re.findall('h|w', 'hello world'))  # ['h','w']
print(re.compile('p.*?y').findall('python'))
```

# bs4
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text,'lxml') # html.parser,xml,html5lib
print(soup.prettify(encoding='utf-8',formatter='minimal'))#结果更美观,树形结构更为直观

#soup.find_all() 可以简写成 soup()
#soup.find() 只能找到第一个
#soup.title soup.name
for i in soup.find_all('a'):  #也可用在标签上
    print(i.prettify())
for i in soup.find_all(True,recursive = False,string = '网易云课堂'):  
    print(i.name) #取所有的标签的名,再取所有子节点,其中满足字符要求的部分
    print(i.text) #print(i.get_text())
#for i in soup.find_all('a',target=\"_blank\")
#for i in soup.find_all('a','_blank')
#for i in soup.find_all('a',target=re.compile('link')) 
#正则表达式可以检索包含link的字符串

#find_parents() find_parent() find_next_siblings()
#find_next_sibling() find_previous_siblings() find_previous_sibling()
tag = soup.a #只能获得第一个a标签 等同于 tag = soup.find('a')
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

r = soup.select('title')#获取所有含有'title'属性的标签，返回一个列表
print(r[0].text)
for i in r:
    print(i['con']) # 打印所有title值为con的标签
    infos = list(i.stripped_strings) # 返回纯文本列表
    print(infos)
print(soup.select('.container'))#获取所有类中class属性为container的类，返回一个列表
print(soup.select(\"tr[class='container']\") # 所有class属性为container的tr标签
print(soup.select('#btnCloseUpdateBrowser'))#id=btnCloseUpdateBrowser的类，返列表
print(soup.select('html body a'))#html里面的body里面的a标签
print(soup.select('p,title'))#所有含p或title的标签
```

# xpath (xml path)
```python
from lxml import etree
# html = etree.parse(source='text.html', etree.HTMLParser(encoding='utf-8')) 
# 从文件中读取 解析器默认为xml 此处设为html解析器
html = etree.HTML(response.text)
print(html.xpath('/html/body/script[1]/text()')) #此处索引从1开始
print(html.xpath('/html/head/meta[@name=\"keywords\"]/@content'))
print(html.xpath('/html/body/script[1]/text()'))
# print(html.xpath('/html/body/script/text()'));print(html.xpath('//script/text()'))
print(html.xpath('//div[@class=\"browser-edition-tip\"]/span/text()'))
print(html.xpath('//*[@class=\"browser-edition-tip\"]/span/text()'))  # *代表所有标签
a = html.xpath('//div[starts-with(@class,\"browser-edition-tip\")]')  
# class属性以dictionary开头的div属性中的text
for i in a:
    if len(i.xpath('//a/text()')) != 0:
        print(i.xpath('//a/@class'))
print(html.xpath('//span/text()'))  # 只能获得span属性下的text
print(html.xpath('string(//span)').replace(' ', '').replace('\\n', ''))  
# 可以获得包括span子属性的text
# result = etree.tostring(html)
# print(result.decode('utf-8'))
```

# scrapy
* pip install scrapy 可能需要开个VPN;另外还需安装(PFW里面) Twisted
* scrapy fetch --nolog （http://www.evenyan.com/post/6） 最简单的爬取网站
* scrapy startproject 创建项目后加项目名
* scrapy genspider 生成爬虫文件后加文件名和要爬取的域名
* scrapy genspider -l 查看爬虫模板 后加爬虫文件名和域名
* scrapy runspider 运行爬虫
* scrapy settings --get botname 显示配置
* scrapy crawl 运行爬虫后加爬虫名
* scrapy crawl book -o book.json/book.jsonl/book.csv/book.xml 输出不同格式的文件
* scrapy shell  --nolog 调试工具后加域名
* scrapy view 在浏览器打开某个网页
* scrapy check 检查爬虫是否合格

# python基本语法
```python
action = '2'
if action in ['1','2','3']:
    print(action)
if action == '1' or action == '2' or action == '3':
    print(action)
# 将复杂的条件多行化
for a in range(10):
    if ((a<3)
        or (a>8)):
        print(a)
```
* 第一个游戏--猜数字
```python
import random
secret = random.randint(1,10)
print ('Game Begin'.center(25))
temp = input ('please guess a number from 1 to 10:')
p = int(temp)
if p == secret:
    print ('Bingo')
elif 1<= p <= secret:
    print ('be bigger')
elif secret <= p <= 10:
    print ('be smaller')
def compare(temp):
    temp = input ('try it again:')
    p = int(temp)
    if p == secret:
        print ('Bingo')
    elif 1<= p <= secret:
        print ('be bigger')
    elif secret <= p <= 10:
        print ('be smaller')
    else:
        print ('please guess from 1 to 10')    
while 1 <= p <= 10 and p != secret:
    compare(temp)
while p < 1 or p > 10:
    temp = input ('try it again from 1 to 10:')
    p = int(temp)
    if p == secret:
        print ('Bingo')
    elif 1<= p <= secret:
        print ('be bigger')
    elif secret <= p <= 10:
        print ('be smaller')
while 1 <= p <= 10 and p != secret:
    compare(temp)
print ('Game Over'.center(25))
```
* [tkinter--小甲鱼GUI](https://www.bilibili.com/video/av4050443?p=65)
```python
import tkinter

fm_main = tkinter.Tk()  # 创建一个窗口

ent = tkinter.Entry(fm_main)  # 指定这个entry控件显示在fm_main上,Entry只是单行文本框
ent.pack()  # pack的上下关系体现了在窗口中的上下关系

ent1 = tkinter.Entry(fm_main)

ent2 = tkinter.Text(fm_main)  # Text是多行文本框


def hello():
    ent_str = ent.get()
    ent1.insert(index='end', string='你好,' + ent_str + ',欢迎回家!')
    ent2.insert('end', 'hello,' + ent_str + ',welcome back!')
    print(ent2.get(index1=1.0, index2=\"end\"))  # 从第1行第1个字开始一直读到最后


btn = tkinter.Button(fm_main, text='press here', command=hello)  # 创建一个按钮
btn.pack()

ent1.pack()
ent2.pack()

fm_main.mainloop()
```
```python
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')
import glob
glob.glob('*.py') # 获取本路径下的所有py文件

```
```python
str1 = '人生苦短'
print(repr(str1)) #repr产生一个解释器易读的表达形式:"'人生苦短'"
b1 = bytearray(str1.encode())
print(b1.decode()) # 人生苦短
b1[:6] = bytearray('生命'.encode()) # bytearray类型支持切片修改 而bytes类型不支持修改
print(b1.decode()) # 生命苦短
print(','.join(str1)) # 人,生,苦,短
s = ';'
print(s.join(str1)) # '人;生;苦;短'
a1 = bytes('中国',encoding = 'utf-8')
print(a1) # b'\xe4\xb8\xad\xe5\x9b\xbd'
print(a1.decode()) #'中国'
print(u'书写national word') # 书写national word 
# #Unicode是书写国际文本的标准方法。如果想要用母语写文本，那么需要一个支持Unicode的编辑器.
print(2 << 2==8) # 将2往左移动两位,即200(二进制)转为10进制既是8
print(3 << 2==12)# 3*2^2 = 12 
print(10 << 2==40) # 即10*4
print(10 >> 2 == 2) # 即10/4取整
print(11 >> 2 == 2) # 即11/4取整
print(5 & 3) # 1
print(5 & 7) # 数字的按位与
print(8 | 2) # 数字的按位或
print(0.2+0.1==0.3) # False
print(3 > 2 and 3 > 1) # True
print(3 > 2 & 3> 8) #False
print(0 & 7) # 0
print(~2) # 按位反转
x = 100
print(~x) # -101
print(5 ^ 2) # 数字的按位XOR 7
print(5 ^ 3) # 6
print(14//3) # 4
print(14/3) # 4.666666666666667
print(14%3) # 2
print(8%2) # 0
print(bool) # <class 'bool'>
print(bool(False)) # False
print(bool(0)) # False
print(bool(-23)) # True
print(bool(None)) # False
print(bool([])) # False
print(bool([23])) # True
a = 1+2j
print(a.real,a.imag) # 1.0 2.0
print(type(a)) # <class 'complex'>
print(f'I am {a} years old') # I am (1+2j) years old
x = '     a   s  fdf  '
x.replace(' ','')
print(x) # 'asfdf'
print('{:->8,}'.format(12345))  # 逗号为千位符 --12,345
print('{0:.3f}'.format(1.0/3)) # 0.333
print("{:_^30x}".format(16)) # ______________10______________
print('{0:\"^11}'.format('hello')) # \ 为字母小写 """hello"""
print('{0} love {1}.{2}'.format('i','fishc','com')) # i love fishc.com
print('{a} love {b}.{c}'.format(a='i',b='fishc',c='com')) # i love fishc.com
print('{0} love {b}.{c}'.format('i',b='fishc',c='com')) # i love fishc.com
print('{0}'.format('hhh')) # hhh
print('{{0}}'.format('hhh')) # {0}
print('{0:1f}{1}'.format(17.77,'gb')) # 17.770000gb
print('%c %c %c'%(97,98,99)) # a b c
print('%s'%'i love you') # i love you
print('%d + %d = %d'% (4,5,4+5)) # 4 + 5 = 9
print('divmod(8,5) = 8//5,8%5', divmod(8, 5)) # divmod(8,5) = 8//5,8%5 (1, 3)
print('pow(2,3)=2^3={0:*^5d} and pow(2,3,8)=2^3//8={1:*<5d}'.format(pow(2, 3),pow(2, 3, 4))) # pow(2,3)=2^3=**8** and pow(2,3,8)=2^3//8=0****
print('(round(3.5)){0:.2f} is 2 times of (round(2.5){1:.2f}'.format(round(3.5), round(2.5))) # (round(3.5))4.00 is 2 times of (round(2.5)2.00
print('round(4.444,2)={0}'.format(round(4.444, 2))) # round(4.444,2)=4.44
print('{0:c} is {1}'.format(97, chr(ord('a')))) # a is a
print('abs(-2) = ', abs(-2)) # abs(-2) =  2
print(all([2 > 1, -1 > -2])) # True
print(any((2, -1 < -2))) # True
a, b, c = oct(8), hex(16), bin(2)
print('{0}={1:o} and {2}={3:x} and {4:b}={5}'.format(a, 8, b, 16, 2, c)) # 0o10=10 and 0x10=10 and 10=0b10
print('0b1010=', 0b1010) # 0b1010= 10
print(f'0o10={a}=oct(8)') # 0o10=0o10=oct(8)
print(f'0x10={b}=hex(16)') # 0x10=0x10=hex(16)
print(f'0b10={c}=bin(2)') # 0b10=0b10=bin(2)
print('test'.center(20, '=')) # ========test========
print('test'.lower()) # test
print('test'.upper()) # TEST
print('test'.strip('t')) # es
print(chr(12288).join('test')) # t　e　s　t
a = u'iloveu' # python2中遍历字符串需要前加u
print([i for i in a]) # ['i', 'l', 'o', 'v', 'e', 'u']
print('test'.find('t', 2)) # 3
```
* 集合类型 (集合) 元素之间无序，相同元素在集合中唯一存在,集合中元素不可重复,元素类型只能是固定数据类型，例如：整数、浮点数等，列表、字典和集合类型本身都是可变数据类型，不能作为集合的元素出现。
* 映射类型 (字典) 每个元素是一个键 值对，表示为(key, value)
* 序列类型 (列表 元组 字符串) 是一维元素向量 元素之间存在先后关系，通过序号访问，元素之间不排他
```python
# 集合 元组 列表 字典都可以用变量名加([])来创建
a = list(['i','love','you'])
print(a[::-1])
print(a.index('i'),a.count('love')) # 0 1
print(';'.join(a)) # 'i;love;you'
for temp in a
   print(temp) # i love you
for index,name in enumerate(a): # 拆包
   print(index,name)  # 0 i   1 love   2 you
user_name,user_age,user_birthday = a
print(user_name) # 'i'

print([(x,y) for x in [1,2] for y in [2,3]]) # [(1, 2), (1, 3), (2, 2), (2, 3)]
print([x + 1 for x in [x**2 for x in [1,2,3]]]) # [2, 5, 10]
print([(x,y) for (x,y) in zip([1,2,3],[3,1,2])]) # [(1, 3), (2, 1), (3, 2)]
l = ['hello','world',18,'apple',None]
print([s.lower() for s in l if isinstance(s,str)]) # ['hello', 'world', 'apple']
g = (s.lower() for s in l if isinstance(s,str)) #把列表生成器的方括号换成圆括号就是生成器generator
print(type(g)) # <generator object <genexpr> at 0x0000018EDF0BC948>
#生成器用next()调用，一次只调用一个，调用完元素就会报错
print(next(g)) # 'hello'
for i in g: # 因此一般用遍历来访问元素，此法不用管是否报错
    print(i)
    
# b = a[0:2] # 切片
b = a[:]  # 浅拷贝 会复制一份，使地址发生变化
d = a.copy() # 浅拷贝
c = a # 仅仅是拷贝了地址，类似于贴了1个标签
import copy
a = [11,22]
b = [22,33]
c = [a,b]
id(c) # 140300149367560
d = copy.copy(c) # 浅拷贝可变类型比如列表时，地址会变，若是拷贝不可变类型比如元组，则地址不变，仅仅是多贴了1个标签(指向)
id(d) # 140300149370696
id(c[0]) # 140300149399496 但内部的引用不会变
id(d[0]) # 140300149399496 地址一样
e = copy.deepcopy(c)# 深拷贝可变类型时地址会变，拷元组时，若元组里面只有基本的数据，则是指向，地址不变，若元组里面有引用其他可变数据比如列表，则依然会将内部引用拷1份，造成地址改变
#深拷贝一般用于对比较重要的数据进行实验，不修改源数据，而是用备份
id(e) # 140300149370824
id(e[0]) # 140300149369224内部的引用会变,即将内部列表一并拷了1份
b.append('you')
print(b[0:2:2]) # ['i']
d.remove('i')
print(d.reverse()) # None
print(sorted(d)) # ['love']
c.clear()
print(a) # []

```

```python
# 在没用字典的情况下 用列表代替
brand = ['li','nai','a','lang'] # 键key
slogan = ['any','just','impossible','program'] # 值value
print('lang的口号是:',slogan[brand.index('lang')]) # lang的口号是: program

# dict0 = dict([('f', 70), ('i', 105)])  #每一个键值组合称为项
# dict0 = dict((('f', 70), ('i', 105))) # 也可以用dict字符加两个小括号创建
dict0 = dict(f=70, i=105)  # 用关键字参数时,键不用引号,值随数据类型的格式写
dict2 = {1:'one',2:'two',3:'three'}   #字典不是数据类型 是映射类型 可以直接用大括号创建
dict0['a'] = 65  #在没规定字典的键的时候直接赋值会出错 此处直接赋值不会引起错误
print(dict0) # {'f': 70, 'i': 105, 'a': 65}
dict1 = {}.fromkeys(range(32), 'an') # 也可以只传入一个元组作为键 没有对应值
print(23 in dict1) # True 默认只查找键
print('an' in dict1) # False
print({}.fromkeys((1,2,3),('one','two','three'))) # {1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}
print({}.fromkeys((1,2,3))) # {1: None, 2: None, 3: None}
print(dict1.keys()) # 返回所有的键信息 dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
print(dict1.values()) # 返回所有的值信息 dict_values(['an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an', 'an'])
print(dict1.items()) # 返回所有的键值对 dict_items([(0, 'an'), (1, 'an'), (2, 'an'), (3, 'an'), (4, 'an'), (5, 'an'), (6, 'an'), (7, 'an'), (8, 'an'), (9, 'an'), (10, 'an'), (11, 'an'), (12, 'an'), (13, 'an'), (14, 'an'), (15, 'an'), (16, 'an'), (17, 'an'), (18, 'an'), (19, 'an'), (20, 'an'), (21, 'an'), (22, 'an'), (23, 'an'), (24, 'an'), (25, 'an'), (26, 'an'), (27, 'an'), (28, 'an'), (29, 'an'), (30, 'an'), (31, 'an')])
print(dict1.get('a', 'None')) # None 键存在则返回相应值，否则返回默认值 不会改变原字典
print(dict1.pop('b', 'None')) # None 键存在则返回相应值，同时删除键值对，否则返回默认值 
print(dict1.popitem()) # (31, 'an') 随机从字典中随机取出一个键值对，以元组(key, value)形式返回 
print(dict1) # {0: 'an', 1: 'an', 2: 'an', 3: 'an', 4: 'an', 5: 'an', 6: 'an', 7: 'an', 8: 'an', 9: 'an', 10: 'an', 11: 'an', 12: 'an', 13: 'an', 14: 'an', 15: 'an', 16: 'an', 17: 'an', 18: 'an', 19: 'an', 20: 'an', 21: 'an', 22: 'an', 23: 'an', 24: 'an', 25: 'an', 26: 'an', 27: 'an', 28: 'an', 29: 'an', 30: 'an'}
dict3 = dict1 # 直接赋值会受原字典改变的影响 因为不会改变id地址
dict3 = dict1.copy() # 浅拷贝会改变id地址,原字典的键的改变并不影响dict3，但原字典内部键对应的值的改变会影响
dict1.clear() # 删除所有的键值对 改变其中之一只会影响地址相同的
print(dict1,'====>',dict3) # {} ====> {0: 'an', 1: 'an', 2: 'an', 3: 'an', 4: 'an', 5: 'an', 6: 'an', 7: 'an', 8: 'an', 9: 'an', 10: 'an', 11: 'an', 12: 'an', 13: 'an', 14: 'an', 15: 'an', 16: 'an', 17: 'an', 18: 'an', 19: 'an', 20: 'an', 21: 'an', 22: 'an', 23: 'an', 24: 'an', 25: 'an', 26: 'an', 27: 'an', 28: 'an', 29: 'an', 30: 'an'}
dict2 = {}.fromkeys(('a','b','c'),('65','66','67'))
print(dict2,dict2['b']) # 字典中没有的键 直接访问会报错 {'a': ('65', '66', '67'), 'b': ('65', '66', '67'), 'c': ('65', '66', '67')} ('65', '66', '67')
dict2.setdefault('d','68') # 随机放进去 字典中没有特殊的顺序
dict2.update(dict0) # 随机更新
print(dict2) # {'a': 65, 'b': ('65', '66', '67'), 'c': ('65', '66', '67'), 'd': '68', 'f': 70, 'i': 105}

```
```python
num = {}
print(type(num)) # <class 'dict'>
num2 = {1,3}
print(type(num2)) # <class 'set'>如果只有值 则被当成了集合
set1 = {1, 2, 2, 3, (3, 4), 'a'} #集合中的特性是唯一，会将重复的值去掉 可以利用该特性整理重复值 但得到的集合是无序的
temp = []
for a in set1: # 将列表中的重复的值去掉 以前的方法是用for循环
    if a not in temp:
        temp.append(a)
set2 = {2, 3, 4}
print(2 in set1) # True
print(set1[0]) # 集合不可以访问单一的值 会报错
set1.add(4)  # 如果数据项x不在集合S中，将x增加到s
set1.remove(4)  # 如果4在集合Set1中，移除该元素；不在则产生 KeyError异常
print(set1 - set2)  # 差集 {1, (3, 4), 'a'}
print(set1 & set2)  # 交集 {2, 3}
print(set1 | set2)  # 并集 {1, 2, 3, 4, 'a', (3, 4)}
print(set1 ^ set2)  # 补集 {1, 4, 'a', (3, 4)}
set1.clear()  # 移除Set1中所有数据项
num3 = frozenset([1, 2, 3, 4, 5, 5])  # 可用来创建不可变集合
# num3.add(3) # AttributeError: 'frozenset' object has no attribute 'add'

exec('a = 100') # 等同于输入a=100

tuple1 = tuple([1, 2, 3])
type((2))  # int
type((2,))  # tuple
# 序列的方法：min max len index count
```
## 函数
```python
def myfirstfunction(name):
    '''函数定义过程中的name叫形参
    因为这是一个形式，表示占据一个参数位置'''
    print('传递进来的'+name+'叫做实参，因为这是具体的参数值')

myfirstfunction('me') # 传递进来的me叫做实参，因为这是具体的参数值
print(myfirstfunction.__doc__) # 函数定义过程中的name叫形参\\n\     因为这是一个形式，表示占据一个参数位置
print(print.__doc__) 
```
### 传递(调用)参数的方法有两种,下面这个是位置参数,即按照默认位置来调用
```python
def saysome(name,words):
    print(name+'->'+words)

saysome('i','love you') # i->love you
saysome('love you','i') # love you->i
saysome(words='love you',name='i')    # 其中name,words为关键字参数,即给定一个值
# i->love you
```
### 下面的name,words为默认参数,i,love you为默认值
### 定义默认参数要牢记一点：默认参数必须指向不变对象
```python
def saysome(name='i',words='love you'):    
    print(name+'->'+words)

saysome() # i->love you
saysome('me') # me->love you
saysome('she','love me') # she->love me
```
### python默认会将`*`后面全当做收集参数
```python
def test(*params,exp):   
    print('参数的长度是:',len(params),'第二个参数是:',params[1])
    
test(1,'小和尚',3.14,5,6,7,8) # Traceback报错
```
### 解决方法为用关键字指定
```python
test(1,'小和尚',3.14,5,6,7,8,exp=8) # 参数的长度是: 7 第二个参数是: 小和尚
```
### 或者将形式参数放在前面
```python
def test(exp,*params):     
    print('参数的长度是:',len(params),'第二个参数是:',params[1])

test(1,'小和尚',3.14,5,6,7,8)  # 参数的长度是: 6 第二个参数是: 3.14
```
```python

```
### 多值不定长参数 
```python
def test(c,d,*args,**kwargs): 
'''*告诉编译器在传入参数时，多传的通通给*args以元组身份保存,**用来接收多传的关键字参数作为字典'''
    print(c,d)
    print(args)
    print('{0:=>20}'.format('*'))
    print(kwargs)

test(1,2,(1,2,3,4),{'a':1,'b':2}) 
```
```python
1 2
((1,2,3,4),{'a':1,'b':2}) # 将后面都当成元组的元素传入
===================*
{}
```
### 需进行拆包
```python
test(1,2,*(1,2,3,4),**{'a':1,'b':2}) 
```
```
1 2
(1, 2, 3, 4)
===================*
{'a': 1, 'b': 2}
```
```python
def hello():
    print('hello fishc!')
    
temp = hello()
hello()
print(temp) # None
type(temp) # <class 'NoneType'>
```
```python
def back():
    return [1,'i',3.14]

back() # [1, 'i', 3.14]

def back():
    return 1,'i',3.14

back() # (1, 'i', 3.14)
```
### 函数定义过程中的局部变量出了函数定义过程就不可使用，而函数定义过程外的变量为全局变量
### 在函数里面可以访问全局变量但不可以修改
```python
count = 5 # 全局变量
def myfun():
    count = 10
    print(10)
    
print(count) # 5
```
### 如果一定要改全局变量则用`global`关键字
```python
def myfun():
    global count
    count = 10
    print(10)
    
myfun() # 10
print(count) # 10
```
```python
def fun1():
    print('fun1()正在被调用...')
    def fun2():
        print('fun2()正在被调用...')
    fun2()

    
fun1()
```
```
fun1()正在被调用...
fun2()正在被调用...
```
```python
fun2()
```
```python
Traceback (most recent call last):
  File \"<pyshell#37>\", line 1, in <module>#内嵌函数出了定义的函数之后就不能被调用了
    fun2()
NameError: name 'fun2' is not defined
```
### 在内部函数`funy()`里，引用外部作用域的变量`x`,则称`funy()`为闭包
```python
def funx(x):
    def funy(y):
        return x*y  
    return funy

funx(1)(3) # 3
i = funx(8)
type(i) # <class 'function'>
```
### 闭包里面不可以用外部作用域的变量去赋值同样的变量名
```python
def fun1():
    x = 5
    def fun2():
        x*=x
        return x  
    return fun2()

fun1() # Traceback报错
```
### 但是可以直接赋值新的值
```python
def abc():
    x = 1
    def bcd():
        x = 2
        return x 
    return bcd()

abc() # 2
```
### 可以用global关键字改变
```python
def fun1():
    x = 5
    def fun2():
        global x   
        x = 1
        return x
    return fun2()
    
fun1() # 1
```
### 也可以将变量改为元组
```python
def fun1():
    x = [5]
    def fun2():
        x[0] *= x[0]   
        return x[0]
    return fun2()

fun1() # 25
```
### 也可以运用nonlocal关键字
```python
def fun1():
    x = 5
    def fun2():
        nonlocal x   
        x *=x
        return x
    return fun2()

fun1() # 25

lambda x :2*x+1
<function <lambda> at 0x000001F7A96F2438>#lambda表达式可以简化函数定义过程
g = lambda x :2*x+1
g(5) # 11
h = lambda x: x%2
list(filter(h,range(1,10))) # filter可以通过函数筛选可迭代区间中的值，默认筛选正数
[1, 3, 5, 7, 9]
list(filter(None,[0,False,True])) # [True]
list(filter(None,[0,1])) # [1]
list(map(lambda x:x*2,range(10))) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# map可以将范围中的值带入函数中再返回值

def creatfile(name,content,censored_word='hello',changed_word='goodbye'):
    name = 'D:\\Users\\向致承\\Documents\\python\\'+name
    content = str(content.replace(censored_word,changed_word))           
    f = open(name,'w')
    f.write(content)
    print('done')
creatfile('new2','hello word') # goodbye world \n done
```
```python
def discounts(price,rate):                                        
    final_price = price*rate                                        
    global old_price # 若是要修改不可变类型的全局变量比如字符串则用global，若是要修改可变类型比如列表则不用global可以直接修改成功                                        
    print('这里试图打印全局变量',old_price)                                        
    old_price= 80                                        
    print('修改后的值为1',old_price)                                        
    return final_price                                        
                                        
old_price = float(input('请输入原价：'))                                        
rate = float(input('请输入折扣率:'))                                        
new_price = discounts(old_price,rate)                                        
print('修改后的值是2',old_price)                                        
print('打折后的价格是:',new_price)                                        
print('这里试图打印局部变量',final_price)                    
```
```
请输入原价：1000                                        
请输入折扣率:0.88                                        
这里试图打印全局变量 1000.0                                        
修改后的值为1 80                                        
修改后的值是2 80                                        
打折后的价格是: 880.0   
```
```python
import sys    
sys.setrecursionlimit(100)#不可以轻易使用递归，要限制位数之后再使用    
def recursion():    
    return recursion()    
def fab(n):    
    if n == 0 or n==1:    
        return 1    
    else:    
        return n*fab(n-1)#求阶乘可用递归    
def fab(n):    
    i = 1    
    x = 1    
    while i!=n:#也可用while循环    
        i += 1    
        x = x*i    
    return x    
def fab(n):    
    result = n    
    for i in range(1,n):#也可用for循环    
        result *= i    
    return result    
fab(5)    
def hanoi(n,x,y,z):    
    if n == 1:    
        print(x,'-->',z)       
    else:    
        hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上 中间的z是借助针 xy分别为初始针和目的针    
        print(x,'-->',z)#将最底下的最后一个盘子从x移动到z上    
        hanoi(n-1,y,x,z)#将y上的n-1个移动到z上 x是借助针    
    
hanoi(3,'x','y','z')    
    
def fib(n):    #用迭代算斐波那契    
    n1 = 1    
    n2 = 1    
    n3 = 1    
    if n == 2 or n == 1:    
        return 1    
    while (n-2)>0:    
        n3 = n2 + n1    
        n1 = n2    
        n2 = n3    
        n = n-1    
    return n3    
    
def fib(n):    
    if n == 1 or n == 2:    
        return 1    
    else:    
        return fib(n-1)+fib(n-2)    
fib(8)    
    
def fib(max):     
   n, a, b = 0, 0, 1     
   L = []     
   while n < max:     
       L.append(b)     
       a, b = b, a + b     
       n = n + 1     
   return L    
    
f = iter(fib(10))    
while True:    
    try:    
        print (next(f), end=" ")    
    except StopIteration:    
        sys.stderr.write('Warning, log file not found starting a new one\\n')    
        sys.exit()
```
```
x --> z  
x --> y  
z --> y  
x --> z  
y --> x  
y --> z  
x --> z  
1 1 2 3 5 8 13 21 34 55 
Warning, log file not found starting a new one

D:\\anaconda\\lib\\site-packages\\IPython\\core\\interactiveshell.py:2969: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D. 
  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)
```
## 面向对象编程(OOP(object oriented programming))
* 1. 面向过程类似于函数,但过程只负责执行而没有返回值,函数既能执行又可以返回结果
> + 在面向过程开发时,侧重于怎么做,逐步实现并将功能独立的代码封装为函数,最后完成就是调用不同的函数,开发过程中没有固定套路,难度很大
* 2. 对象=属性+方法，静态的为属性，动态的动作为方法，即一个固定的套路，适合复杂的开发项目
> + OOP侧重于谁来做,首先需要考虑方法,然后考虑用合适的对象封装方法,最后不同的对象实现不同的方法
* 3. OOP相比于面向过程是一个更大的封装，封装是为了数据的隐蔽性，继承是为了子类调用父类的属性或方法更方便，多态是不同类的同一方法可以不一样
* 4. 类名使用大驼峰命名法,即每个单词首字母大写且不用下划线隔开
* 5. 类的设计前要需求分析,名词提炼法将某个业务流程中的名词设为类名,这个名词的特征描述就是属性,该名词的行为(动词)就是方法
> + OOP中引用的概念同样适用,变量名引用了新建的实例对象,并且默认情况下`print`输出对象变量时会输出该变量引用的对象是由哪个类创建的对象,以及内存中的地址(16进制)
* 6. 使用`类名()`创建实例对象时,会自动先为对象在内存中分配空间,然后初始化
* 7. python中一切皆对象,类是一个特殊的对象,用`class`定义称为类对象,,`类名()`创建的为实例对象
> + 类对象在内存中只有一份,一个类可以创建多个实例对象
* 基本方法
* `__del__(self)`析构器，当一个实例被销毁的时候调用的方法
* `__call__(self[, args...])`允许一个类的实例像函数一样被调用：x(a, b) 调用 x.__call__(a, b)
* `__len__(self)`定义当被 len() 调用时的行为
* `__repr__(self)`定义当被 repr() 调用时的行为
* `__str__(self)`定义当被 str() 调用时的行为
* `__bytes__(self)`定义当被 bytes() 调用时的行为
* `__hash__(self)`定义当被 hash() 调用时的行为
* `__bool__(self)`定义当被 bool() 调用时的行为，应该返回 True 或 False
* `__format__(self, format_spec)`定义当被 format() 调用时的行为

* 有关属性
* `__getattr__(self, name)`	定义当用户试图获取一个不存在的属性时的行为
* `__getattribute__(self, name)`	定义当该类的属性被访问时的行为
* `__setattr__(self, name, value)`	定义当一个属性被设置时的行为
* `__delattr__(self, name)`	定义当一个属性被删除时的行为
* `__dir__(self)`	定义当 dir() 被调用时的行为
* `__get__(self, instance, owner)`	定义当描述符的值被取得时的行为
* `__set__(self, instance, value)`	定义当描述符的值被改变时的行为
* `__delete__(self, instance)`	定义当描述符的值被删除时的行为

* 比较操作符
* `__lt__(self, other)`	定义小于号的行为：x < y 调用 x.__lt__(y)
* `__le__(self, other)`	定义小于等于号的行为：x <= y 调用 x.__le__(y)
* `__eq__(self, other)` 定义等于号的行为：x == y 调用 x.__eq__(y)
* `__ne__(self, other)`	定义不等号的行为：x != y 调用 x.__ne__(y)
* `__gt__(self, other)`	定义大于号的行为：x > y 调用 x.__gt__(y)
* `__ge__(self, other)`	定义大于等于号的行为：x >= y 调用 x.__ge__(y)

* 算数运算符
* `__add__(self, other)`	定义加法的行为：+
* `__sub__(self, other)`	定义减法的行为：-
* `__mul__(self, other)`	定义乘法的行为：*
* `__truediv__(self, other)`	定义真除法的行为：/
* `__floordiv__(self, other)`	定义整数除法的行为：//
* `__mod__(self, other)`	定义取模算法的行为：%
* `__divmod__(self, other)`	定义当被 divmod() 调用时的行为
* `__pow__(self, other[, modulo])` 	定义当被 power() 调用或 ** 运算时的行为
* `__lshift__(self, other)`	定义按位左移位的行为：<<
* `__rshift__(self, other)`	定义按位右移位的行为：>>
* `__and__(self, other)`	定义按位与操作的行为：&
* `__xor__(self, other)`	定义按位异或操作的行为：^
* `__or__(self, other)`		定义按位或操作的行为：| 
 
* 反运算
* `__radd__(self, other)`	（与上方相同，当左操作数不支持相应的操作时被调用）
* `__rsub__(self, other)`	（与上方相同，当左操作数不支持相应的操作时被调用）
* `__rmul__(self, other)`	（与上方相同，当左操作数不支持相应的操作时被调用）
* `__rtruediv__(self, other)`	（与上方相同，当左操作数不支持相应的操作时被调用）
* `__rfloordiv__(self, other)`	（与上方相同，当左操作数不支持相应的操作时被调用）
* `__rmod__(self, other)`	（与上方相同，当左操作数不支持相应的操作时被调用）
* `__rdivmod__(self, other)`	（与上方相同，当左操作数不支持相应的操作时被调用）
* `__rpow__(self, other)`	（与上方相同，当左操作数不支持相应的操作时被调用）
* `__rlshift__(self, other)`	（与上方相同，当左操作数不支持相应的操作时被调用）
* `__rrshift__(self, other)`	（与上方相同，当左操作数不支持相应的操作时被调用）
* `__rand__(self, other)`	（与上方相同，当左操作数不支持相应的操作时被调用）
* `__rxor__(self, other)`	（与上方相同，当左操作数不支持相应的操作时被调用）
* `__ror__(self, other)`	（与上方相同，当左操作数不支持相应的操作时被调用）

* 增量赋值运算
* `__iadd__(self, other)`	定义赋值加法的行为：+=
* `__isub__(self, other)`	定义赋值减法的行为：-=
* `__imul__(self, other)`	定义赋值乘法的行为：*=
* `__itruediv__(self, other)`	定义赋值真除法的行为：/=
* `__ifloordiv__(self, other)`	定义赋值整数除法的行为：//=
* `__imod__(self, other)`	定义赋值取模算法的行为：%=
* `__ipow__(self, other[, modulo])`	定义赋值幂运算的行为：**=
* `__ilshift__(self, other)`	定义赋值按位左移位的行为：<<=
* `__irshift__(self, other)`	定义赋值按位右移位的行为：>>=
* `__iand__(self, other)`	定义赋值按位与操作的行为：&=
* `__ixor__(self, other)`	定义赋值按位异或操作的行为：^=
* `__ior__(self, other)`		定义赋值按位或操作的行为：|=

* 一元操作符
* `__pos__(self)`	定义正号的行为：+x
* `__neg__(self)`	定义负号的行为：-x
* `__abs__(self)`	定义当被 abs() 调用时的行为
* `__invert__(self)`	定义按位求反的行为：~x

* 类型转换
* `__complex__(self)`	定义当被 complex() 调用时的行为（需要返回恰当的值）
* `__int__(self)`	定义当被 int() 调用时的行为（需要返回恰当的值）
* `__float__(self)`	定义当被 float() 调用时的行为（需要返回恰当的值）
* `__round__(self[, n])`	定义当被 round() 调用时的行为（需要返回恰当的值）
* `__index__(self)`	
> * 1. 当对象是被应用在切片表达式中时，实现整形强制转换
> * 2. 如果你定义了一个可能在切片时用到的定制的数值型,你应该定义 __index__
> * 3. 如果 __index__ 被定义，则 __int__ 也需要被定义，且返回相同的值

* 上下文管理（with 语句）
* `__enter__(self)`定义当使用 `with` 语句时的初始化行为
> + `__enter__` 的返回值被 with 语句的目标或者 as 后的名字绑定
* `__exit__(self, exc_type, exc_value, traceback)`定义当一个代码块被执行或者终止后上下文管理器应该做什么
> + 一般被用来处理异常，清除工作或者做一些代码块执行完毕之后的日常工作

* 容器类型
* `__len__(self)`	定义当被 len() 调用时的行为（返回容器中元素的个数）
* `__getitem__(self, key)`	定义获取容器中指定元素的行为，相当于 self[key]
* `__setitem__(self, key, value)`	定义设置容器中指定元素的行为，相当于 self[key] = value
* `__delitem__(self, key)`	定义删除容器中指定元素的行为，相当于 del self[key]
* `__iter__(self)`	定义当迭代容器中的元素的行为
* `__reversed__(self)`	定义当被 reversed() 调用时的行为
* `__contains__(self, item)`	定义当使用成员测试运算符（in 或 not in）时的行为
```python
class MyTimer():   
    def __init__(self):
        self.uint = ['年','月','日','小时','分钟','秒']
        self.prompt = "未开始计时"
        self.lasted = []
        self.btime = 0
        self.etime = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self,other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.uint[index])
        return prompt
        # return int(self)+int(other)
    def __sub__(self,other):
        return int.__sub__(self,other)
    
    def start(self):
        self.btime = time.localtime()
        self.prompt = "请先调用stop()停止计时"
        print('开始计时')

    def stop(self):
        if not self.btime:
            print('请先调用start()进行计时')
        else:
            self.etime = time.localtime()
            self._calc()
            print('停止计时')

    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.etime[index] - self.btime[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index])+self.uint[index]
        self.btime = 0
        self.etime = 0


a = MyTimer()
b = MyTimer()
b.start()
a.start()
time.sleep(3)
a.stop()
b.stop()
print(a)
print(b)
print(a + b)
```
```python
class Rectangle:
    def __init__(self,width=0,height=0):
        self.width = width # 赋值操作会自动触动setattr
        self.height = height
    def __setattr__(self,name,value):
        if name == "square":
            self.width = value
            self.height = value
        else:
            # self.name = value # 再次触动setattr，一直死循环
            super().__setattr__(name,value) # self.__dict__[name] = value
    def getArea(self):
        return self.width * self.height

r1 = Rectangle()
r1.square = 10
print(r1.width,r1.height,r1.getArea())
```
* 描述符就是将某种特殊类型的类的实例指派给另一个类的属性,即property的原理
* 特殊类型即至少实现__get__ & __set__ & __delete__三个方法中的一个
```python
class MyProperty: 
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self,instance,owner):
        print("getting...",self,instance,owner)
        return self.fget(instance)

    def __set__(self,instance,value):
        print("setting...",self,instance,value)
        self.fset(instance,value)
    
    def __delete__(self,instance):
        print('deleting...',self,instance)
        self.fdel(instance)


class Test:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self,value):
        self._x = value

    def delX(self):
        del self._x

    def __getattribute__(self,name):
        print("getattribute of Test")
        return super().__getattribute__(name)
    def __getattr__(self,name):
        print("getattr of Test")
    def __setattr__(self,name,value):
        print("setattr of Test")
        super().__setattr__(name,value)
    def __delattr__(self,name):
        print("delattr of Test")
        super().__delattr__(name)
    y = MyProperty(getX,setX,delX) # MyProperty是y的描述符



test = Test()
print(test.x) # 先访问getattribute,如果没有属性就访问getattr
test.x = "x-man" # 调用__setattr__
print(test.x) 
del test.x # 调用__delattr__
print('下示访问修改描述符的属性'.center(20,'*'))
print(test.y) # 先访问getattribute,如果没有属性就访问getattr,最后调用描述符类的__get__
test.y = "Y-man" # 先调用__setattr__,再调用描述符类的__set__
print(test._x)
del test.y # 先调用__delattr__,再调用描述符类的__delete__
```
```python
class Celsius:    
    def __init__(self,value = 26.0):
        self.value = float(value)

    def __get__(self,instance,owner):
        return self.value

    def __set__(self,instance,value):
        self.value = float(value)
    

class Fahrenheit:
    def __get__(self,instance,owner):
        return instance.cel * 1.8 + 32

    def __set__(self,instance,value):
        instance.cel = (float(value) - 32)/1.8  

class Temperature:
    cel = Celsius()
    fah = Fahrenheit()

test = Temperature()
print(test.cel)
test.cel = 38 
print(test.fah)
test.fah = 78
print(test.cel) 
```
* 协议protocols与其他语言中的接口很相似,规定哪些方法必须定义
* 在python中的协议不是很正式,更像一种指南
* 容器类型的协议有两种
* 若定制的容器不可变,只需定义__len__() & __getitem__()
* 若容器可变,需定义__len__() & __getitem__() & __setitem__() & __delitem__()
```python
class CountList:
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self,key): # 每次访问元素都会调用的方法
        self.count[key] += 1 # 每访问一次增加一次
        return self.values[key]

c1 = CountList(1,3,5,7,9)
c2 = CountList(2,4,6,8,10)
print(c1.count)
print(c1[1]+c2[2])
print(c1.count)
```
```python
import random
class Person(object):    
    population = 0 # population是类属性,下面的name是实例属性
    name_list = []
    def __init__(self,name,age,salary):   # 利用init方法时,第一个参数始终是self,相当于C++的this指针
        """初始化的过程是,先调用__new__为实例分配空间,然后返回实例引用
        然后才调用__init__实例初始化,定义实例属性
        实例化几次实例就会执行几次初始化
        父类的魔法方法会被继承,最好不要自创魔法方法"""
        print('Initializing'+str(self)) # 查看实例名\类名\分配存储空间的地址
        self.__name = name 
        Person.name_list.append(self.__name)
        self.__age = age # 在__init__方法内部,可以把各种属性绑定到self,因为self就指向创建的实例本身
        self.__salary = salary # __ 开头即类的内置属性或方法，只能在实例方法内访问
        self.x = random.randint(1,10) 
        self.y = random.randint(1,10)    
        self.sum_ = self.x + self.y # 单后置 _ 用于避免与关键字冲突
        self._z = pow((self.x+self.y),2) # 单前置 _ 为私有化属性或方法,导入模块时并不会导入,通常用于避免模块之间全局变量的冲突
        self.__class__.population += 1 # 因为每个实例都通过__class__属性引用其类中的方法和属性
        # Person.population += 1 # 也可用此句代替

    def __greet(self): # 私有方法
        """Greeting by the robot.Yeah, they can do that."""

    def gps(self):    
        print('GPS is ',self.x,self.y)    

    def move_to_east(self):    
        self.x -= 1    
        print('移后的位置是',self.x,self.y)             

    def get_info(self):
        """子类想调用父类的私有属性或私有方法只能通过父类的公有方法"""
        self.__greet()
        print("Greetings,my name is {0} and {1}-year-old with {2} money.".format(self.__name,self.__age,self.__salary))

    def __del__(self): # 析构函数在该实例被从内存中销毁之前自动调用  
        """I am dying."""
        print('{} is being destroyed'.format(self.__name))
        if Person.population == 0:
            print("{} was the last one,no Person alive!.".format(self.__name))
            return # 后面不加返回值则是终止不再执行之后的代码
        Person.population -= 1
        Person.name_list.remove(self.__name)

    @staticmethod # 不访问类/实例的属性/方法,则使用静态方法
    def run(): # 通过类名.静态方法---不需要创建实例对象
        print("i'm running")

    @classmethod # 意思同 count_Person = classmethod(count_Person) 标记为类方法 只访问类属性
    def count_Person(cls): # 用cls代替类名访问类属性,而不是self 
        """Prints the current population."""
        print('There are',cls.population,'persons alived\
                They are ',cls.name_list)
    
A = Person('Adom',23,2000) # A是一个全局变量,__del__方法会在所有代码执行完后调用
print('{:x}'.format(id(A))) # 查看地址
print(Person.__doc__) # 查看类对象的简介
B = Person('Nady',24,4000)
print(A is B) # 身份运算符is判断二者id是否一致 
# == 用于判断两个变量的值是否相等    
# is 用于判断两个变量引用变量是否为同一个    
# 与None进行比较时，最好使用is     
A.z = 10 # 加个属性,此为动态绑定
print(A._Person__age) # 在私有属性前加下划线类名可以访问私有属性，因为python的私有是伪私有
A._Person__greet() # 私有方法同理,此法不建议常用
Person.count_Person()
del A # 也可以主动提前调用
del B
```
* 定义的子类完全可以继承父类的所有属性和属性,私有属性(方法)除外,若需访问父类的私有属性,同样需用父类定义的方法从内部来调用
* 新定义的属性或方法会覆盖父类的同名属性或方法
```python
class Killer(Person): # 单继承
    population = 0
    def __init__(self,name,age,salary): # 若子类init方法与父类参数或属性不一致，仍会报错
        Person.__init__(self,name,age,salary) # 这里调用父类的init方法，只是继承父类的变量
        Killer.population += 1
        print('i am a killer')
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('i am hungry')
            self.hungry = False
        else:
            print('i am full')
    def get_info(self): # 不想覆盖父类的方法而只是扩展,则使用super类
        # super().get_info()
        # super类用于调用父类中封装的方法,不用传入父类的名字,自动查找父类
        Person.get_info(self) # 2.0版本前用父类名.方法(子类名)
        print('i am a Killer') # 之后可以扩写子类特有的代码
        # print(self.__age) # 在子类的方法中不能访问父类中的私有属性或私有方法

Killer_1 = Killer('haniba',33,1000)
Killer_1.population = 99 # 动态绑定实例对象属性并不会影响类属性,只会在实例对象内部添加该属性
# 向上查找机制会先从实例对象找属性,再从类中找,因此访问类属性最好用类名
print(Killer.population) 
# Killer_1.__secret() # 子类不可以访问父类的私有属性或私有方法
Killer_1.get_info() # 但是可以通过访问父类公有方法间接访问父类私有属性或私有方法
del Killer_1

class Programmer(Person):
    population = 0
    def __init__(self,name,age,salary):
        super().__init__(name,age,salary)
        Programmer.population += 1
        print("i'm a programmer")
    def get_info(self):
        """在不同的子类中重写父类方法之后的调用中就会引用新写的方法
        引用不变,方法在变,此为多态
        因为python中不允许出现同一变量名,后定义的变量名会覆盖前面的,此为重写
        而C中在定义函数时可以指定参数的类型，所以即使函数名不一样，调用的时候不会混合,这叫重载
        """
        super().get_info()
        print('i am a Programmer')
    def __str__(self): # 打印实例名时默认输出类名和该实例的地址，重定义之后可修改，但必须返回字符串    
        return 'this is a self-intro of a programmer'

mrx = Programmer('Mrx',20,8000)
mrx.get_info()
del mrx
programmer1 = Programmer('programmer1',30,3000)
programmer2 = Programmer('programmer2',40,4000)
programmer3 = Programmer('programmer3',50,5000)
programmer4 = Programmer('programmer4',60,6000)
print(Programmer.count_Person())
del programmer1
del programmer2
print(Programmer.count_Person())
del programmer3
del programmer4
```
* 若多个父类中存在多个同名的属性或方法时,应该尽量避免多继承,因为会重复调用父类的初始化方法
* 一般会先继承排在前面的类中的方法或属性,
* 新式类和经典类的搜索顺序不一样,新式类是以object为基类的类,推荐使用
* 在python3中无论是否继承object都会创建新式类,在python2中不指定继承则默认不继承object
* 因此定义类时,如果没有父类建议统一继承object,以防代码出错
```python
class WebProgrammer(Programmer,Killer): 
    population = 0
    def __init__(self,name,age,salary):
        super().__init__(name,age,salary) 
        # 直接写父类名.__init__ 就是调用指定父类 改用super调用就不一定调用继承的类 而是继承__mro__中的该类的后一个 
        # super(Killer,self).__init__(self,name,age,salary)
        # 指定Killer就会继承__mro__中Killer的后一个
        WebProgrammer.population += 1

	
mry = WebProgrammer('Mry',19,10000)
mry.get_info()
print(WebProgrammer.__mro__) # 使用super时,C3算法会在__mro__属性中查看方法的搜索顺序,调用webProgrammer的下一个
del mry 

```
* 横向的类可以用组合,属性名字与方法名相同,属性会覆盖方法 
* 应该运用继承与组合来扩展类，而不是定义很多方法 
```python
class Biology: 
    def __init__(self,name,age,salary): 
        self.Person = Person(name,age,salary) 
    def print_num(self): 
        print('there are {0} Persons'.format(self.Person.population)) 

    def play(self,other):
        print("I'm playing with..")
        other.get_info()

# 如果没有实例化就用类名调用方法，调用实例方法时会报错，需要传入一个实例名作为参数 
b = Biology('steve',23,1000) 
# Instan = Programmer('Instan',77,80000)
Instan = Killer('Instan',77,80000) # 相同的变量名但是类不一样
b.play(Instan) # 相同的方法传入的实例的类不一样,调用结果也不一样,此为多态
print(Biology.__dict__) # 类对象的方法是绑定在类上面的 
print(b.__dict__) # 实例对象的方法里面没有，但是可以调用 
b.x = 1 # 如果定义一个实例对象的特殊属性，该属性独属于该实例对象,并且不影响同名类属性
print(b.__dict__) 
print(Biology.__dict__) 
Biology.y = 1 # 如果给类对象定义特殊的属性，那么连同每一个实例对象都会有该属性 
print(b.__dict__)
Biology.__init__(b,'jobs',25,2000) # 因此想要更改单一实例的某个属性可以用类的__init__方法传入实例名，再改 
# 如果把类删除，实例对象调用的所有绑定在类上的方法依然不会失效 

```
* 设计模式是前人工作的总结和提炼，通常被人们广泛流传的设计模式是针对某一特定问题的成熟解决方案
* 使用设计模式是为了可重用代码、让代码更容易被他人理解、保证代码可靠性
* 单例设计模式的目的是让类创建的对象、在系统中只有唯一的一个实例
* 每一次执行实例化返回的对象内存地址完全相同，比如回收站、打印机、音乐播放软件
```python
class STR(str):
    instance = None
    init_flag = False # 标记初始化动作
    def __new__(cls,args): # 构造函数
        '''__new__主要用于继承一些不可变的类时,提供一些自定义实例化的途径,主要用于单例设计模式
        是一个静态方法,在调用时要主动传入cls参数,做两件事:1.自动为对象分配一个空间
        2.返回对象的引用,作为第一个参数传给__init__ '''
        newArgs = args.upper()
        if cls.instance is None:
            # cls.instance = str.__new__(cls,newArgs) 
            cls.instance = super().__new__(cls,newArgs) # 将给实例对象分配的空间固定在类属性
        return cls.instance # 返回固定的类属性实现单例
    def __init__(self,name): 
        if STR.init_flag: # 判断初始化动作标记
            return    # 控制只执行一次,若没有这两句则会初始化两次,self.name就会不一样
        self.name = name
        print('initing data of {}'.format(self.name))
        STR.init_flag = True   # 更改标记初始化动作
    def getName(self): 
        return self.name 
    def setName(self,value):
        self.name = value
    def delName(self):
        del self.name
    myname = property(getName,setName,delName) # property的作用是通过属性设置属性,来简化属性 
    # 三个参数分别是获取\改变\删除,对应属性的方法,将该属性的值赋值给新的属性 @property

str1 = STR('iloveu')
print(str1,id(str1))
str2 = STR('imissu')
print(str2,id(str2))
print(str1,id(str1)) # 不仅内容一样,且二者内存完全一样
print('STR是str的子类',issubclass(STR,str)) # 返回'cls'是派生自另一个类还是同一个类,自身可以是自身的子类
print('str1是STR的实例',isinstance(str1,STR)) # 如果是多继承第二个参数用元组,若第一个参数不是实例对象则永远返回False,若第二个参数不是类或元组则抛出Typeerror异常
print(hasattr(str1,'newattr')) # 判断是否有该属性 
print(getattr(str1,'newattr','你所访问的属性不存在')) # 访问对象的属性 不存在就返回给定值 
setattr(str1,'newattr','设置属性成功') # 给实例对象添加属性 
print(getattr(str1,'newattr','设置属性未成功')) 
delattr(str1,'newattr') # 删除存在的属性 如果不存在就返回异常 

print(str2.myname)
str2.myname = 'jackey'
print(str2.myname)
print(str2)
del str2.myname # 通过property可以简化属性的获取、更改、删除的过程
```
```python
class stock2(object):
    """stock2类中包含属性"""
    def __init__ (self,code,price):
        self.code = code
        self.price = price
    @classmethod
    def split(cls,stock):
        code = stock.split('-')[0]
        price = stock.split('-')[1]
        if len(price) == 6:
            return cls(code,price)
        print('主动抛出异常')
        raise Exception('股票代码有误')

s = stock2.split('中国平安-601318')
print(s.price,s.code)

```
```python
class Stack(object):    
    '''模拟实现栈'''
    def __init__(self,limit= 10):    
        self.stack = []    
        self.limit = limit    
    def push (self,data):    
        if len(self.stack) >= self.limit:    
            raise IndexError('超出栈容量的极限')    
        self.stack.append(data)    
    def pop(self):    
        if self.stack:    
            return self.stack.pop()    
        else:    
            raise IndexError('pop from an empty stack')    
    def bottom(self):    
        print(self.stack[0])    
    def isEmpty(self):    
        return not bool(len(self.stack))    
    def peek(self):    
        if self.stack:    
            return self.stack[-1]    
    def size(self):    
        return len(self.stack) 
stack_1 = Stack()
print(stack_1.limit)
stack_1.push(123)
print(stack_1.size())
print(stack_1.__dict__)

```
## python的异常处理可以自己捕捉，也可以自己定义
* 程序运行时,若解释器遇到一个错误,会停止程序的运行,并提示一些错误信息,这就是异常,程序停止执行并提示错误信息这个动作为抛出(raise)异常,并不是抛给用户而是抛给代码
* 很难面面俱到,通过异常捕获可以针对突发事件做集中处理,从而保证程序的稳定性和健壮性
```python
try:
	f = open('wenjian.txt')
except TypeError as reason:
	print('出错了，理由是'+str(reason))  # 如果错误类型没找到，还是会报错
except Exception as result:   # 因此可以利用Exception类捕获未知错误
	print('未知错误',str(result))
else:   
	print('尝试成功')    # try中的语句没有错误就会执行else中的语句
finally:
	print('无论是否出错都会执行')

```
* 异常的传递性--当函数/方法执行出错抛出异常，程序并不会终止，会将异常传递给函数/方法的调用方
* 如果传递到主程序，**仍然没有异常处理**，程序才会终止
* 利用异常的<u>传递性</u>,将捕获异常的代码放在主程序中
* 因为主程序中调用其他函数，只要出现异常就会传到主程序中
* 这样就不需要增加大量的异常捕获，能保证代码的灵活性
```python
def demo1():
    return int(input("输入整数："))

def demo2():
    return demo1()

try:
    print(demo2)   # 在主程序中捕获异常
except Exception as result:
    print('未知错误'+str(result))
```
* 有时程序运行没有错，但需要主动抛出异常，1.创建一个异常类,并定义错误信息\2.抛出该异常\3.主程序捕获错误信息
```python
def input_password():
    pwd = input('please input your password:')
    if len(pwd)>= 8:
        return pwd
    print('主动抛出异常')
    ex = Exception("密码长度不够!") # 先创建一个异常类，并增加错误信息
    raise ex # 抛出异常

try:
    print(input_password())
except Exception as result:
    print(result)
```
```python
class ShortInputException(Exception):  # 创建我们自己的异常类型
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
        
try:
        text = input('Enter something --> ')
        if len(text) < 3:
            raise ShortInputException(len(text), 3) # Other work can continue as usual here
except EOFError:
	print('Why did you do an EOF on me?')
except ShortInputException as ex:  # 错误类别ShortInputException存储在as变量名中
	print(('ShortInputException: The input was ' +
       		'{0} long, expected at least {1}').format(ex.length, ex.atleast))
else:  
	print('No exception was raised.')

```
### Python标准异常总结,由于异常的传递性,只在主程序捕获异常
* `AssertionError`断言语句（assert）失败
* `AttributeError`尝试访问未知的对象属性
* `EOFError`用户输入文件末尾标志EOF（Ctrl+d）
* `FloatingPointError`浮点计算错误
* `GeneratorExit`generator.close()方法被调用的时候
* `ImportError`导入模块失败的时候
* `IndexError`索引超出序列的范围
* `KeyError`字典中查找一个不存在的关键字
* `KeyboardInterrupt`用户输入中断键（Ctrl+c）
* `MemoryError`内存溢出（可通过删除对象释放内存）
* `NameError`尝试访问一个不存在的变量
* `NotImplementedError`尚未实现的方法
* `OSError`操作系统产生的异常（例如打开一个不存在的文件）
* `OverflowError`数值运算超出最大限制
* `ReferenceError`弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象
* `RuntimeError`一般的运行时错误
* `StopIteration`迭代器没有更多的值
* `SyntaxError`Python的语法错误
* `IndentationError`缩进错误
* `TabError`Tab和空格混合使用
* `SystemError`Python编译器系统错误
* `SystemExit`Python编译器进程被关闭
* `TypeError`不同类型间的无效操作
* `UnboundLocalError`访问一个未初始化的本地变量（NameError的子类）
* `UnicodeError`Unicode相关的错误（ValueError的子类）
* `UnicodeEncodeError`Unicode编码时的错误（UnicodeError的子类）
* `UnicodeDecodeError`Unicode解码时的错误（UnicodeError的子类）
* `UnicodeTranslateError`Unicode转换时的错误（UnicodeError的子类）
* `ValueError`传入无效的参数
* `ZeroDivisionError`除数为零

### 以下是 Python 内置异常类的层次结构：
*  BaseException
*  SystemExit
*  KeyboardInterrupt
*  GeneratorExit
*  Exception    # 捕获未知异常
  > * StopIteration
  > * ArithmeticError
  >> * FloatingPointError
  >> * OverflowError
  >> * ZeroDivisionError
  > * AssertionError
  > * AttributeError
  > * BufferError
  > * EOFError
  > * ImportError
  > * LookupError
  >> * IndexError
  >> * KeyError
  > * MemoryError
  > * NameError
  >> * UnboundLocalError
  > * OSError
  >> * BlockingIOError
  >> * ChildProcessError
  >> * ConnectionError
  >>> * BrokenPipeError
  >>> * ConnectionAbortedError
  >>> * ConnectionRefusedError
  >>> * ConnectionResetError
  >> * FileExistsError
  >> * FileNotFoundError
  >> * InterruptedError
  >> * IsADirectoryError
  >> * NotADirectoryError
  >> * PermissionError
  >> * ProcessLookupError
  >> * TimeoutError
  > * ReferenceError
  > * RuntimeError
  >> * NotImplementedError
  > * SyntaxError
  >> * IndentationError
  >>> * TabError
  > * SystemError
  > * TypeError
  > * ValueError
  >> * UnicodeError
  >>> * UnicodeDecodeError
  >>> * UnicodeEncodeError
  >>> * UnicodeTranslateError
  > * Warning
  >> * DeprecationWarning
  >> * PendingDeprecationWarning
  >> * RuntimeWarning
  >> * SyntaxWarning
  >> * UserWarning
  >> * FutureWarning
  >> * ImportWarning
  >> * UnicodeWarning
  >> * BytesWarning
  >> * ResourceWarning

## python的模块
### 查找模块的过程:先在当前目录找指定模块名的文件,有就直接导入,没有 再搜索系统目录
* 因此在开发时，给文件起名，不要和系统的模块文件重名
* 每一个模块都有一个内置属性`__file__`可以查看模块的完整路径,
* 也可以通过`sys`模块
```python
import sys 
print(sys.path) # 列表中的先后顺序表示导入模块时搜索的路径,空的字符串表示先在当前路径搜索
sys.path.insert(0,'')  # 在最前面插入要先搜索的路径
print(sys.argv[0]) # 代码本身文件路径
print(sys.argv[1]) # 第一个命令行参数
print(sys.argv[1:]) # 从第一个命令行参数到输入的最后一个命令行参数
print(sys.argv[1][2:]) # 取第一个命令行参数，但是去掉前两个字节
```
### 导入模块的过程:python找到这个模块然后导入,再定义一个变量名来指向该模块
* 因此多模块之间沟通需要直接导入模块名来指向模块，而不是from XX import XX
* 如果直接import导入，系统会自动避免重新导入同一模块,使模块的改变得不到更新
* 若需要更新import导入的模块，需要imp库
```python
from imp import reload
reload(random) # 此时方可得到模块的更新,此法只能更新import 导入的模块
```
* 不推荐使用`from XX import *`的方式，因为函数重名没有任何提示，出问题不好排查
### 只能在导入的值的基础上修改,不能指向一个新的值
### 如果导入的两个模块存在同名的函数,后导入的函数会覆盖先导入的函数,可以用`as`取别名区分开
### 开发时尽量将导入模块写在文件顶部，便于发现冲突
### python3.3之前，要创建一个包，都提示需要__init__.py文件，可以是空的，但是不能缺少。
### python3.3之后不需要了，但要使用一些初始化的数据还是要添加__init__.py文件,调用包的方法同调用模块的方法。
### 每一个模块的在导入时`__name__`属性中的字符串都是模块名，但在模块文件内部的`__name__`属性都是`__main__`
* 比如`time.__name__`为`time`
```python
import __main__ # 该模块整合了所有已经导入的模块，表示该模块由用户独立运行
print(__main__.sys)

import antigravity # open_an_url
print(antigravity.geohash(37.421542, -122.085589, b'2005-05-26-10458.68'))# 纬度 经度 日期
import winsound
winsound.Beep(300,100) # 音调、声音长短
```
### 还需要注意导入模块时,模块中所有没有任何缩进的代码都会被执行
* 我们通常在模块里面写一些执行代码是为了测试模块的功能,这被称为单元测试,来避免不需要执行的代码
* 在常规项目开发中，单元测试是代码质量保证的前提,比如下面的几行经常会加在文件末
```python
def multinverse(num):
    return 1 / num

if (__name__ == '__main__'):  
    print(sys.argv)
    if len(sys.argv) > 1:
        print(multinverse(sys.argv[1]))
```
### 快速学习一个库分为以下几步
> + 1. `import pickle`导入模块,`print(pickle.__name__)`确认包名
> + 2. `print(pickle.__doc__)`查看简介
> + 3. `print(pickle.__file__)`查看源代码位置
> + 4. `print(dir(pickle))`查看所有方法
> + 5. 一般其中的`pickle.__all__`会包含所有可调用的函数
> + 6. 也可用`help(pickle)`查看帮助文档
```python
import pickle
f = open('D:\\Users\\向致承\\Documents\\python\\note4.txt','wb') #注意是以二进制形式
m = ['asf',234]
pickle.dump(m,f) #调用的时候用load(f),并且文件打开的时候依然用二进制'rb'打开
f.close()

import io
f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text) # Imagine non-English language here
file = open("abc.txt","rb",encoding="utf-8")
print(file.encoding) # 'utf-8'
print(file.tell()) 
print(file.seek())
print(file.readline())
for each in file:
    print(each)

import os
os.walk()先返回该目录路径以及该目录下的所有文件(夹)名,遇到文件夹则返回该文件夹路径以#及文件夹下的所有文件,反复直到没有文件夹
os.rename(原名,新名)
os.system()执行想在终端中执行的命令

from datetime import date
now = date.today()
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")) # 01-31-20. 31 Jan 2020 is a Friday on the 31 day of January.
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days) # 20272

import zlib
s = b'witch which has which witches wrist watch'
t = zlib.compress(s)
print(len(s),len(t)) # 41 37
print(zlib.decompress(t)) # b'witch which has which witches wrist watch'
zlib.crc32(s) # 226805979

from timeit import Timer
print(Timer('t=a;a=b;b=t','a=1;b=2').timeit()) # 0.11044700000002194
print(Timer('a,b=b,a','a=1;b=2').timeit()) # 0.046078599999873404
```
```python
import time
print(time.perf_counter()) # 755.0105955
print(time.time())  # 获取当前时间戳,表示从1970年开始到现在经历的秒数
print(time.gmtime())  # 获取当前美国时间戳对应的struct_time对象
print(time.localtime())  # 获取当前时间戳对应的本地时间的struct_time对象
# 注意结果与gmtime的区别,UTC时间已自动转换为北京时间。
print(time.ctime())  # 获取当前时间戳对应的易读字符串表示,内部会调用time.localtime()函数以输出当地时间。
print(time.mktime(time.gmtime()))  # 将struct_time对象t转换为时间戳
lctime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 利用一个格式字符串，对时间格式进行表达
print(time.strptime(lctime, '%Y-%m-%d %H:%M:%S'))  # 提取字符串中时间来生成strut_time对象
print(time.monotonic())
```  
```python
import random
random.seed(10)  # 初始化随机数种子,默认值为当前系统时间,第二次设置同样的值再产生随机数则会产生一样的
print(random.random())  # 生成一个[0.0, 1.0)之间的随机小数
print(random.randint(2, 8))  # 生成一个[2,8]之间的整数
print(random.randrange(10))  # 生成10之间的一个随机数
print(random.randrange(1, 20, 3))  # 生成一个[1,20)之间以3为步数的随机整数
print(random.choice(['a', 'b', 'c', 'd']))  # 从序列类型(例如：列表)中随机返回一个元素
print(random.uniform(10, 20))  # 生成一个[10,20]之间的随机小数
la = ['a', 'b', 'c', 'd']
print(random.shuffle(la))  # 将序列类型中元素随机排列，返回打乱后的序列
print(random.sample(la, 3))  # 从pop类型中随机选取k个元素，以列表类型返回
print(random.getrandbits(3))  # 生成一个3比特长度的随机整数
```  

```python
import jieba
from wordcloud import WordCloud

excludes = {"什么","一个","我们","那里","你们","如今", \
            "说道","知道","老太太","起来","姑娘","这里", \
            "出来","他们","众人","自己","一面","太太", \
            "只见","怎么","奶奶","两个","没有","不是", \
            "不知","这个","听见"}
f = open("红楼梦.txt", "r", encoding="utf-8")
txt = f.read()
f.close()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:  #排除单个字符的分词结果
        continue
    else:
        counts[word] = counts.get(word,0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(5):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))

newtxt = ' '.join(words)
wordcloud = WordCloud(background_color="white", \
                          width=800, \
                          height=600, \
                          font_path="msyh.ttc", \
                          max_words=200, \
                          max_font_size=80, \
                          stopwords = excludes, \
                          ).generate(newtxt)
wordcloud.to_file('红楼梦基本词云.png')
#jieba.cut(s) 精确模式，返回一个可迭代的数据类型
#jieba.cut(s,cut_all=True) 全模式，输出文本s中所有的可能的单词
#jieba.cut_for_search(s) 搜索引擎模式，适合搜索引建立索引的分词结果
#jieba.lcut(s) 精确模式，返回一个列表类型
#jieba.lcut(s,cut_all=True) 全模式，返回一个列表类型
#jieba.lcut_for_search(s) 搜索引模式，返回一个列表类型
#jieba.add_word(word,freq=None,tag=None) 在程序中向字典添加单词 
#jieba.del_word(word) 删除字典中的单词
#jieba.suggest_freq(segment,tune=True) 可调节单个词语的词频，使其能（或不能）被拆分 

```
```python
import turtle
turtle.setup(650, 350, 100, 100)  # 宽度 高度 x坐标 y坐标
turtle.setpos(0, 0)  # 等同于turtle.goto(0,0);turtle.setx(0);turtle.sety(0)
turtle.penup()  # 等同于turtle.up()
turtle.speed(10)  # 取值范围0-10
turtle.seth(-40)  # turtle.setheading()设置当前朝向为-40的角度
turtle.circle(40, 80 / 2)  # 半径40角度40的弧
turtle.circle(40, steps=3)  # 边长40边数为3的三角形
turtle.fd(40) # 向前
turtle.backward() # 向相反的方向
turtle.dot(40, 'red')  # 半径40颜色red的圆点
turtle.tracer(False) # 把绘制过程关闭直接显示结果
turtle.pencolor((r, g, b))  # 3个1是白色 3个0是黑色
turtle.color(c, c)  # 等同于turtle.pencolor(c);turtle.fillcolor(c)
turtle.reset()  # 等同于turtle.home()
turtle.done()
turtle.undo() # 撤销最后一步动作

```

# pycharm快捷键 及使用技巧
* ctrl+Q 查看函数内置文件 点在函数名上 再左侧黄色灯泡中插入内置文件
* debug的时候 F8 -- step over 把函数当作一行代码来执行   F7 -- step into 在函数里面一行一行执行
* TODO注释 在井号后面空一格 输入TODO 之后在任意地方点击下方TODO窗口可以回到该行注释
* 字符串的判断避免使用or拼接复杂的逻辑条件，改为使用in

# Ipython shell命令
- `Ctrl-P`    或上箭头键 后向搜索命令历史中以当前输入的文本开头的命令
- `Ctrl-N`   或下箭头键 前向搜索命令历史中以当前输入的文本开头的命令
- `Ctrl-R`   按行读取的反向历史搜索（部分匹配）
- `Ctrl-Shift-v`   从剪贴板粘贴文本
- `Ctrl-C`   中止当前正在执行的代码
- `Ctrl-A`   将光标移动到行首
- `Ctrl-E`   将光标移动到行尾
- `Ctrl-K`   删除从光标开始至行尾的文本
- `Ctrl-U`   清除当前行的所有文本译注12
- `Ctrl-F`   将光标向前移动一个字符
- `Ctrl-b`   将光标向后移动一个字符
- `Ctrl-L`   清屏

# Ipython 魔术命令
- `%quickref` 显示IPython的快速参考
- `%magic` 显示所有魔术命令的详细文档
- `%debug` 从最新的异常跟踪的底部进入交互式调试器
- `%hist` 打印命令的输入（可选输出）历史
- `%pdb` 在异常发生后自动进入调试器
- `%paste` 执行剪贴板中的Python代码
- `%cpaste` 打开一个特殊提示符以便手工粘贴待执行的Python代码
- `%reset` 删除interactive命名空间中的全部变量/名称
- `%page` OBJECT 通过分页器打印输出OBJECT
- `%run script.py` 在IPython中执行一个Python脚本文件
- `%prun statement` 通过cProfile执行statement，并打印分析器的输出结果
- `%time statement` 报告statement的执行时间
- `%timeit statement` 多次执行statement以计算系综平均执行时间。对那些执行时 间非常小的代码很有用
- `%who、%who_ls、%whos` 显示interactive命名空间中定义的变量，信息级别/冗余度可变
- `%xdel variable` 删除variable，并尝试清除其在IPython中的对象上的一切引用

# Ipython系统交互命令
- 如：dir_info = !dir ipython中的变量可以保存系统shell中返回的结果，在调用系统shell命令时加上！即可
- `%bookmark db /home/wesm/Dropbox` 将db作为书签永久保存
- `%alias ll ls -l` 将ll作为ls -l的别名暂时保存
- `%!cmd` 在系统shell中执行cmd
- `%output  = !cmd args` 执行cmd，并将stdout存放在output中
- `%alias alias_name cmd` 为系统shell命令定义别名
- `%bookmark` 使用IPython的目录书签系统
- `%cd directory` 将系统工作目录更改为directory
- `%pwd` 返回系统的当前工作目录
- `%pushd directory` 将目前目录入栈，并转向目标目录
- `%popd` 弹出栈顶目录，并转向该目录
- `%dirs` 返回一个含有当前目录栈的列表
- `%dhist` 打印目录访问历史
- `%env` 以dict形式返回系统环境变量

# pdb 命令
1. 进入命令行Debug模式，python -m pdb xxx.py  
2. h：（help）帮助  
3. w：（where）打印当前执行堆栈  
4. d：（down）执行跳转到在当前堆栈的深一层（个人没觉得有什么用处）  
5. u：（up）执行跳转到当前堆栈的上一层  
6. b：（break）添加断点  
> + 列出当前所有断点，和断点执行到统计次数  
> + line_no：当前脚本的line_no行添加断点  
> + filename:line_no：脚本filename的line_no行添加断点  
> + function：在函数function的第一条可执行语句处添加断点  
+    7）tbreak：（temporary break）临时断点  
> + 在第一次执行到这个断点之后，就自动删除这个断点，用法和b一样  
+    8）cl：（clear）清除断点  
> + 清除所有断点  
> + bpnumber1 bpnumber2... 清除断点号为bpnumber1  bpnumber2...的断点  
> + lineno 清除当前脚本lineno行的断点  
> + filename:line_no 清除脚本filename的line_no行的断点  
+    9）disable：停用断点，参数为bpnumber，和cl的区别是，断点依然存在，只是不启用  
+    10）enable：激活断点，参数为bpnumber  
+    11）s：（step）执行下一条命令  
> + 如果本句是函数调用，则s会执行到函数的第一句  
+    12）n：（next）执行下一条语句  
> + 如果本句是函数调用，则执行函数，接着执行当前执行语句的下一条。  
+    13）r：（return）执行当前运行函数到结束  
+    14）c：（continue）继续执行，直到遇到下一条断点  
+    15）l：（list）列出源码  
> + 列出当前执行语句周围11条代码  
> + first 列出first行周围11条代码  
> + first second 列出first--second范围的代码，如果second<first，second将被解析为行数  
+    16）a：（args）列出当前执行函数的函数  
+    17）p expression：（print）输出expression的值  
+    18）pp expression：好看一点的p expression  
+    19）run：重新启动debug，相当于restart  
+    20）q：（quit）退出debug  
+    21）j lineno：（jump）设置下条执行的语句函数  
> + 只能在堆栈的最底层跳转，向后重新执行，向前可直接执行到行号  
+    22）unt：（until）执行到下一行（跳出循环），或者当前堆栈结束  
+    23）condition bpnumber conditon，给断点设置条件，当参数condition返回True的时候bpnumber断点有效，否则bpnumber断点无效
