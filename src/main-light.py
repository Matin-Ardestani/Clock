from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from clock import Ui_ClockWindow

class RootMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ClockWindow()
        self.ui.setupUi(self)

        self.btn_alarm.clicked.connect(lambda: [self.pages.setCurrentWidget(self.page_alarm) , 
            self.btn_alarm.setStyleSheet('background-color: #F9F9F9; border-right: 1px solid #0B0D12'),
            self.btn_timer.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_stopW.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_world.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_settings.setStyleSheet('background-color: #DEDEDE;')
            ])

            self.btn_timer.clicked.connect(lambda: [self.pages.setCurrentWidget(self.page_timer) , 
            self.btn_timer.setStyleSheet('background-color: #F9F9F9; border-right: 1px solid #0B0D12'),
            self.btn_alarm.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_stopW.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_world.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_settings.setStyleSheet('background-color: #DEDEDE;')
            ])

            self.btn_stopW.clicked.connect(lambda: [self.pages.setCurrentWidget(self.page_stopwatch) , 
            self.btn_stopW.setStyleSheet('background-color: #F9F9F9; border-right: 1px solid #0B0D12'),
            self.btn_timer.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_alarm.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_world.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_settings.setStyleSheet('background-color: #DEDEDE;')
            ])

            self.btn_world.clicked.connect(lambda: [self.pages.setCurrentWidget(self.page_world) , 
            self.btn_world.setStyleSheet('background-color: #F9F9F9; border-right: 1px solid #0B0D12'),
            self.btn_timer.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_stopW.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_alarm.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_settings.setStyleSheet('background-color: #DEDEDE;')
            ])

            self.btn_settings.clicked.connect(lambda: [self.pages.setCurrentWidget(self.page_settings) , 
            self.btn_settings.setStyleSheet('background-color: #F9F9F9;'),
            self.btn_timer.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_stopW.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_world.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE; color: #0B0D12'),
            self.btn_alarm.setStyleSheet('border-right: 1px solid #0B0D12; background-color: #DEDEDE;')
            ])





        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = RootMain()
    sys.exit(app.exec_())