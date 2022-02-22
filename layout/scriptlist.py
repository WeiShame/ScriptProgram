"""************************************************************
*   Author  : WeiShame
*   Date    : 2022/02/12
*   function: main window's layout
*
************************************************************"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QListWidgetItem, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QListWidget, QListView, QTextEdit
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont
from PyQt5.QtCore import pyqtSlot, Qt

class myscriptlist(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
         #===========variable==============================================
        #self.setStyleSheet('background-color: 	#000000;')
        self.scriptlist_window = QListWidget()
        self.scriptlog_window = QTextEdit()
        self.mylabel = QLabel()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.button1 = QPushButton("錄製")
        self.button2 = QPushButton("刪除")
        self.button3 = QPushButton("循環N次")
        self.button4 = QPushButton("匯入腳本")
        self.button5 = QPushButton("匯出腳本")
        #-----init-----
        self.scriptlog_window.setReadOnly(True)
        self.sciptlist = ["按下右鍵", "按下左鍵"]
        self.sciptlist = ["按下右鍵", "按下左鍵", "按下左鍵", "按下左鍵", "按下左鍵", "按下左鍵"]

        self.updatelist(self.sciptlist)
        self.updatelist(self.sciptlist)
        self.scriptlog_window.setText("測試")
        
        self.scriptlist_window.setCurrentRow(0)
        self.scriptlist_window.setViewMode(QListView.ListMode)
        self.scriptlist_window.setSpacing(1)
        self.scriptlist_window.setEnabled(True)

        sp = QSizePolicy()
        sp.setVerticalPolicy(QSizePolicy.Minimum)
        self.button1.setSizePolicy(sp)
        self.button2.setSizePolicy(sp)
        self.button3.setSizePolicy(sp)
        self.button4.setSizePolicy(sp)
        self.button5.setSizePolicy(sp)

        self.button1.setStyleSheet('background-color: 	#FFFFFF;')
        self.button2.setStyleSheet('background-color: 	#FFFFFF;')
        self.button3.setStyleSheet('background-color: 	#FFFFFF;')
        self.button4.setStyleSheet('background-color: 	#FFFFFF;')
        self.button5.setStyleSheet('background-color: 	#FFFFFF;')
        self.scriptlist_window.setStyleSheet('background-color: 	#FFFFFF;')
        self.scriptlog_window.setStyleSheet('background-color: 	#FFFFFF;')
        #-----Layout setting----------------------------------------------
        # V layout
        self.v_layout.addStretch(1)
        self.v_layout.addWidget(self.button1,1)
        self.v_layout.addWidget(self.button2,1)
        self.v_layout.addWidget(self.button3,1)
        self.v_layout.addWidget(self.button4,1)
        self.v_layout.addWidget(self.button5,1)
        self.v_layout.addStretch(1)

        # H layout
        self.h_layout.addWidget(self.scriptlist_window)
        self.h_layout.addLayout(self.v_layout)
        self.h_layout.addWidget(self.scriptlog_window)

        self.setLayout(self.h_layout)

    #=================================================================
    #===========function==============================================
    def create_item(self, script_name, icon = None):
        item = QListWidgetItem()
        item.setText(script_name)
        if icon != None:
            item.setIcon(QIcon(icon))
        item.setStatusTip(script_name)
        item.setTextAlignment(Qt.AlignLeft)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        return item
    #*****************************************************************
    def updatelist(self, scriptlist):
        itemlist = []
        for index in range(len(scriptlist)):
            item = self.create_item(scriptlist[index])
            itemlist.append(item)

        self.scriptlist_window.clear()

        self.scriptlist_window.addItem(itemlist[0])
        for item in itemlist:
           self.scriptlist_window.addItem(item)
    #==================================================================
