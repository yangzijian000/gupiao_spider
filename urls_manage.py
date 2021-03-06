#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-17 下午10:25
# @Author  : YANGz1J
# @Site    : 
# @File    : urls_manage.py
# @Software: PyCharm
class Urlmanager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def get_new_url(self):
        if len(self.new_urls) == 0:
            return
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def has_new_url(self):
        return len(self.new_urls) != 0

    def add_new_urls(self, urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    def urls_clear(self):
        if self.old_urls is None and self.new_urls is None:
            return
        self.old_urls.clear()
        self.new_urls.clear()

