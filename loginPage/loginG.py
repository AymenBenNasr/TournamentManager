from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from loginPage.login import *
from dbConnection import *


class loginWid(QWidget, Ui_Login_Page):
    clicked = pyqtSignal()

    def __init__(self, central_widget, landingpage , parent=None):
        QWidget.__init__(self, parent=None)
        self.central_widget = central_widget
        self.landingpage = landingpage
        self.setupUi(self)
        self.Show_pswd.toggled.connect(lambda : self.checked_password())
        self.connectButton.clicked.connect(lambda: self.login())


    def login(self):

        login = self.loginInput.text()
        password = self.password_input.text()
        db = MyDBTest()

        X = ("SELECT *  from admin where nomadmin = %s AND password= %s ")
        data = (login, password)
        db.cursor.execute(X, data)

        result = db.cursor.fetchall()

        if result:
            for i in result:
                self.central_widget.setCurrentWidget(self.central_widget.setCurrentWidget(self.landingpage))
                break

        else:
            print("error")


    def checked_password(self):
        if self.Show_pswd.isChecked():
            self.password_input.setEchoMode(0)
        else:
            self.password_input.setEchoMode(2)