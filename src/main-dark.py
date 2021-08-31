from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

import sys

from dark import Ui_MainWindow

class RootMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        icon_light = QtGui.QIcon()
        icon_light.addPixmap(QtGui.QPixmap("/home/matin/Desktop/Tools/images/settings-light.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        icon_dark = QtGui.QIcon()
        icon_dark.addPixmap(QtGui.QPixmap("/home/matin/Desktop/Tools/images/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.ui.btn_alarm.clicked.connect(lambda: [self.ui.pages.setCurrentWidget(self.ui.page_alarm) , 
        self.ui.btn_alarm.setStyleSheet('background-color: #0B0D12; border-right: 1px solid #0B0D12; color: #F9F9F9;'),
        self.ui.btn_timer.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_stopW.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_world.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_settings.setStyleSheet('background-color: #DEDEDE;'),
        self.ui.btn_settings.setIcon(icon_dark)
        ])

        self.ui.btn_timer.clicked.connect(lambda: [self.ui.pages.setCurrentWidget(self.ui.page_timer) , 
        self.ui.btn_timer.setStyleSheet('background-color: #0B0D12; border-right: 1px solid #0B0D12; color: #F9F9F9;'),
        self.ui.btn_alarm.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_stopW.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_world.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_settings.setStyleSheet('background-color: #DEDEDE;'),
        self.ui.btn_settings.setIcon(icon_dark)
        ])

        self.ui.btn_stopW.clicked.connect(lambda: [self.ui.pages.setCurrentWidget(self.ui.page_stopwatch) , 
        self.ui.btn_stopW.setStyleSheet('background-color: #0B0D12; border-right: 1px solid #0B0D12; color: #F9F9F9;'),
        self.ui.btn_timer.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_alarm.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_world.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_settings.setStyleSheet('background-color: #DEDEDE;'),
        self.ui.btn_settings.setIcon(icon_dark)
        ])

        self.ui.btn_world.clicked.connect(lambda: [self.ui.pages.setCurrentWidget(self.ui.page_world) , 
        self.ui.btn_world.setStyleSheet('background-color: #0B0D12; border-right: 1px solid #0B0D12; color: #F9F9F9;'),
        self.ui.btn_timer.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_stopW.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_alarm.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_settings.setStyleSheet('background-color: #DEDEDE;'),
        self.ui.btn_settings.setIcon(icon_dark)
        ])

        self.ui.btn_settings.clicked.connect(lambda: [self.ui.pages.setCurrentWidget(self.ui.page_settings) , 
        self.ui.btn_settings.setStyleSheet('background-color: #0B0D12;'),
        self.ui.btn_settings.setIcon(icon_light),
        self.ui.btn_timer.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_stopW.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_world.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
        self.ui.btn_alarm.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE;')
        ])


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = RootMain()
    sys.exit(app.exec_())