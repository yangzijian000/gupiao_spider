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
        soup = BeautifulSoup(html_cont.decode('gbk'), 'lxml', from_encoding='gbk')
        new_urls = self.get_new_urls(new_url)
        new_data,data_time = self.get_new_data(soup)
        new_urls_stock = self.get_new_stock_urls(soup)
        return new_urls,new_urls_stock,new_data,data_time
    def get_new_urls(self, url):
        new_urls = set()
        pattern = re.compile(r'_(\d+)\.')
        strcurpage = pattern.search(url).group(1)
        next_page = int(strcurpage) + 1
        new_url = pattern.sub('_'+str(next_page)+'.',url)
        new_urls.add(new_url)
        return new_urls

    def get_new_data(self, soup):
        tbody_tds = soup.tbody.find_all('td')
        new_data = []
        for td in tbody_tds:
            new_data.append(td.get_text())
        table_tds = soup.table.find_all('td')
        pattern = re.compile(r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})')
        data_time = pattern.search(table_tds[len(table_tds)-1].get_text()).group(1)
        return new_data,data_time
    def get_new_stock_urls(self,soup):
        new_stock_urls = set()
        tbody_a = soup.tbody.find_all('a')
        for a in tbody_a:
            new_stock_urls.add(a['href'])
        return new_stock_urls
    def stockparser(self,html_cont):
        if html_cont is None:
            return
        new_data = []
        soup = BeautifulSoup(html_cont.decode('gbk'), 'lxml' ,from_encoding='gbk')
        div = soup.find_all('div', class_='name')
        tds = soup.tbody.find_all('td')
        pattern = re.compile(r'([\d\.%]+)')
        stock_name = div[0].h2.get_text()
        stock_number = pattern.search(div[0].get_text()).group(1)
        new_data.append(stock_number)
        new_data.append(stock_name)
        data_time = tds[6].get_text() + ' ' + tds[13].get_text()
        for i in (0,1,7,8):
            match = pattern.search(tds[i].get_text())
            new_data.append(match.group(1))
        return new_data,data_time
        
