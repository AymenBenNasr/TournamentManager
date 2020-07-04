# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login_Page(object):
    def setupUi(self, Login_Page):
        Login_Page.setObjectName("Login_Page")
        Login_Page.resize(1100, 600)
        Login_Page.setStyleSheet("QLineEdit{\n"
"border-style:hidden hidden hidden solid;border-bottom : 1px solid;\n"
"border-color:#b5b5b5;\n"
"color:white;\n"
"}\n"
"QLineEdit:focus{\n"
"border-bottom : 2px solid;\n"
"border-color:#1c77d2;\n"
"}\n"
"")
        self.connectButton = QtWidgets.QPushButton(Login_Page)
        self.connectButton.setGeometry(QtCore.QRect(420, 460, 300, 35))
        self.connectButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.connectButton.setStyleSheet("background-color:#1c77d2;color:white;font-size: 15px;")
        self.connectButton.setObjectName("connectButton")
        self.forgetPswd = QtWidgets.QPushButton(Login_Page)
        self.forgetPswd.setGeometry(QtCore.QRect(500, 520, 151, 31))
        self.forgetPswd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgetPswd.setStyleSheet("border:hidden;\n"
"color : rgb(25,118,220);\n"
"font-family: Arial, Helvetica, sans-serif;\n"
"font-size: 15pxm")
        self.forgetPswd.setObjectName("forgetPswd")
        self.Login_Label = QtWidgets.QLabel(Login_Page)
        self.Login_Label.setGeometry(QtCore.QRect(150, 265, 47, 21))
        self.Login_Label.setStyleSheet("font-size:15px")
        self.Login_Label.setObjectName("Login_Label")
        self.pswd_label = QtWidgets.QLabel(Login_Page)
        self.pswd_label.setGeometry(QtCore.QRect(150, 350, 91, 16))
        self.pswd_label.setStyleSheet("font-size:15px")
        self.pswd_label.setObjectName("pswd_label")
        self.Show_pswd = QtWidgets.QCheckBox(Login_Page)
        self.Show_pswd.setGeometry(QtCore.QRect(150, 410, 191, 17))
        self.Show_pswd.setStyleSheet("font-size:15px")
        self.Show_pswd.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Show_pswd.setObjectName("Show_pswd")
        self.loginIcon = QtWidgets.QLabel(Login_Page)
        self.loginIcon.setGeometry(QtCore.QRect(510, 50, 121, 121))
        self.loginIcon.setText("")
        self.loginIcon.setTextFormat(QtCore.Qt.AutoText)
        self.loginIcon.setPixmap(QtGui.QPixmap("login.png"))
        self.loginIcon.setObjectName("loginIcon")
        self.loginInput = QtWidgets.QLineEdit(Login_Page)
        self.loginInput.setGeometry(QtCore.QRect(150, 289, 811, 31))
        self.loginInput.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.loginInput.setObjectName("loginInput")
        self.password_input = QtWidgets.QLineEdit(Login_Page)
        self.password_input.setGeometry(QtCore.QRect(150, 370, 811, 31))
        self.password_input.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")

        self.retranslateUi(Login_Page)
        QtCore.QMetaObject.connectSlotsByName(Login_Page)

    def retranslateUi(self, Login_Page):
        _translate = QtCore.QCoreApplication.translate
        Login_Page.setWindowTitle(_translate("Login_Page", "Form"))
        self.connectButton.setText(_translate("Login_Page", "Se Connecter"))
        self.forgetPswd.setText(_translate("Login_Page", "Mot de passe oublié  ? "))
        self.Login_Label.setText(_translate("Login_Page", "Login"))
        self.pswd_label.setText(_translate("Login_Page", "Mot de passe"))
        self.Show_pswd.setText(_translate("Login_Page", "Afficher le mot de passe"))
        self.loginInput.setPlaceholderText(_translate("Login_Page", "login"))
        self.password_input.setPlaceholderText(_translate("Login_Page", "moot de passe"))
