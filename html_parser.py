import re
import urllib.parse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_content):
        """
        解析该页面
        :param page_url:
        :param html_content:
        :return:
        """
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    @staticmethod
    def _get_new_urls(page_url, soup):
        """
        获取该页面中所有的符合检验规则的url
        :param page_url:
        :param soup:
        :return:
        """
        # 新的带爬取的url集合
        new_urls = set()
        # 获取所有符合检验规则的url
        links = soup.find_all('a', href=re.compile(r'/item/'))
        for link in links:
            new_url = link['href']
            # 将相对路径的url拼接成绝对路径的url
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup):
        """
        整合页面的数据
        :param page_url:
        :param soup:
        :return:
        """
        # 该页面整合的数据
        res_data = {'url': page_url}

        """
        获取爬取页面的标题
        <dd class="lemmaWgt-lemmaTitle-title">
        <h1 >Python</h1>
        """
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        """
        获取爬取页面的概要
        <div class="lemma-summary" label-module="lemmaSummary">
        <div class="para" label-module="para">
        Python语法简洁清晰，特色之一是强制用空白符(white space)作为语句缩进。
        </div></div>
        """
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        return res_data
