from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from clock import Ui_ClockWindow

class RootMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ClockWindow()
        self.ui.setupUi(self)

        


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = RootMain()
    sys.exit(app.exec_())