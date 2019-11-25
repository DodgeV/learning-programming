from threading import Thread
from queue import Queue, Empty
from ReportSpider import ReportSpider, TaskItem

from config import load_config
from log import Log

# 初始化日志
log = Log(__name__)

# 待抓取任务队列
task_queue = Queue(maxsize=100000)

# 抓取结果队列
response_queue = Queue(maxsize=100000)

# 公告爬虫
spider = ReportSpider()

# 加载配置文件
config = load_config("report.yaml")


# 加载待抓取的任务
def load_wait_crawled():
    wait_list = []
    start_url = config['start_url']
    wait_list.append(TaskItem(start_url, "", ""))
    return wait_list


"""
 Master线程：
 1. 初始化时加载待抓取的任务，放入到待抓取任务队列。
 2. 接收抓取返回队列的抓取结果。
 3. 提取抓取结果中的待抓取URL，放入到待抓取任务队列。 
"""


class MasterThread(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        # 加载待抓取任务
        task_list = load_wait_crawled()
        self.log = Log(self.name)
        for task in task_list:
            try:
                # 放入待抓取任务队列中
                task_queue.put_nowait(task)
            except:
                self.log.error("初始化加载抓取任务异常")
                continue

    def run(self):
        while True:
            try:
                # 接收抓取任务的返回结果：包含已抓取URL、解析页面内容后提取的待抓取URL列表
                response_item = response_queue.get(block=True, timeout=30)
                for task in response_item.tasks:
                    if task_queue.qsize() > 99000:
                        break
                    task_queue.put(task)
            except Empty:
                self.log.debug("response queue empty")
                break
            except:
                self.log.error("crawl task error")
                break


"""
Worker线程
1. 从待抓取任务队列中获取任务
2. 执行爬虫的抓取任务
3. 将解析页面内容后的结果放入到抓取结果队列中
"""


class WorkerThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.log = Log(self.name)

    def run(self):
        while True:
            try:
                # 从待抓取任务队列中获取任务
                task_item = task_queue.get(block=True, timeout=30)
                # 执行爬虫的抓取任务。返回抓取任务的结果：包含已抓取URL、解析页面内容后提取的待抓取URL列表
                response_item = spider.process(task_item)
                # 将解析页面内容后的结果放入到抓取结果队列中
                response_queue.put(response_item)
            except Empty:
                self.log.debug("task queue empty")
                break
            except:
                self.log.error("抓取任务返回异常")
                break


def work():
    # 定义并且启动Master线程
    master = MasterThread("masterThread")
    master.start()

    # 定义Worker线程数量
    threads_numbers = config['thread_numbers']

    worker_list = []
    # 定义Worker线程
    for i in range(threads_numbers):
        worker_thread = WorkerThread("workerThread" + str(i))
        worker_list.append(worker_thread)

    # 启动所有的Worker线程
    for t in worker_list:
        t.start()

    # Master线程加入线程同步
    master.join()
    # Worker线程分别加入线程同步
    for t in worker_list:
        t.join()


def main():
    work()


main()
