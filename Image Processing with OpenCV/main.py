import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import Ui_MainWindow
from Question1 import Image_Processing
from Question2 import Image_Smoothing
from Question3 import Edge_Detection


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.Q1 = Image_Processing()
        self.Q2 = Image_Smoothing()
        self.Q3 = Edge_Detection()

        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AppWindow()
    main.show()
    sys.exit(app.exec_())
