#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-17 下午10:17
# @Author  : YANGz1J
# @Site    : 
# @File    : db_mysql.py
# @Software: PyCharm
import pymysql
import datetime
class Mysql(object):
    def __init__(self,tablename):
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.dbname = 'gupiao'
        self.passwd = '230512'
        self.charset = 'utf8'
        self.tablename = tablename
        self.CreateTable()
    def startoutdata(self,new_data):
        if len(new_data)==0:
            return
        conn,cursor = self.connectsql()
        action = 'insert into '+ self.tablename +\
                 '(代码,简称,最新价,涨跌幅,涨跌额,5分钟涨幅,成交量,成交额,换手率,振幅,量比,委比,市盈率,数据时间) ' \
                 'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        dt = new_data[len(new_data)-1]

        for i in range(0, len(new_data)-1, 13):
            try:
                cursor.execute(action,
                           (new_data[i],new_data[i+1],new_data[i+2],new_data[i+3],new_data[i+4],
                            new_data[i+5],new_data[i+6],new_data[i+7],new_data[i+8],new_data[i+9],
                            new_data[i+10],new_data[i+11],new_data[i+12],dt))
            except Exception as e:
                # print(Exception,':',e)
                i = i+13
        conn.commit()
        cursor.close()
        conn.close()
        print('成功导入数据!')



    def connectsql(self):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user,passwd=self.passwd,charset=self.charset,db=self.dbname)
        cursor = conn.cursor()
        print('连接数据库成功！')
        return conn,cursor

    def CreateTable(self):
        conn,cursor = self.connectsql()
        # cursor.execute('DROP TABLE IF EXISTS ' +self.tablename)
        # conn.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS ' + self.tablename + '(代码 varchar(30) not null,'
                                                     '  简称 varchar(30),  最新价 varchar(30),  涨跌幅 varchar(30),'
                                                     '  涨跌额 varchar(30),  5分钟涨幅 varchar(30),  成交量 varchar(30),'
                                                     '  成交额 varchar(30),  换手率 varchar(30),  振幅 varchar(30),'
                                                     '  量比 varchar(30),  委比 varchar(30),  市盈率 varchar(30),'
                                                     '数据时间 datetime,primary key(代码,数据时间))engine=innodb default charset=utf8;')
        # cursor.execute('CREATE TABLE IF NOT EXISTS timefor'+self.tablename+
        #                '(nid int not null auto_increment primary key,'
        #                'datetime datetime not null,UNIQUE (datetime))')
        conn.commit()
        cursor.close()
        conn.close()
        print('创建表成功！')
    def fetch(self,page):
        page = (page-1) * 22
        conn, cursor = self.connectsql()
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute('select * from ' + self.tablename)
            cursor.scroll(page, mode='absolute')
            data = cursor.fetchmany(22)
            conn.commit()
            cursor.close()
            conn.close()
            print(data)
            return data
        except:
            str = '爬取中...'
            data=(str,str,str,str,str,str,str,str,str,str,str,str,str,str,)
            datas=[]
            for i in range(0,22):
                datas.append(data)
            return datas

