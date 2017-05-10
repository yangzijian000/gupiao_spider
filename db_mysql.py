#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-17 下午10:17
# @Author  : YANGz1J
# @Site    : 
# @File    : db_mysql.py
# @Software: PyCharm
import pymysql
import warnings
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
        self.order = 'default'
        self.sortby = 'desc'
        self.CreateTable()
    def startoutdata(self,new_data,data_time):
        if len(new_data)==0:
            return
        conn,cursor = self.connectsql()
        action = 'insert into '+ self.tablename +\
                 '(代码,简称,最新价,涨跌幅,涨跌额,5分钟涨幅,成交量,成交额,换手率,振幅,量比,委比,市盈率,数据时间) ' \
                 'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        dt = data_time

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
        cursor.execute('CREATE TABLE IF NOT EXISTS stockfor'+self.tablename+
                       '(代码 varchar(30) not null,'
                       ' 简称 varchar(30) not null,'
                       ' 今开 varchar(30) not null,'
                       ' 最高 varchar(30) not null,'
                       ' 昨收 varchar(30) not null,'
                       ' 最低 varchar(30) not null,'
                       ' 数据时间 datetime not null,'
                       ' primary key(代码,数据时间))engine=innodb default charset=utf8;')
        conn.commit()
        cursor.close()
        conn.close()
        print('创建表成功！')
    def fetch(self,page):
        warnings.filterwarnings('ignore')
        fetch_page = (page-1) * 18
        conn, cursor = self.connectsql()
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        if self.order == 'default':
            sql = 'select * from %s order by 数据时间 desc limit %d,18'%(self.tablename,fetch_page)
        else:
            sql = 'select * from %s order by 数据时间 desc,%s %s limit %d,18'%(self.tablename,self.order,self.sortby,fetch_page)
        try:
            cursor.execute(sql)
            # cursor.scroll((page-1) * 18, mode='absolute')
            data = cursor.fetchall()
            conn.commit()
            cursor.close()
            conn.close()
            # print(data)
            return data
        except:
            # print(e)
            str = '爬取中...'
            data=(str,str,str,str,str,str,str,str,str,str,str,str,str,str,)
            datas=[]
            for i in range(0,18):
                datas.append(data)
            return datas

    def stockdata(self, new_data, data_time):
        if len(new_data)==0:
            return
        conn,cursor = self.connectsql()
        action = 'insert into stockfor'+ self.tablename +\
                 '(代码,简称,今开,最高,昨收,最低,数据时间) ' \
                 'VALUES(%s,%s,%s,%s,%s,%s,%s)'
        dt = data_time
        try:
            cursor.execute(action,
                       (new_data[0],new_data[1],new_data[2],new_data[3],new_data[4],
                        new_data[5],dt))
        except Exception as e:
            # print(Exception,':',e)
            conn.rollback()
        conn.commit()
        cursor.close()
        conn.close()
        # print('成功导入数据!')

    def InquireStock(self, text):
        conn, cursor = self.connectsql()
        try:
            sql = 'select 代码,简称,今开,昨收,最高,最低,date_format(数据时间,%s) from stockfor%s where 代码=\'%s\' order by 数据时间 desc limit 0,1;'\
                  %('\'%Y-%m-%d %H:%m:%s\'',self.tablename,text)
            # print(sql)
            cursor.execute(sql)
            stockdata = cursor.fetchall()
            today = datetime.datetime.today().date()
            sql = 'select 最新价,涨跌幅,涨跌额,成交量,换手率,市盈率,振幅,数据时间 from %s where 代码=\'%s\' ' \
                  'and 数据时间 > \'%s\' order by 数据时间 desc;'%(self.tablename,text,today.isoformat())
            # print(sql)
            cursor.execute(sql)
            data = cursor.fetchall()
            data4Day_k = []
            for i in range(1,8):
                day1 = (today-datetime.timedelta(days=i-1)).isoformat()
                day2 = (today-datetime.timedelta(days=i-2)).isoformat()
                print(day2)
                sql = 'select 昨收,数据时间 from stockfor%s where 代码=\'%s\' ' \
                      'and 数据时间 > \'%s\' and 数据时间 < \'%s\' order by ' \
                      '数据时间 desc limit 0,1;'%(self.tablename,text,day1,day2)
                cursor.execute(sql)
                data4Day_k.append(cursor.fetchone())
            conn.commit()
            cursor.close()
            conn.close()
            print(stockdata,data)
            print(data4Day_k)
        except Exception as e:
            print(e)
        return stockdata[0],data,data4Day_k




