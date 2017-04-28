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
text = requests.get('http://quote.stockstar.com/stock/ranklist_a_3_1_1.html')
soup = BeautifulSoup(text.text,'lxml',from_encoding='gb2312')
tds = soup.table.find_all('td')
len = len(tds)
for td in tds:
    print(td.get_text())
pattern = re.compile(r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})')
match = pattern.search(tds[len-1].get_text())
print(match.group(1))
# tbodys = soup.find_all('tbody')
# for tbody in tbodys:
    # print(tbody)
# print(text.text)