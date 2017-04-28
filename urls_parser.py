#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-17 下午10:17
# @Author  : YANGz1J
# @Site    : 
# @File    : urls_parser.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import re
class Parser(object):

    def parser(self, new_url, html_cont):
        if new_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'lxml', from_encoding='gb2312')
        new_urls = self.get_new_urls(new_url)
        new_data = self.get_new_data(soup)
        return new_urls,new_data
    def get_new_urls(self, url):
        new_urls = set()
        pattern = re.compile(r'_(\d+)\.')
        strcurpage = pattern.search(url).group(1)
        next_page = int(strcurpage) + 1
        new_url = pattern.sub('_'+str(next_page)+'.',url)
        new_urls.add(new_url)
        return new_urls

    def get_new_data(self, soup):
        tds = soup.table.find_all('td')
        new_data = []
        for i in range(0,len(tds)-2):
            new_data.append(tds[i].get_text())
        pattern = re.compile(r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})')
        data_time = pattern.search(tds[len(tds)-1].get_text()).group(1)
        new_data.append(data_time)
        return new_data