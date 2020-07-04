# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_home(object):
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(1100, 600)
        home.setStyleSheet("background-color : #2d2d2d;\n"
"color : #b5b5b5")
        self.Acceuil = QtWidgets.QWidget(home)
        self.Acceuil.setEnabled(True)
        self.Acceuil.setGeometry(QtCore.QRect(0, 0, 1100, 600))
        self.Acceuil.setStyleSheet("border-style:hidden hidden hidden groove")
        self.Acceuil.setObjectName("Acceuil")
        self.label = QtWidgets.QLabel(self.Acceuil)
        self.label.setGeometry(QtCore.QRect(59, 26, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnEntraineur = QtWidgets.QToolButton(self.Acceuil)
        self.btnEntraineur.setGeometry(QtCore.QRect(820, 340, 241, 191))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnEntraineur.setFont(font)
        self.btnEntraineur.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEntraineur.setStyleSheet("QToolButton{\n"
" background-color : white;\n"
"}\n"
"QToolButton:checked,QToolButton:pressed{\n"
" background-color : green;\n"
"}\n"
"QToolButton:hover{\n"
" background-color :rgb(67, 147, 83)\n"
"\n"
"}")
        self.btnEntraineur.setObjectName("btnEntraineur")
        self.btnEquipes = QtWidgets.QToolButton(self.Acceuil)
        self.btnEquipes.setGeometry(QtCore.QRect(300, 340, 241, 191))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnEquipes.setFont(font)
        self.btnEquipes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEquipes.setStyleSheet("QToolButton{\n"
" background-color : white;\n"
"}\n"
"QToolButton:checked,QToolButton:pressed{\n"
" background-color : green;\n"
"}\n"
"QToolButton:hover{\n"
" background-color :rgb(67, 147, 83)\n"
"\n"
"}")
        self.btnEquipes.setObjectName("btnEquipes")
        self.btnComp = QtWidgets.QToolButton(self.Acceuil)
        self.btnComp.setGeometry(QtCore.QRect(560, 130, 241, 191))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnComp.setFont(font)
        self.btnComp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnComp.setStyleSheet("QToolButton{\n"
" background-color : white;\n"
"}\n"
"QToolButton:checked,QToolButton:pressed{\n"
" background-color : green;\n"
"}\n"
"QToolButton:hover{\n"
" background-color :rgb(67, 147, 83)\n"
"\n"
"}")
        self.btnComp.setObjectName("btnComp")
        self.btnStat = QtWidgets.QToolButton(self.Acceuil)
        self.btnStat.setGeometry(QtCore.QRect(820, 130, 241, 191))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnStat.setFont(font)
        self.btnStat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStat.setStyleSheet("QToolButton{\n"
" background-color : white;\n"
"}\n"
"QToolButton:checked,QToolButton:pressed{\n"
" background-color : green;\n"
"}\n"
"QToolButton:hover{\n"
" background-color :rgb(67, 147, 83)\n"
"\n"
"}")
        self.btnStat.setObjectName("btnStat")
        self.btnArbitres = QtWidgets.QToolButton(self.Acceuil)
        self.btnArbitres.setGeometry(QtCore.QRect(560, 340, 241, 191))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnArbitres.setFont(font)
        self.btnArbitres.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnArbitres.setStyleSheet("QToolButton{\n"
" background-color : white;\n"
"}\n"
"QToolButton:checked,QToolButton:pressed{\n"
" background-color : green;\n"
"}\n"
"QToolButton:hover{\n"
" background-color :rgb(67, 147, 83)\n"
"\n"
"}")
        self.btnArbitres.setObjectName("btnArbitres")
        self.btnMatch = QtWidgets.QToolButton(self.Acceuil)
        self.btnMatch.setGeometry(QtCore.QRect(300, 130, 241, 191))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnMatch.setFont(font)
        self.btnMatch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMatch.setStyleSheet("QToolButton{\n"
" background-color : white;\n"
"}\n"
"QToolButton:checked,QToolButton:pressed{\n"
" background-color : green;\n"
"}\n"
"QToolButton:hover{\n"
" background-color :rgb(67, 147, 83)\n"
"\n"
"}")
        self.btnMatch.setObjectName("btnMatch")
        self.label_3 = QtWidgets.QLabel(self.Acceuil)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 30, 30))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/aymen/PycharmProjects/lone\homePage/acceuil.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.btnProfile = QtWidgets.QToolButton(self.Acceuil)
        self.btnProfile.setGeometry(QtCore.QRect(940, 30, 21, 21))
        self.btnProfile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProfile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProfile.setIcon(icon)
        self.btnProfile.setIconSize(QtCore.QSize(30, 30))
        self.btnProfile.setObjectName("btnProfile")
        self.toolButton_4 = QtWidgets.QToolButton(self.Acceuil)
        self.toolButton_4.setGeometry(QtCore.QRect(990, 30, 21, 21))
        self.toolButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("reglage (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon1)
        self.toolButton_4.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_4.setObjectName("toolButton_4")
        self.btnClose = QtWidgets.QToolButton(self.Acceuil)
        self.btnClose.setGeometry(QtCore.QRect(1040, 30, 21, 21))
        self.btnClose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/aymen/PycharmProjects/lone/homePage/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon2)
        self.btnClose.setIconSize(QtCore.QSize(30, 30))
        self.btnClose.setObjectName("btnClose")
        self.btnJoueurs = QtWidgets.QToolButton(self.Acceuil)
        self.btnJoueurs.setGeometry(QtCore.QRect(40, 340, 241, 191))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnJoueurs.setFont(font)
        self.btnJoueurs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnJoueurs.setStyleSheet("QToolButton{\n"
" background-color : white;\n"
"}\n"
"QToolButton:checked,QToolButton:pressed{\n"
" background-color : green;\n"
"}\n"
"QToolButton:hover{\n"
" background-color :rgb(67, 147, 83)\n"
"\n"
"}")
        self.btnJoueurs.setObjectName("btnJoueurs")
        self.label_2 = QtWidgets.QLabel(self.Acceuil)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 231, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../projetQt/img/cp.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "Form"))
        self.label.setText(_translate("home", "Acceuil"))
        self.btnEntraineur.setText(_translate("home", "Entraineurs"))
        self.btnEquipes.setText(_translate("home", "Equipes"))
        self.btnComp.setText(_translate("home", "Compétition"))
        self.btnStat.setText(_translate("home", "Statistiques"))
        self.btnArbitres.setText(_translate("home", "Arbitres"))
        self.btnMatch.setText(_translate("home", "Matchs"))
        self.toolButton_4.setText(_translate("home", "..."))
        self.btnClose.setText(_translate("home", "..."))
        self.btnJoueurs.setText(_translate("home", "Joueurs"))
