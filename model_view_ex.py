# model_view_ex.py
# Asis Sotelo
#
# 04April21

import sys, csv
from PyQt5.QtWidgets import (QApplication,QWidget,QTableView,QVBoxLayout)
from PyQt5.QtGui import QStandardItemModel,QStandardItemModel

## Create class and initialize with constructor

class DisplayParts(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """ Initialize the Window and display its contents to the screen"""

        self.setGeometry(100,100,450,300)
        self.setWindowTitle('Model View')

        # self.setupModelView()

        self.show()




if __name__ =='__main__':
    app = QApplication(sys.argv)
    window=DisplayParts()
    sys.exit(app.exec_())

