# 上市公司公告定向抓取

## 说明
 公告来源网站是东方财富。代码仅供学习参考，抓取数据必须遵守网站的规则。
 1. 默认使用公告的标题作为文件名，因为同名的公告不会重复抓取，所以不再额外使用去重处理。
 2. 动态IP可以自行配置，建议线程和IP数量保持一致。
 
### 文件
- crawl_reports.py  多线程抓取
- ReportSpider.py   公告爬虫[网站内容调整后需要修改页面提取规则]
- log.py   日志
- downloader 网页下载器
- config.py 加载配置文件
- resources/report.yaml 爬虫配置文件


### 流程
1. crawl_reports启动线程Master, 初始化任务队列。
2. 线程Worker从任务队列中获取抓取任务，启动ReportSpider的parse函数，执行抓取任务。
3. parse函数抽取网页中要继续抓取的URL以及其他需要记录的信息，返回给Worker线程。 
4. Worker将返回结果存入返回结果队列。
5. Master从返回结果队列中取出返回结果，将下一步要抓取的URL存入任务队列。
6. 任务队列为空，Worker线程退出；返回结果队列为空，Master线程退出。
7. Worker和Master都结束，退出程序。



## 配置文件 
resources/report.yaml

名称 | 说明
---|---
start_url | 代码一览表页面URL
list_url  | 公告列表URL模板
page_limit | 最多抓取的页面数[抓取最新的公告时，可以限制只抓取前几页,默认抓取前5页，不设置抓取全部]
encoding | 页面编码
thread_numbers | 线程数量
download_root | PDF公告保存路径
User-Agent | HTTP请求头
proxies | 动态IP代理设置[默认为空]
 
 
## 运行
1. 配置：
    resources/report.yaml

2. 启动抓取：
    python crawl_reports.py




