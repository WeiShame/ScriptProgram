"""************************************************************
*   Author  : WeiShame
*   Date    : 2022/02/12
*   function: main window's layout
*
************************************************************"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QMainWindow, QLabel
from layout.scriptlist import myscriptlist

class Mywindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        #-----variable----------------------------------------------------
        window_width = 720
        window_height = 720
        a = QLabel("測試")
        #獲取顯示器解析度大小
        desktop = QApplication.desktop()

        screenRect = desktop.screenGeometry()
        screen_height = screenRect.height()
        screen_width = screenRect.width()

        #宣告腳本list物件
        self.scriptlist = myscriptlist()

        self.mainlayout = QHBoxLayout()

        #*****************************************************************
        #-----Widgets Initial setting-------------------------------------
        # 調整主視窗大小
        
        self.resize(window_width, window_height)

        #設定視窗標題
        self.setWindowTitle("腳本程式")

        #視窗居中
        self.move((screen_width - window_width) / 2, (screen_height - window_height) /2)

        #設定背景顏色
        self.setStyleSheet('background-color: 	#FFFACD;')
        
        #固定視窗大小
        self.setFixedSize(window_width, window_height)    # Fixed the size of window

        #*****************************************************************
        #-----layout setting----------------------------------------------
        self.mainlayout.addWidget(self.scriptlist)
        self.setLayout(self.mainlayout)
    #==================================================================
