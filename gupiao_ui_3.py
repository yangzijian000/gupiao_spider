# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gupiao3.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import db_mysql
import stock_ui
import matplotlib.pyplot as plt
import datetime
class Ui_Stock(object):
    def setupUi(self, Stock):
        Stock.setObjectName("Stock")
        Stock.resize(1425, 960)
        self.tabWidget = QtWidgets.QTabWidget(Stock)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1401, 961))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget_A = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_A.setGeometry(QtCore.QRect(40, 30, 1321, 811))
        self.tableWidget_A.setObjectName("tableWidget_A")
        self.tableWidget_A.setColumnCount(13)
        self.tableWidget_A.setRowCount(18)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(12, item)
        self.tableWidget_A.horizontalHeader().setDefaultSectionSize(99)
        self.PageUpButton_A = QtWidgets.QPushButton(self.tab)
        self.PageUpButton_A.setGeometry(QtCore.QRect(750, 840, 126, 33))
        self.PageUpButton_A.setObjectName("PageUpButton_A")
        self.PageDownButton_A = QtWidgets.QPushButton(self.tab)
        self.PageDownButton_A.setGeometry(QtCore.QRect(880, 840, 126, 33))
        self.PageDownButton_A.setObjectName("PageDownButton_A")
        self.PageCount_A = QtWidgets.QLabel(self.tab)
        self.PageCount_A.setGeometry(QtCore.QRect(340, 850, 121, 23))
        self.PageCount_A.setObjectName("PageCount_A")
        self.Current_Page_A = QtWidgets.QLabel(self.tab)
        self.Current_Page_A.setGeometry(QtCore.QRect(480, 850, 121, 23))
        self.Current_Page_A.setObjectName("Current_Page_A")
        self.InquirelineEdit_A = QtWidgets.QLineEdit(self.tab)
        self.InquirelineEdit_A.setGeometry(QtCore.QRect(1002, 0, 151, 33))
        self.InquirelineEdit_A.setText("")
        self.InquirelineEdit_A.setObjectName("InquirelineEdit_A")
        self.InquireButton_A = QtWidgets.QPushButton(self.tab)
        self.InquireButton_A.setGeometry(QtCore.QRect(1150, 0, 126, 33))
        self.InquireButton_A.setObjectName("InquireButton_A")
        self.GotoPageLine_A = QtWidgets.QLineEdit(self.tab)
        self.GotoPageLine_A.setGeometry(QtCore.QRect(620, 840, 51, 33))
        self.GotoPageLine_A.setObjectName("GotoPageLine_A")
        self.GotoPageButton_A = QtWidgets.QPushButton(self.tab)
        self.GotoPageButton_A.setGeometry(QtCore.QRect(670, 840, 51, 33))
        self.GotoPageButton_A.setObjectName("GotoPageButton_A")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.InquirelineEdit_B = QtWidgets.QLineEdit(self.tab_2)
        self.InquirelineEdit_B.setGeometry(QtCore.QRect(1002, 0, 151, 33))
        self.InquirelineEdit_B.setText("")
        self.InquirelineEdit_B.setObjectName("InquirelineEdit_B")
        self.InquireButton_B = QtWidgets.QPushButton(self.tab_2)
        self.InquireButton_B.setGeometry(QtCore.QRect(1150, 0, 126, 33))
        self.InquireButton_B.setObjectName("InquireButton_B")
        self.PageUpButton_B = QtWidgets.QPushButton(self.tab_2)
        self.PageUpButton_B.setGeometry(QtCore.QRect(750, 840, 126, 33))
        self.PageUpButton_B.setObjectName("PageUpButton_B")
        self.PageDownButton_B = QtWidgets.QPushButton(self.tab_2)
        self.PageDownButton_B.setGeometry(QtCore.QRect(880, 840, 126, 33))
        self.PageDownButton_B.setObjectName("PageDownButton_B")
        self.tableWidget_B = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_B.setGeometry(QtCore.QRect(40, 30, 1321, 811))
        self.tableWidget_B.setObjectName("tableWidget_B")
        self.tableWidget_B.setColumnCount(13)
        self.tableWidget_B.setRowCount(18)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(12, item)
        self.tableWidget_B.horizontalHeader().setDefaultSectionSize(99)
        self.GotoPageLine_B = QtWidgets.QLineEdit(self.tab_2)
        self.GotoPageLine_B.setGeometry(QtCore.QRect(620, 840, 51, 33))
        self.GotoPageLine_B.setObjectName("GotoPageLine_B")
        self.PageCount_B = QtWidgets.QLabel(self.tab_2)
        self.PageCount_B.setGeometry(QtCore.QRect(340, 850, 121, 23))
        self.PageCount_B.setObjectName("PageCount_B")
        self.Current_Page_B = QtWidgets.QLabel(self.tab_2)
        self.Current_Page_B.setGeometry(QtCore.QRect(480, 850, 121, 23))
        self.Current_Page_B.setObjectName("Current_Page_B")
        self.GotoPageButton_B = QtWidgets.QPushButton(self.tab_2)
        self.GotoPageButton_B.setGeometry(QtCore.QRect(670, 840, 51, 33))
        self.GotoPageButton_B.setObjectName("GotoPageButton_B")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Stock)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Stock)

    def retranslateUi(self, Stock):
        _translate = QtCore.QCoreApplication.translate
        Stock.setWindowTitle(_translate("Stock", "股票查询"))
        item = self.tableWidget_A.verticalHeaderItem(0)
        item.setText(_translate("Stock", "1"))
        item = self.tableWidget_A.verticalHeaderItem(1)
        item.setText(_translate("Stock", "2"))
        item = self.tableWidget_A.verticalHeaderItem(2)
        item.setText(_translate("Stock", "3"))
        item = self.tableWidget_A.verticalHeaderItem(3)
        item.setText(_translate("Stock", "4"))
        item = self.tableWidget_A.verticalHeaderItem(4)
        item.setText(_translate("Stock", "5"))
        item = self.tableWidget_A.verticalHeaderItem(5)
        item.setText(_translate("Stock", "6"))
        item = self.tableWidget_A.verticalHeaderItem(6)
        item.setText(_translate("Stock", "7"))
        item = self.tableWidget_A.verticalHeaderItem(7)
        item.setText(_translate("Stock", "8"))
        item = self.tableWidget_A.verticalHeaderItem(8)
        item.setText(_translate("Stock", "9"))
        item = self.tableWidget_A.verticalHeaderItem(9)
        item.setText(_translate("Stock", "10"))
        item = self.tableWidget_A.verticalHeaderItem(10)
        item.setText(_translate("Stock", "11"))
        item = self.tableWidget_A.verticalHeaderItem(11)
        item.setText(_translate("Stock", "12"))
        item = self.tableWidget_A.verticalHeaderItem(12)
        item.setText(_translate("Stock", "13"))
        item = self.tableWidget_A.verticalHeaderItem(13)
        item.setText(_translate("Stock", "14"))
        item = self.tableWidget_A.verticalHeaderItem(14)
        item.setText(_translate("Stock", "15"))
        item = self.tableWidget_A.verticalHeaderItem(15)
        item.setText(_translate("Stock", "16"))
        item = self.tableWidget_A.verticalHeaderItem(16)
        item.setText(_translate("Stock", "17"))
        item = self.tableWidget_A.verticalHeaderItem(17)
        item.setText(_translate("Stock", "18"))
        item = self.tableWidget_A.horizontalHeaderItem(0)
        item.setText(_translate("Stock", "代码"))
        item = self.tableWidget_A.horizontalHeaderItem(1)
        item.setText(_translate("Stock", "简称"))
        item = self.tableWidget_A.horizontalHeaderItem(2)
        item.setText(_translate("Stock", "最新价"))
        item = self.tableWidget_A.horizontalHeaderItem(3)
        item.setText(_translate("Stock", "涨幅率"))
        item = self.tableWidget_A.horizontalHeaderItem(4)
        item.setText(_translate("Stock", "涨幅额"))
        item = self.tableWidget_A.horizontalHeaderItem(5)
        item.setText(_translate("Stock", "5分钟涨幅"))
        item = self.tableWidget_A.horizontalHeaderItem(6)
        item.setText(_translate("Stock", "成交量(手)"))
        item = self.tableWidget_A.horizontalHeaderItem(7)
        item.setText(_translate("Stock", "成交额(万)"))
        item = self.tableWidget_A.horizontalHeaderItem(8)
        item.setText(_translate("Stock", "换手率"))
        item = self.tableWidget_A.horizontalHeaderItem(9)
        item.setText(_translate("Stock", "振幅"))
        item = self.tableWidget_A.horizontalHeaderItem(10)
        item.setText(_translate("Stock", "量比"))
        item = self.tableWidget_A.horizontalHeaderItem(11)
        item.setText(_translate("Stock", "委比"))
        item = self.tableWidget_A.horizontalHeaderItem(12)
        item.setText(_translate("Stock", "市盈率"))
        self.PageUpButton_A.setText(_translate("Stock", "上一页"))
        self.PageDownButton_A.setText(_translate("Stock", "下一页"))
        self.PageCount_A.setText(_translate("Stock", "TextLabel"))
        self.Current_Page_A.setText(_translate("Stock", "TextLabel"))
        self.InquireButton_A.setText(_translate("Stock", "查询"))
        self.GotoPageButton_A.setText(_translate("Stock", "GO"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Stock", "沪深A股"))
        self.InquireButton_B.setText(_translate("Stock", "查询"))
        self.PageUpButton_B.setText(_translate("Stock", "上一页"))
        self.PageDownButton_B.setText(_translate("Stock", "下一页"))
        item = self.tableWidget_B.verticalHeaderItem(0)
        item.setText(_translate("Stock", "1"))
        item = self.tableWidget_B.verticalHeaderItem(1)
        item.setText(_translate("Stock", "2"))
        item = self.tableWidget_B.verticalHeaderItem(2)
        item.setText(_translate("Stock", "3"))
        item = self.tableWidget_B.verticalHeaderItem(3)
        item.setText(_translate("Stock", "4"))
        item = self.tableWidget_B.verticalHeaderItem(4)
        item.setText(_translate("Stock", "5"))
        item = self.tableWidget_B.verticalHeaderItem(5)
        item.setText(_translate("Stock", "6"))
        item = self.tableWidget_B.verticalHeaderItem(6)
        item.setText(_translate("Stock", "7"))
        item = self.tableWidget_B.verticalHeaderItem(7)
        item.setText(_translate("Stock", "8"))
        item = self.tableWidget_B.verticalHeaderItem(8)
        item.setText(_translate("Stock", "9"))
        item = self.tableWidget_B.verticalHeaderItem(9)
        item.setText(_translate("Stock", "10"))
        item = self.tableWidget_B.verticalHeaderItem(10)
        item.setText(_translate("Stock", "11"))
        item = self.tableWidget_B.verticalHeaderItem(11)
        item.setText(_translate("Stock", "12"))
        item = self.tableWidget_B.verticalHeaderItem(12)
        item.setText(_translate("Stock", "13"))
        item = self.tableWidget_B.verticalHeaderItem(13)
        item.setText(_translate("Stock", "14"))
        item = self.tableWidget_B.verticalHeaderItem(14)
        item.setText(_translate("Stock", "15"))
        item = self.tableWidget_B.verticalHeaderItem(15)
        item.setText(_translate("Stock", "16"))
        item = self.tableWidget_B.verticalHeaderItem(16)
        item.setText(_translate("Stock", "17"))
        item = self.tableWidget_B.verticalHeaderItem(17)
        item.setText(_translate("Stock", "18"))
        item = self.tableWidget_B.horizontalHeaderItem(0)
        item.setText(_translate("Stock", "代码"))
        item = self.tableWidget_B.horizontalHeaderItem(1)
        item.setText(_translate("Stock", "简称"))
        item = self.tableWidget_B.horizontalHeaderItem(2)
        item.setText(_translate("Stock", "最新价"))
        item = self.tableWidget_B.horizontalHeaderItem(3)
        item.setText(_translate("Stock", "涨幅率"))
        item = self.tableWidget_B.horizontalHeaderItem(4)
        item.setText(_translate("Stock", "涨幅额"))
        item = self.tableWidget_B.horizontalHeaderItem(5)
        item.setText(_translate("Stock", "5分钟涨幅"))
        item = self.tableWidget_B.horizontalHeaderItem(6)
        item.setText(_translate("Stock", "成交量(手)"))
        item = self.tableWidget_B.horizontalHeaderItem(7)
        item.setText(_translate("Stock", "成交额(万)"))
        item = self.tableWidget_B.horizontalHeaderItem(8)
        item.setText(_translate("Stock", "换手率"))
        item = self.tableWidget_B.horizontalHeaderItem(9)
        item.setText(_translate("Stock", "振幅"))
        item = self.tableWidget_B.horizontalHeaderItem(10)
        item.setText(_translate("Stock", "量比"))
        item = self.tableWidget_B.horizontalHeaderItem(11)
        item.setText(_translate("Stock", "委比"))
        item = self.tableWidget_B.horizontalHeaderItem(12)
        item.setText(_translate("Stock", "市盈率"))
        self.PageCount_B.setText(_translate("Stock", "TextLabel"))
        self.Current_Page_B.setText(_translate("Stock", "TextLabel"))
        self.GotoPageButton_B.setText(_translate("Stock", "GO"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Stock", "沪深B股"))

class pagemanage(object):
    def __init__(self):
        self.currentpage=1
        self.sumpage=179
    def page_turning_down(self):
        if self.currentpage == 179:
            return 179
        self.currentpage = self.currentpage + 1
        return self.currentpage
    def page_turring_up(self):
        if self.currentpage==1:
            return 1
        self.currentpage = self.currentpage - 1
        return self.currentpage
    def get_currentpage(self):
        return self.currentpage
    def goto_page(self,page):
        if page < 1:
            page =1
        if page >179:
            page =179
        self.currentpage = page
        return self.currentpage
class MY_UI(QtWidgets.QWidget,Ui_Stock):
    def __init__(self):
        super(MY_UI,self).__init__()
        self.setupUi(self)
        self.pagemanger_A = pagemanage()
        self.pagemanger_B = pagemanage()
        self.initui()
        self.dbA = db_mysql.Mysql('沪深A股')
        self.dbB = db_mysql.Mysql('沪深B股')
        self.initdataA()
        self.initdataB()
    def initui(self):
        self.tableWidget_A.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_A.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_A.verticalHeader().setVisible(False)
        self.tableWidget_B.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_B.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_B.verticalHeader().setVisible(False)
        self.tableWidget_A.horizontalHeader().sectionClicked.connect(self.SortA_desc)
        self.tableWidget_B.horizontalHeader().sectionClicked.connect(self.SortB_desc)
        self.tableWidget_A.cellDoubleClicked.connect(self.itemdoubleclicked_A)
        self.tableWidget_B.cellDoubleClicked.connect(self.itemdoubleclicked_B)
        self.PageUpButton_A.clicked.connect(self.PageUpButton_A_clicked)
        self.PageDownButton_A.clicked.connect(self.PageDownButton_A_clicked)
        self.PageUpButton_B.clicked.connect(self.PageUpButton_B_clicked)
        self.PageDownButton_B.clicked.connect(self.PageDownButton_B_clicked)
        self.InquireButton_A.clicked.connect(self.InquireButton_A_clicked)
        self.InquireButton_B.clicked.connect(self.InquireButton_B_clicked)
        self.InquirelineEdit_A.returnPressed.connect(self.InquireButton_A_clicked)
        self.InquirelineEdit_B.returnPressed.connect(self.InquireButton_B_clicked)
        self.PageCount_A.setText('总共179页')
        self.PageCount_B.setText('总共179页')
        self.Current_Page_A.setText('当前为'+str(self.pagemanger_A.currentpage)+'页')
        self.Current_Page_B.setText('当前为'+str(self.pagemanger_B.currentpage)+'页')
        self.GotoPageButton_A.clicked.connect(self.GotoPageButton_A_clicked)
        self.GotoPageButton_B.clicked.connect(self.GotoPageButton_B_clicked)
        self.GotoPageLine_A.returnPressed.connect(self.GotoPageButton_A_clicked)
        self.GotoPageLine_B.returnPressed.connect(self.GotoPageButton_B_clicked)
    def SortA_asc(self,colum):
        order = {0: 'default', 1: 'default', 2: '最新价', 3: '(涨跌幅+0)', 4: '(涨跌额+0)', 5: '(5分钟涨幅+0)',
                 6: '成交量', 7: '成交额', 8: '(换手率+0)', 9: '(振幅+0)', 10: '量比', 11: '(委比+0)', 12: '市盈率', }
        self.dbA.order = order[colum]
        self.dbA.sortby = 'asc'
        self.tableWidget_A.horizontalHeader().sectionClicked.disconnect(self.SortA_asc)
        self.tableWidget_A.horizontalHeader().sectionClicked.connect(self.SortA_desc)
        self.initdataA()
    def SortA_desc(self,colum):
        order = {0: 'default', 1: 'default', 2: '最新价', 3: '(涨跌幅+0)', 4: '(涨跌额+0)', 5: '(5分钟涨幅+0)',
                 6: '成交量', 7: '成交额', 8: '(换手率+0)', 9: '(振幅+0)', 10: '量比', 11: '(委比+0)', 12: '市盈率', }
        self.dbA.order = order[colum]
        self.dbA.sortby = 'desc'
        self.tableWidget_A.horizontalHeader().sectionClicked.disconnect(self.SortA_desc)
        self.tableWidget_A.horizontalHeader().sectionClicked.connect(self.SortA_asc)
        self.initdataA()
    def SortB_asc(self,colum):
        order = {0: 'default', 1: 'default', 2: '最新价', 3: '(涨跌幅+0)', 4: '(涨跌额+0)', 5: '(5分钟涨幅+0)',
                 6: '成交量', 7: '成交额', 8: '(换手率+0)', 9: '(振幅+0)', 10: '量比', 11: '(委比+0)', 12: '市盈率', }
        self.dbB.order = order[colum]
        self.dbB.sortby = 'asc'
        self.tableWidget_B.horizontalHeader().sectionClicked.disconnect(self.SortB_asc)
        self.tableWidget_B.horizontalHeader().sectionClicked.connect(self.SortB_desc)
        self.initdataB()
    def SortB_desc(self,colum):
        order = {0: 'default', 1: 'default', 2: '最新价', 3: '(涨跌幅+0)', 4: '(涨跌额+0)', 5: '(5分钟涨幅+0)',
                 6: '成交量', 7: '成交额', 8: '(换手率+0)', 9: '(振幅+0)', 10: '量比', 11: '(委比+0)', 12: '市盈率', }
        self.dbB.order = order[colum]
        self.dbB.sortby = 'desc'
        self.tableWidget_B.horizontalHeader().sectionClicked.disconnect(self.SortB_desc)
        self.tableWidget_B.horizontalHeader().sectionClicked.connect(self.SortB_asc)
        self.initdataB()
    def initdataA(self):
        datas = self.dbA.fetch(self.pagemanger_A.get_currentpage())
        self.settabledataA(datas)
    def initdataB(self):
        datas = self.dbB.fetch(self.pagemanger_B.get_currentpage())
        self.settabledataB(datas)
    def settabledataA(self,datas):
        self.tableWidget_A.clearContents()
        for i in range(0,len(datas)):
            for j in range(0, 13):
                item =QtWidgets.QTableWidgetItem(datas[i][j])
                self.tableWidget_A.setItem(i,j,item)
    def settabledataB(self,datas):
        self.tableWidget_B.clearContents()
        for i in range(0,len(datas)):
            for j in range(0, 13):
                item =QtWidgets.QTableWidgetItem(datas[i][j])
                self.tableWidget_B.setItem(i,j,item)

    def PageUpButton_A_clicked(self):
        datas = self.dbA.fetch(self.pagemanger_A.page_turring_up())
        self.settabledataA(datas)
        self.Current_Page_A.setText('当前为' + str(self.pagemanger_A.currentpage) + '页')

    def PageDownButton_A_clicked(self):
        datas = self.dbA.fetch(self.pagemanger_A.page_turning_down())
        self.settabledataA(datas)
        self.Current_Page_A.setText('当前为' + str(self.pagemanger_A.currentpage) + '页')

    def PageUpButton_B_clicked(self):
        datas = self.dbB.fetch(self.pagemanger_B.page_turring_up())
        self.settabledataB(datas)
        self.Current_Page_B.setText('当前为' + str(self.pagemanger_B.currentpage) + '页')

    def PageDownButton_B_clicked(self):
        datas = self.dbB.fetch(self.pagemanger_B.page_turning_down())
        self.settabledataB(datas)
        self.Current_Page_B.setText('当前为' + str(self.pagemanger_B.currentpage) + '页')

    def GotoPageButton_A_clicked(self):
        try:
            page = int(self.GotoPageLine_A.text())
            datas = self.dbA.fetch(self.pagemanger_A.goto_page(page))
            self.settabledataA(datas)
            self.Current_Page_A.setText('当前为' + str(self.pagemanger_A.currentpage) + '页')
        except:
            return

    def GotoPageButton_B_clicked(self):
        try:
            page = int(self.GotoPageLine_B.text())
            datas = self.dbB.fetch(self.pagemanger_B.goto_page(page))
            self.settabledataB(datas)
            self.Current_Page_B.setText('当前为' + str(self.pagemanger_B.currentpage) + '页')
        except:
            return

    def InquireButton_A_clicked(self):
        try:
            text = self.InquirelineEdit_A.text()
            stockdata,datas,data4Day_k = self.dbA.InquireStock(text)
            self.drawtimepicture(datas)
            self.drawK_day(data4Day_k)
            self.Dialog = MY_DIALOG(datas[0],stockdata)
            self.Dialog.show()
        except:
            return

    def InquireButton_B_clicked(self):
        try:
            text = self.InquirelineEdit_B.text()
            stockdata,datas,data4Day_k = self.dbB.InquireStock(text)
            self.drawtimepicture(datas)
            self.drawK_day(data4Day_k)
            self.Dialog = MY_DIALOG(datas[0], stockdata)
            self.Dialog.show()
        except:
            return
    def itemdoubleclicked_A(self,row,colum):
        item = self.tableWidget_A.item(row,0)
        text = item.text()
        stockdata, datas, data4Day_k = self.dbA.InquireStock(text)
        self.drawtimepicture(datas)
        self.drawK_day(data4Day_k)
        self.Dialog = MY_DIALOG(datas[0], stockdata)
        self.Dialog.show()

    def itemdoubleclicked_B(self,row,colum):
        item = self.tableWidget_B.item(row,0)
        text = item.text()
        stockdata, datas, data4Day_k = self.dbB.InquireStock(text)
        self.drawtimepicture(datas)
        self.drawK_day(data4Day_k)
        self.Dialog = MY_DIALOG(datas[0], stockdata)
        self.Dialog.show()

    def drawtimepicture(self,datas):
        fig = plt.figure()
        fig.set_size_inches(15.5, 4.01)
        ax = fig.add_subplot(1, 1, 1)
        x = []
        y = []
        group_labels = ['9:30', '10:30', '11:30', '13:00', '14:00', '15:00']
        x_label = [570, 630, 690, 780, 840, 900]
        for data in datas:
            hour = data[7].time().hour
            minute = data[7].time().minute
            # x_label = hour+':'+minute
            # group_labels.append(x_label)
            x.append(hour * 60 + minute)
            y.append(data[0])
        plt.plot(x, y)
        plt.xticks(x_label, group_labels, rotation=0)
        # for label in ax.xaxis.get_ticklabels():
        #     label.set_rotation(45)
        plt.savefig('stock.png')

    def drawK_day(self,data4Day_k):
        fig = plt.figure()
        fig.set_size_inches(15.5, 4.01)
        x = []
        y = []
        group_labels = []
        today = datetime.datetime.today().date()
        for data in data4Day_k:
            if data is None:
                continue
            x.append(data[1])
            y.append(data[0])
        for i in range(1, 7):
            day = (today - datetime.timedelta(days=i)).isoformat()
            group_labels.append(day)
        plt.plot(x, y)
        plt.xticks(x, group_labels, rotation=0)
        plt.savefig('K_day.png')


class MY_DIALOG(QtWidgets.QDialog,stock_ui.Ui_Dialog):
    def __init__(self,data,stockdata):
        super(MY_DIALOG,self).__init__()
        self.setupUi(self)
        self.data = data
        self.stockdata = stockdata
        self.initui()
    def initui(self):
        self.label.setText(self.stockdata[1])
        self.label_2.setText('代码:'+self.stockdata[0])
        self.label_3.setText('最新价:'+self.data[0])
        self.label_4.setText('涨跌幅:'+self.data[1])
        self.label_5.setText('涨跌额:'+self.data[2])
        self.label_6.setText('今开:'+self.stockdata[2])
        self.label_7.setText('昨收:'+self.stockdata[4])
        self.label_8.setText('最高:'+self.stockdata[3])
        self.label_9.setText('最低:'+self.stockdata[5])
        self.label_10.setText('成交(万手)：'+self.data[3])
        self.label_11.setText('换手:'+self.data[4])
        self.label_12.setText('市盈:'+self.data[5])
        self.label_13.setText('振幅:'+self.data[6])
        self.label_14.setText(self.stockdata[6])
        print(self.data[2][0])
        if self.data[2][0] !='-' :
            self.label.setStyleSheet("QLabel{color:#DC143C;font-size:16;font-weight:bold;font-family:Ubuntu;}")
            self.label_3.setStyleSheet("QLabel{color:#DC143C;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_4.setStyleSheet("QLabel{color:#DC143C;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_5.setStyleSheet("QLabel{color:#DC143C;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_6.setStyleSheet("QLabel{color:#DC143C;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_8.setStyleSheet("QLabel{color:#DC143C;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_12.setStyleSheet("QLabel{color:#DC143C;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_13.setStyleSheet("QLabel{color:#DC143C;font-size:11;font-weight:bold;font-family:Ubuntu;}")
        else:
            self.label.setStyleSheet("QLabel{color:green;font-size:16;font-weight:bold;font-family:Ubuntu;}")
            self.label_3.setStyleSheet("QLabel{color:green;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_3.setStyleSheet("QLabel{color:green;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_3.setStyleSheet("QLabel{color:green;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_3.setStyleSheet("QLabel{color:green;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_3.setStyleSheet("QLabel{color:green;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_3.setStyleSheet("QLabel{color:green;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_4.setStyleSheet("QLabel{color:green;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_5.setStyleSheet("QLabel{color:green;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_6.setStyleSheet("QLabel{color:green;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_8.setStyleSheet("QLabel{color:green;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_12.setStyleSheet("QLabel{color:green;font-size:11;font-weight:bold;font-family:Ubuntu;}")
            self.label_13.setStyleSheet("QLabel{color:green;font-size:11;font-weight:bold;font-family:Ubuntu;}")

        self.pixmap = QtGui.QPixmap()
        self.pixmap.load('stock.png')
        item = QtWidgets.QGraphicsPixmapItem(self.pixmap)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addItem(item)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()
        self.pixmap1 = QtGui.QPixmap()
        self.pixmap1.load('K_day.png')
        item1 = QtWidgets.QGraphicsPixmapItem(self.pixmap1)
        self.scene1 = QtWidgets.QGraphicsScene()
        self.scene1.addItem(item1)
        self.graphicsView_2.setScene(self.scene1)
        self.graphicsView_2.show()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MY_UI()
    ui.show()
    sys.exit(app.exec_())