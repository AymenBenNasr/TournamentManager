
from loginPage.loginG import *
from homePage.homeG import *
from tournamentPage.compG import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from dbConnection import *

from PyQt5.QtWidgets import *


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QMainWindow.__init__(self, parent)
        self.setObjectName("MainWindow")
        self.resize(1100, 600)
        self.setWindowTitle("MainWindow")
        self.setStyleSheet("background-color : #2d2d2d;\n"
                                 "color : #b5b5b5")
        flag = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flag)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.resize(1100,600)
        #All pages instantiation

        self.home_page = homeWid(self.central_widget)
        self.login_page = loginWid(self.central_widget , self.home_page)
        self.tournamet_page = tournamentWid()
        #Stacking all widgets

        self.central_widget.addWidget(self.login_page)
        self.central_widget.addWidget(self.home_page)
        # self.central_widget.addWidget(self.tournamet_page)
        self.central_widget.setCurrentWidget(self.home_page)


        self.home_page.btnClose.clicked.connect(lambda : self.close())


class Second(QWidget):

    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        layout = QHBoxLayout()
        button = QPushButton("bbbb")
        layout.addWidget(button)
        self.setLayout(layout)
        button.clicked.connect(self.clicked.emit)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    myWindow = MainWindow(None)
    myWindow.show()
    app.exec_()