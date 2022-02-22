"""************************************************************
*   Author  : WeiShame
*   Date    : 2022/02/12
*   function: Script of keyboard and mouse  
*
************************************************************"""
import sys
from layout import mainlayout
from PyQt5.QtWidgets import QApplication

#==================================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = mainlayout.Mywindow()
    w.show()
    sys.exit(app.exec_())