import json
import re
import os
from bs4 import BeautifulSoup

from Singleton import Singleton
from config import load_config
from downloader import Downloader
from log import Log

"""
下一步待执行的抓取任务。
:param url：爬虫下一步待抓取的URL。
:param code: 待抓取公告的股票代码。1.组装公告列表URL时需要code;2.本地下载公告后，建立以股票代码为名字的文件夹存放该上市公司的所有公告。 
:param title: 待抓取公告的名字。下载公告后，需要以公告的名字作为文件名。
"""


class TaskItem:
    def __init__(self, url, code, title):
        self.url = url
        self.code = code
        self.title = title


"""  
爬虫抓取后的返回结果。 
:param url: 已抓取页面的请求网址。
:param tasks: 下一步待抓取的任务集合。
"""


class ResponseItem:
    def __init__(self, url, tasks):
        self.url = url
        self.tasks = tasks


"""
抓取公告的爬虫。
:param downloader 网页下载器。
:param start_url 开始抓取的URL。
:param list_url 列表页URL。
:param page_total 总页数 - 指定要抓取的列表页总数。
:param encoding 页面编码。
:param download_root 下载文件保存目录。
"""


class ReportSpider(Singleton):
    def __init__(self):
        # 加载爬虫配置文件
        config = load_config("report.yaml")
        self.downloader = Downloader(config)
        self.config = config
        self.list_url = config['list_url']
        self.page_limit = config['page_limit']
        self.encoding = config['encoding']
        self.download_root = config['download_root']
        self.log = Log(__name__)

    """
    根据不同URL的特征，指定解析函数。
    :param task: 抓取任务
    :return: 解析页面后提取的信息以及当前请求的URL
    """

    def process(self, task):
        url = task.url
        try:
            if bool(re.match(r'.*quote\.eastmoney\.com/stocklist\.html', url)):
                return self.parse_index_page(task)

            elif bool(re.match(r'.*data\.eastmoney\.com/notices/getdata\.ashx.*', url)):
                return self.parse_report_list(task)

            elif bool(re.match(r'.*data\.eastmoney\.com/notices/detail/[\d]{6}/.*', url)):
                return self.parse_report_page(task)
            elif bool(re.match(r'.*pdf\.dfcfw\.com/pdf.*', url)):
                return self.parse_pdf_page(task)
        except:
            self.log.error("提取信息异常")

        return ResponseItem(url, [])

    """ 
    解析股票代码一览表页面，提取股票代码，组装公告第一页URL。
    :param task: 抓取任务。
    :return: 解析页面后提取的信息以及当前请求的URL。
    """

    def parse_index_page(self, task):
        url = task.url
        task_list = []

        resp = self.downloader.get_response(url, encoding=self.encoding)
        soup = BeautifulSoup(resp.text, 'html.parser')
        a_list = soup.find_all("a")

        # 组装列表页URL，例子：
        # code = "000001"
        # list_url = self.list_url % {"code": code, "page": str(1)}
        # task_list.append(TaskItem(list_url, code, ""))
        for a in a_list:
            try:
                href = a.attrs['href']
                # 600XXX、601XXX、603XXX、000xxx  沪深A股
                code = re.findall('s[hz]((?:600|601|603|000)[\d]{3})', href)[0]
                list_url = self.list_url % {"code": code, "page": str(1)}
                task_list.append(TaskItem(list_url, code, ""))
            except:
                continue
        return ResponseItem(url, task_list)

    """ 
    解析公告列表URL返回文本，提取公告页面URL以及公告标题。
    :param task: 抓取任务。
    :return: 解析页面后提取的信息以及当前请求的URL。
    """

    def parse_report_list(self, task):
        url = task.url
        task_list = []

        resp = self.downloader.get_response(url, self.encoding)
        # 提取返回文本中的json字符串
        resp_json = json.loads(re.findall(r'=[\s]({"data".*);', resp.text)[0])
        code = task.code
        for info in resp_json['data']:
            # 公告中带有分号，在windows系统中， 文件的命名不能包含分号。
            title = info['NOTICETITLE'].split(':')[-1]
            task_list.append(TaskItem(info['Url'], code, title))

        page_index = int(re.findall('PageIndex=([\d]+)&PageSize', url)[0])

        # 当请求页面为1时，获取总页数，并生成股票公告列表请求URL
        total = int(resp_json['pages'])

        if self.page_limit and total > self.page_limit:
            total = self.page_limit

        if page_index < total:
            reports_url = self.list_url % {"code": code, "page": str(page_index + 1)},
            task_list.append(TaskItem(reports_url, code, ""))

        return ResponseItem(url, task_list)

    """ 
    解析公告页URL返回文本，提取公告页面URL以及公告标题。
    :param task: 抓取任务。
    :return: 解析页面后提取的信息以及当前请求的URL。
    """

    def parse_report_page(self, task):
        url = task.url
        task_list = []

        code = task.code
        title = task.title
        resp = self.downloader.get_response(url, encoding=self.encoding)
        if bool(re.match('application/pdf', resp.headers["Content-Type"])):
            self.save_pdf(code, title + ".pdf", resp.content)
            return ResponseItem(url, task_list)

        elif bool(re.match('text/html', resp.headers["Content-Type"])):
            soup = BeautifulSoup(resp.text, 'html.parser')
            tag = soup.select("div.detail-header > h1 > span > a")[0]
            task_list.append(TaskItem(tag.attrs['href'], code, title))
            return ResponseItem(url, task_list)

        return ResponseItem(url, task_list)

    """ 
    获取PDF公告URL的返回文件，下载文件内容。
    :param task: 抓取任务。
    :return: 
    """

    def parse_pdf_page(self, task):
        url = task.url
        resp = self.downloader.get_response(task.url, encoding=None)
        if bool(re.match('application/pdf', resp.headers["Content-Type"])):
            self.save_pdf(self.download_root + task.code, task.title + ".pdf", resp.content)
        return ResponseItem(url, [])

    """
    保存文件。
    :param root: 文件目录。
    :param filename: 文件名。
    :param content: 文件内容。
    :return:
    """

    def save_pdf(self, root, filename, content):
        path = root + "/" + filename
        if not os.path.exists(root):
            os.makedirs(root)
        if not os.path.exists(path):
            with open(path, 'wb') as f:
                f.write(content)
                f.close()
                self.log.info("文件保存成功:%s" % path)
        else:
            self.log.debug("文件已经存在")
