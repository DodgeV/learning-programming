from queue import Queue, Empty

import time

import requests
from requests import HTTPError
from log import Log

"""
 网页下载器。
 发送HTTP请求，下载服务器返回的内容。
"""


class Downloader:
    def __init__(self, config):
        # 加载配置文件
        self.log = Log("downloader")

        self.user_agent_queue = Queue(maxsize=1000)
        self.proxy_queue = Queue(maxsize=1000)

        # 加载配置文件。
        # 设置agent队列。
        if 'User-Agent' in config and config['User-Agent']:
            for agent in config['User-Agent']:
                self.user_agent_queue.put(agent)
        # 设置代理IP队列。
        if 'proxies' in config and config['proxies']:
            for proxy in config['proxies']:
                self.proxy_queue.put(proxy)
        # 设置延迟请求时间，默认是2s。
        if 'delay' in config and config['delay']:
            self.delay = config['delay']
        else:
            self.delay = 2
        # 设置请求响应时间，默认是20s。
        if 'timeout' in config and config['timeout']:
            self.timeout = config['timeout']
        else:
            self.timeout = 20

    """
    UserAgent设置。
    每次从队列中取出一个返回，同时放入队列。保证多线程的情况下尽量少的重复使用。
    """

    def choice_user_agent(self):
        try:
            ua = self.user_agent_queue.get(block=True, timeout=0.5)
            self.user_agent_queue.put(ua)
            return {"User-Agent": ua}
        except Empty:
            self.log.info("队列中没有可供使用的UserAgent")

    """
    IP代理设置。
    每次从队列中取出一个返回，同时放入队列。保证多线程的情况下尽量少的重复使用。
    """

    def choice_proxies(self):
        try:
            p = self.proxy_queue.get(block=True, timeout=0.5)
            self.proxy_queue.put(p)
            return p
        except Empty:
            self.log.info("队列中没有可供使用的Proxy")

    """
    获取HTTP请求返回结果。
    :param url: 请求URL。
    :param encoding: 返回结果的编码。
    :return: 按encoding编码后的返回结果。
    """

    def get_response(self, url, encoding):
        try:
            time.sleep(self.delay)
            rsp = requests.get(url, headers=self.choice_user_agent(), proxies=self.choice_proxies(),
                               timeout=self.timeout)
            rsp.raise_for_status()
            # 如果没有传入encoding参数， 默认使用配置文件中的encoding
            if encoding:
                rsp.encoding = encoding
            return rsp
        except HTTPError:
            self.log.debug("网络异常,url=%s" % url)

    """
    获取HTTP请求返回结果
    :param url: 请求URL
    :param encoding: 返回结果的编码
    :param headers: 请求头
    :return: 按encoding编码后的返回结果。
    """

    def get(self, url, encoding, headers):
        try:
            time.sleep(self.delay)
            if headers:
                headers.update(self.choice_user_agent())
            else:
                headers = self.choice_user_agent()
            rsp = requests.get(url, headers=headers, proxies=self.choice_proxies(),
                               timeout=self.timeout)
            rsp.raise_for_status()
            # 如果没有传入encoding参数， 默认使用配置文件中的encoding
            if encoding:
                rsp.encoding = encoding

            return rsp
        except HTTPError:
            self.log.debug("网络异常,url=%s" % url)
