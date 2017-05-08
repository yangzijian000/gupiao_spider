#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-27 下午4:17
# @Author  : YANGz1J
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import re
text = requests.get('http://stock.quote.stockstar.com/300649.shtml')
soup = BeautifulSoup(text.content.decode('gbk'),'lxml',from_encoding='gbk')
divs = soup.find_all('div', class_='name')
tds = soup.tbody.find_all('td')
# leng = len(tbody_tds)
# print(text.content.decode('gbk'))
pattern = re.compile(r'([\d\.%]+)')
# data_time = tbody_tds[6].get_text()+' '+tbody_tds[13].get_text()0
print(divs[0].h2.get_text())
match = pattern.search(divs[0].get_text())
print(match.group(1))
for i in (0,1,7,8):
    match = pattern.search(tds[i].get_text())
    print(match.group(1))
# table_tds =soup.table.find_all('td')
# pattern = re.compile(r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})')
# match = pattern.search(table_tds[len(table_tds)-1].get_text())
# print(match.group(1))
# tbody_a = soup.tbody.find_all('a')
# for a in tbody_a:
#     print(a['href'])
# tbodys = soup.find_all('tbody')
# for tbody in tbodys:
    # print(tbody)
# print(text.text)