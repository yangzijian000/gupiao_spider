#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-17 下午9:24
# @Author  : YANGz1J
# @Site    : 
# @File    : spider_main.py
# @Software: PyCharm
import sys

import time
from PyQt5 import QtWidgets

import db_mysql,urls_download,urls_manage,urls_parser
import threading
import gupiao_ui_3 as UI
class SpiderMain(object):
    def __init__(self, tablename,root_url):
        self.urls = urls_manage.Urlmanager()
        self.downloader = urls_download.Downloader()
        self.parser = urls_parser.Parser()
        self.mysql = db_mysql.Mysql(tablename)
        self.root_url = root_url
        self.tablename = tablename
        self.urls_stock = urls_manage.Urlmanager()
    def start(self):
        page = 1
        self.urls.add_new_url(self.root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print ('get page %d:%s' % (page, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_url_stock, new_data, data_time = self.parser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.mysql.startoutdata(new_data, data_time)
                self.urls_stock.add_new_urls(new_url_stock)
                th_stock = threading.Thread(target=self.start_stock, args=())
                th_stock.setDaemon(True)
                th_stock.start()
                if page == 107 and self.tablename == '沪深A股':
                    self.urls.urls_clear()
                    self.urls.add_new_url(self.root_url)
                    page = 1
                    continue
                elif page == 4 and self.tablename == '沪深B股':
                    self.urls.urls_clear()
                    self.urls.add_new_url(self.root_url)
                    page = 1
                    continue
                page = page + 1
            except Exception as e:
                print('craw failed')
                page = page + 1
                print(e)
    def start_stock(self):
            if self.urls_stock.has_new_url():
                try:
                    new_url_stock = self.urls_stock.get_new_url()
                    html_cont_stock = self.downloader.download(new_url_stock)
                    new_data, data_time = self.parser.stockparser(html_cont_stock)
                    self.mysql.stockdata(new_data, data_time)
                except:
                    # print('craw failed')
                    return
            else:
                self.urls_stock.urls_clear()
    def process(self):
        th = threading.Thread(target=self.start,args=())
        th.setDaemon(True)
        th.start()


if __name__ =="__main__":
    root_urlA = 'http://quote.stockstar.com/stock/ranklist_a_3_1_1.html'
    tablenameA = "沪深A股"
    gupiao_spiderA = SpiderMain(tablenameA, root_urlA)
    root_urlB = "http://quote.stockstar.com/stock/ranklist_b_3_1_1.html"
    tablenameB = "沪深B股"
    gupiao_spiderB = SpiderMain(tablenameB, root_urlB)
    gupiao_spiderB.process()
    gupiao_spiderA.process()
    app = QtWidgets.QApplication(sys.argv)
    ui = UI.MY_UI()
    ui.show()
    sys.exit(app.exec_())





        
        
        
