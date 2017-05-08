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
import gupiao_ui
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
        while 1:
            if self.urls_stock.has_new_url():
                try:
                    new_url_stock = self.urls_stock.get_new_url()
                    html_cont_stock = self.downloader.download(new_url_stock)
                    new_data, data_time = self.parser.stockparser(html_cont_stock)
                    self.mysql.stockdata(new_data, data_time)
                except:
                    # print('craw failed')
                    continue
            else:
                time.sleep(0.5)
    def process(self):
        th = threading.Thread(target=self.start,args=())
        th.setDaemon(True)
        th.start()
        th_stock = threading.Thread(target=self.start_stock,args=())
        th_stock.setDaemon(True)
        th_stock.start()
        # return th
class pagemanage(object):
    def __init__(self):
        self.currentpage=1
        self.nextpage=2
        self.prevpage=0
        self.sumpage=179
    def page_turning_down(self):
        if self.currentpage == 179:
            return 179
        self.currentpage = self.currentpage+1
        self.nextpage = self.nextpage+1
        self.prevpage = self.prevpage+1
        return self.currentpage
    def page_turring_up(self):
        if self.currentpage==1:
            return 1
        self.currentpage = self.currentpage - 1
        self.nextpage = self.nextpage - 1
        self.prevpage = self.prevpage - 1
        return self.currentpage
    def get_currentpage(self):
        return self.currentpage
if __name__ =="__main__":
    root_urlA = 'http://quote.stockstar.com/stock/ranklist_a_3_1_1.html'
    tablenameA = "沪深A股"
    gupiao_spiderA = SpiderMain(tablenameA, root_urlA)
    root_urlB = "http://quote.stockstar.com/stock/ranklist_b_3_1_1.html"
    tablenameB = "沪深B股"
    gupiao_spiderB = SpiderMain(tablenameB, root_urlB)
    gupiao_spiderB.process()
    gupiao_spiderA.process()
    # th1.join()
    # th2.join()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gupiao_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    pagemanageA = pagemanage()
    Adatas = gupiao_spiderA.mysql.fetch(pagemanageA.get_currentpage())
    ui.settabledata1(Adatas)
    pagemanageB = pagemanage()
    Bdatas = gupiao_spiderB.mysql.fetch(pagemanageB.get_currentpage())
    ui.settabledata2(Bdatas)
    MainWindow.show()
    sys.exit(app.exec_())






        
        
        
