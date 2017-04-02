import html_downloader
import html_outputer
import html_parser
import url_manager

"""
爬虫主程序
"""


class SpiderMain(object):
    #  初始化爬虫
    def __init__(self):
        # URL管理器
        self.urls = url_manager.UrlManager()
        # HTML下载器
        self.downloader = html_downloader.HtmlDownloader()
        # HTML解析器
        self.parser = html_parser.HtmlParser()
        # HTML输出器
        self.outputer = html_outputer.HtmlOutputer()

    # 爬虫的调动程序
    def craw(self, root_url):
        # 记录当前爬取的url序号
        cnt = 1
        # 添加爬取入口的url
        self.urls.add_new_url(root_url)
        # 若有新的待爬取的url，则一直循环爬取
        while self.urls.has_new_url():
            try:
                # 获取新的待爬取的url
                new_url = self.urls.get_new_url()
                # 打印当前爬取的url序号与名字
                print('craw %d : %s' % (cnt, new_url))
                # 下载爬取的页面
                html_content = self.downloader.download(new_url)
                # 解析爬取的页面
                new_urls, new_data = self.parser.parse(new_url, html_content)
                # 添加批量的带爬取的url
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)
                # 爬取目标定为爬取20个url，若完成任务，则退出循环
                if cnt == 20:
                    break
                cnt += 1
            except:
                print('craw failed.')

        # 输出收集好的数据
        self.outputer.output_html()


if __name__ == '__main__':
    # 爬虫入口页面
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.craw(root_url)
