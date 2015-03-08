# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Mar  8 10:42:18 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, random
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

class TabContainer(QtGui.QWidget):
  def __init__(self):
    super(TabContainer, self).__init__()
    self.initUI()
    QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)
    QtGui.QShortcut(QtGui.QKeySequence("Ctrl+T"), self, self.add_page)
    QtGui.QShortcut(QtGui.QKeySequence("Ctrl+W"), self, self.closeTab_1)
    

  def initUI(self):
    self.tabwidget = QtGui.QTabWidget(self)
    self.tabwidget.setTabPosition(QtGui.QTabWidget.North)
    self.tabButton = QtGui.QToolButton(self)
    self.tabButton.setText('+')
    font = self.tabButton.font()
    font.setBold(True)
    self.tabButton.setFont(font)
    self.tabwidget.setCornerWidget(self.tabButton)
    self.tabButton.clicked.connect(self.add_page)
    self.connect(self.tabwidget, QtCore.SIGNAL('tabCloseRequested (int)'),self.closeTab)
    self.tabwidget.setTabsClosable(True)
    self.tabwidget.setAutoFillBackground(False)
    self.tabwidget.setMovable(True)
    vbox = QtGui.QVBoxLayout()
    self.tabwidget.setDocumentMode(True)
    vbox.addWidget(self.tabwidget)
    self.setLayout(vbox)
    self.pages = []
    self.add_page()
    self.show()

  def create_page(self, *contents):
    page = QtGui.QWidget()
    num = 0 
    hbox = QtGui.QHBoxLayout() 
    vbox = QtGui.QVBoxLayout()  
    hbox.addStretch(1) 
    for c in contents[0:2]: 
        hbox.addWidget(c)
    #hbox.addWidget(contents[3])
    vbox.addLayout(hbox)
    hbox1 = QtGui.QHBoxLayout()
    hbox1.addWidget(contents[2])
    hbox1.insertStretch(0,1)
    vbox.addLayout(hbox1)
    vbox.insertStretch(-1,1) 
    page.setLayout(vbox)
    return page 
  
  def closeTab(self, index):
      if self.tabwidget.count()== 1:
          self.close()
      self.tabwidget.removeTab(index)
      
      self.tabwidget.destroy(index)
      print len(self.pages)
        
  def closeTab_1(self):
      
      index=self.tabwidget.currentIndex()
      if self.tabwidget.count()== 1:
          self.close()
      self.pages.remove(self.tabwidget.currentWidget())
      self.tabwidget.destroy(index)
      self.tabwidget.removeTab(index)
      print len(self.pages)

  def create_table(self):
    rows, columns = 10, 3
    table = QtGui.QTableWidget( rows, columns )
    table.setHorizontalHeaderLabels(['x','y','z'])
    table.setVerticalHeaderLabels(['1', '2', '3', '4', '5','6','7','8','9','10'])
    for r in xrange(rows):
        for c in xrange(columns):
            table.setItem( r, c, QtGui.QTableWidgetItem( str( random.randint(0,10) ) ) )
    table.setVisible(False)
    table.resizeColumnsToContents()
    table.resizeRowsToContents()
    table.horizontalHeader().setStretchLastSection(True)
    #table.horizontalHeader().setResizeMode(QHeaderView.Stretch);
    table.setVisible(True)
    return table

  def create_new_page_button(self):
    radioButton = QtGui.QRadioButton('2D Graph')
    radioButton.setGeometry(QtCore.QRect(0, 0, 116, 22))
    #radioButton.clicked.connect(self.add_pagex)
    return radioButton
  
  def create_new_page_button_2(self):
    radioButton_2 = QtGui.QRadioButton('3D Graph')
    radioButton_2.setGeometry(QtCore.QRect(0, 0, 116, 22))
    #radioButton_2.clicked.connect(self.add_pagex)
    return radioButton_2
  
  def create_new_page_button_3(self):
    btn = QtGui.QPushButton('Change the title of the page!')
    btn.clicked.connect(self.change_title)
    return btn

  def add_page(self):
    self.pages.append(self.create_page(self.create_new_page_button(),self.create_new_page_button_2(),self.create_table()))
    self.tabwidget.addTab( self.pages[-1] , 'Page %s' % len(self.pages) )
    self.tabwidget.setCurrentIndex( len(self.pages)-1 )
  
 

if __name__=="__main__":
    from sys import argv, exit

    a=QtGui.QApplication(sys.argv)
    m=TabContainer()
    a.installEventFilter(m)
    m.showMaximized()
    m.raise_()
    exit(a.exec_())
