# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'match.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1016, 600)
        Form.setStyleSheet("background-color : #2d2d2d;\n"
"color : #b5b5b5")
        self.Match = QtWidgets.QWidget(Form)
        self.Match.setEnabled(True)
        self.Match.setGeometry(QtCore.QRect(0, 0, 1101, 601))
        self.Match.setStyleSheet("")
        self.Match.setObjectName("Match")
        self.label_158 = QtWidgets.QLabel(self.Match)
        self.label_158.setGeometry(QtCore.QRect(75, 40, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(36)
        self.label_158.setFont(font)
        self.label_158.setObjectName("label_158")
        self.btnRetour_7 = QtWidgets.QToolButton(self.Match)
        self.btnRetour_7.setGeometry(QtCore.QRect(20, 550, 41, 30))
        self.btnRetour_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRetour_7.setStyleSheet("border:none")
        self.btnRetour_7.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("retour.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRetour_7.setIcon(icon)
        self.btnRetour_7.setIconSize(QtCore.QSize(30, 30))
        self.btnRetour_7.setObjectName("btnRetour_7")
        self.label_240 = QtWidgets.QLabel(self.Match)
        self.label_240.setGeometry(QtCore.QRect(25, 40, 40, 40))
        self.label_240.setText("")
        self.label_240.setPixmap(QtGui.QPixmap("award (1).png"))
        self.label_240.setScaledContents(True)
        self.label_240.setObjectName("label_240")
        self.AjoutMatch = QtWidgets.QWidget(self.Match)
        self.AjoutMatch.setGeometry(QtCore.QRect(0, 700, 1111, 611))
        self.AjoutMatch.setStyleSheet("background-color:rgba(0,0,0,0.7)")
        self.AjoutMatch.setObjectName("AjoutMatch")
        self.ajouterMatch = QtWidgets.QWidget(self.AjoutMatch)
        self.ajouterMatch.setGeometry(QtCore.QRect(60, 80, 871, 421))
        self.ajouterMatch.setStyleSheet("background-color : #2d2d2d;\n"
"border-radius:20px\n"
"")
        self.ajouterMatch.setObjectName("ajouterMatch")
        self.label_241 = QtWidgets.QLabel(self.ajouterMatch)
        self.label_241.setGeometry(QtCore.QRect(50, 23, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(24)
        self.label_241.setFont(font)
        self.label_241.setObjectName("label_241")
        self.label_242 = QtWidgets.QLabel(self.ajouterMatch)
        self.label_242.setGeometry(QtCore.QRect(13, 28, 31, 31))
        self.label_242.setText("")
        self.label_242.setPixmap(QtGui.QPixmap("add.png"))
        self.label_242.setScaledContents(True)
        self.label_242.setObjectName("label_242")
        self.Prop = QtWidgets.QFrame(self.ajouterMatch)
        self.Prop.setGeometry(QtCore.QRect(20, 120, 831, 201))
        self.Prop.setStyleSheet("border : 1px groove;border-color:#b5b5b5;color:white")
        self.Prop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Prop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Prop.setObjectName("Prop")
        self.logoComp = QtWidgets.QLabel(self.Prop)
        self.logoComp.setGeometry(QtCore.QRect(40, 10, 40, 40))
        self.logoComp.setStyleSheet("border : 0px")
        self.logoComp.setText("")
        self.logoComp.setPixmap(QtGui.QPixmap("award (1).png"))
        self.logoComp.setScaledContents(True)
        self.logoComp.setObjectName("logoComp")
        self.Score = QtWidgets.QWidget(self.Prop)
        self.Score.setGeometry(QtCore.QRect(390, 54, 121, 31))
        self.Score.setObjectName("Score")
        self.line = QtWidgets.QFrame(self.Prop)
        self.line.setGeometry(QtCore.QRect(450, 54, 3, 30))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.Prop)
        self.line_2.setGeometry(QtCore.QRect(160, 110, 600, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Equipe1 = QtWidgets.QLineEdit(self.Prop)
        self.Equipe1.setGeometry(QtCore.QRect(260, 54, 111, 31))
        self.Equipe1.setStyleSheet("border:1px solid gray")
        self.Equipe1.setText("")
        self.Equipe1.setObjectName("Equipe1")
        self.Equipe2 = QtWidgets.QLineEdit(self.Prop)
        self.Equipe2.setGeometry(QtCore.QRect(520, 54, 111, 31))
        self.Equipe2.setStyleSheet("border:1px solid gray")
        self.Equipe2.setText("")
        self.Equipe2.setObjectName("Equipe2")
        self.CompMatch = QtWidgets.QLineEdit(self.Prop)
        self.CompMatch.setGeometry(QtCore.QRect(20, 54, 81, 31))
        self.CompMatch.setStyleSheet("border:1px solid gray")
        self.CompMatch.setText("")
        self.CompMatch.setObjectName("CompMatch")
        self.logoEquipe1 = QtWidgets.QLabel(self.Prop)
        self.logoEquipe1.setGeometry(QtCore.QRect(210, 50, 40, 40))
        self.logoEquipe1.setStyleSheet("border : 0px")
        self.logoEquipe1.setText("")
        self.logoEquipe1.setPixmap(QtGui.QPixmap("addLogo.png"))
        self.logoEquipe1.setScaledContents(True)
        self.logoEquipe1.setObjectName("logoEquipe1")
        self.Juge = QtWidgets.QLineEdit(self.Prop)
        self.Juge.setGeometry(QtCore.QRect(170, 130, 111, 31))
        self.Juge.setStyleSheet("border:1px solid gray")
        self.Juge.setText("")
        self.Juge.setDragEnabled(False)
        self.Juge.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Juge.setObjectName("Juge")
        self.chaineTV = QtWidgets.QLineEdit(self.Prop)
        self.chaineTV.setGeometry(QtCore.QRect(290, 130, 111, 31))
        self.chaineTV.setStyleSheet("border:1px solid gray")
        self.chaineTV.setText("")
        self.chaineTV.setObjectName("chaineTV")
        self.commentateur = QtWidgets.QLineEdit(self.Prop)
        self.commentateur.setGeometry(QtCore.QRect(410, 130, 111, 31))
        self.commentateur.setStyleSheet("border:1px solid gray")
        self.commentateur.setText("")
        self.commentateur.setObjectName("commentateur")
        self.logoEquipe2 = QtWidgets.QLabel(self.Prop)
        self.logoEquipe2.setGeometry(QtCore.QRect(640, 50, 40, 40))
        self.logoEquipe2.setStyleSheet("border : 0px")
        self.logoEquipe2.setText("")
        self.logoEquipe2.setPixmap(QtGui.QPixmap("addLogo.png"))
        self.logoEquipe2.setScaledContents(True)
        self.logoEquipe2.setObjectName("logoEquipe2")
        self.Stade = QtWidgets.QLineEdit(self.Prop)
        self.Stade.setGeometry(QtCore.QRect(530, 130, 111, 31))
        self.Stade.setStyleSheet("border:1px solid gray")
        self.Stade.setText("")
        self.Stade.setObjectName("Stade")
        self.dateMatch = QtWidgets.QDateEdit(self.Prop)
        self.dateMatch.setGeometry(QtCore.QRect(650, 130, 111, 31))
        self.dateMatch.setStyleSheet("border:1px solid gray")
        self.dateMatch.setCalendarPopup(True)
        self.dateMatch.setObjectName("dateMatch")
        self.btnAnnulerMatch = QtWidgets.QToolButton(self.ajouterMatch)
        self.btnAnnulerMatch.setGeometry(QtCore.QRect(820, 370, 31, 31))
        self.btnAnnulerMatch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAnnulerMatch.setIcon(icon1)
        self.btnAnnulerMatch.setIconSize(QtCore.QSize(30, 30))
        self.btnAnnulerMatch.setObjectName("btnAnnulerMatch")
        self.btnEnregSuppComp = QtWidgets.QToolButton(self.ajouterMatch)
        self.btnEnregSuppComp.setGeometry(QtCore.QRect(780, 370, 31, 31))
        self.btnEnregSuppComp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEnregSuppComp.setIcon(icon2)
        self.btnEnregSuppComp.setIconSize(QtCore.QSize(30, 30))
        self.btnEnregSuppComp.setObjectName("btnEnregSuppComp")
        self.ModifMatch = QtWidgets.QWidget(self.Match)
        self.ModifMatch.setGeometry(QtCore.QRect(0, 700, 1111, 611))
        self.ModifMatch.setStyleSheet("background-color:rgba(0,0,0,0.7)")
        self.ModifMatch.setObjectName("ModifMatch")
        self.modifierMatch = QtWidgets.QWidget(self.ModifMatch)
        self.modifierMatch.setGeometry(QtCore.QRect(80, 130, 871, 421))
        self.modifierMatch.setStyleSheet("background-color : #2d2d2d;\n"
"border-radius:20px\n"
"")
        self.modifierMatch.setObjectName("modifierMatch")
        self.label_243 = QtWidgets.QLabel(self.modifierMatch)
        self.label_243.setGeometry(QtCore.QRect(50, 23, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(24)
        self.label_243.setFont(font)
        self.label_243.setObjectName("label_243")
        self.label_247 = QtWidgets.QLabel(self.modifierMatch)
        self.label_247.setGeometry(QtCore.QRect(29, 290, 101, 16))
        self.label_247.setObjectName("label_247")
        self.dateMatchModif = QtWidgets.QDateEdit(self.modifierMatch)
        self.dateMatchModif.setGeometry(QtCore.QRect(30, 320, 111, 31))
        self.dateMatchModif.setStyleSheet("border:1px solid gray")
        self.dateMatchModif.setCalendarPopup(True)
        self.dateMatchModif.setObjectName("dateMatchModif")
        self.Prop_2 = QtWidgets.QFrame(self.modifierMatch)
        self.Prop_2.setGeometry(QtCore.QRect(20, 120, 831, 161))
        self.Prop_2.setStyleSheet("border : 1px groove;border-color:#b5b5b5;color:white")
        self.Prop_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Prop_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Prop_2.setObjectName("Prop_2")
        self.logoComp_2 = QtWidgets.QLabel(self.Prop_2)
        self.logoComp_2.setGeometry(QtCore.QRect(40, 10, 40, 40))
        self.logoComp_2.setStyleSheet("border : 0px")
        self.logoComp_2.setText("")
        self.logoComp_2.setPixmap(QtGui.QPixmap("award (1).png"))
        self.logoComp_2.setScaledContents(True)
        self.logoComp_2.setObjectName("logoComp_2")
        self.logoComment_2 = QtWidgets.QLabel(self.Prop_2)
        self.logoComment_2.setGeometry(QtCore.QRect(430, 100, 40, 40))
        self.logoComment_2.setStyleSheet("border : 0px")
        self.logoComment_2.setText("")
        self.logoComment_2.setPixmap(QtGui.QPixmap("img/mou.png"))
        self.logoComment_2.setScaledContents(True)
        self.logoComment_2.setObjectName("logoComment_2")
        self.logoTv_2 = QtWidgets.QLabel(self.Prop_2)
        self.logoTv_2.setGeometry(QtCore.QRect(260, 100, 61, 41))
        self.logoTv_2.setStyleSheet("border : 0px")
        self.logoTv_2.setText("")
        self.logoTv_2.setPixmap(QtGui.QPixmap("img/tv.png"))
        self.logoTv_2.setScaledContents(True)
        self.logoTv_2.setObjectName("logoTv_2")
        self.logoJuge_2 = QtWidgets.QLabel(self.Prop_2)
        self.logoJuge_2.setGeometry(QtCore.QRect(110, 100, 40, 40))
        self.logoJuge_2.setStyleSheet("border : 0px")
        self.logoJuge_2.setText("")
        self.logoJuge_2.setPixmap(QtGui.QPixmap("img/arb.png"))
        self.logoJuge_2.setScaledContents(True)
        self.logoJuge_2.setObjectName("logoJuge_2")
        self.Score_2 = QtWidgets.QWidget(self.Prop_2)
        self.Score_2.setGeometry(QtCore.QRect(390, 40, 121, 31))
        self.Score_2.setObjectName("Score_2")
        self.line_3 = QtWidgets.QFrame(self.Prop_2)
        self.line_3.setGeometry(QtCore.QRect(450, 40, 3, 30))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.Prop_2)
        self.line_4.setGeometry(QtCore.QRect(160, 88, 600, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Equipe1_2 = QtWidgets.QLineEdit(self.Prop_2)
        self.Equipe1_2.setGeometry(QtCore.QRect(230, 40, 111, 31))
        self.Equipe1_2.setStyleSheet("border:1px solid gray")
        self.Equipe1_2.setText("")
        self.Equipe1_2.setObjectName("Equipe1_2")
        self.Equipe2_2 = QtWidgets.QLineEdit(self.Prop_2)
        self.Equipe2_2.setGeometry(QtCore.QRect(560, 40, 111, 31))
        self.Equipe2_2.setStyleSheet("border:1px solid gray")
        self.Equipe2_2.setText("")
        self.Equipe2_2.setObjectName("Equipe2_2")
        self.CompMatch_2 = QtWidgets.QLineEdit(self.Prop_2)
        self.CompMatch_2.setGeometry(QtCore.QRect(20, 54, 81, 31))
        self.CompMatch_2.setStyleSheet("border:1px solid gray")
        self.CompMatch_2.setText("")
        self.CompMatch_2.setObjectName("CompMatch_2")
        self.logoEquipe1_2 = QtWidgets.QLabel(self.Prop_2)
        self.logoEquipe1_2.setGeometry(QtCore.QRect(180, 36, 40, 40))
        self.logoEquipe1_2.setStyleSheet("border : 0px")
        self.logoEquipe1_2.setText("")
        self.logoEquipe1_2.setPixmap(QtGui.QPixmap("addLogo.png"))
        self.logoEquipe1_2.setScaledContents(True)
        self.logoEquipe1_2.setObjectName("logoEquipe1_2")
        self.Juge_2 = QtWidgets.QLineEdit(self.Prop_2)
        self.Juge_2.setGeometry(QtCore.QRect(160, 110, 111, 31))
        self.Juge_2.setStyleSheet("border:1px solid gray")
        self.Juge_2.setText("")
        self.Juge_2.setDragEnabled(False)
        self.Juge_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Juge_2.setObjectName("Juge_2")
        self.chaineTV_2 = QtWidgets.QLineEdit(self.Prop_2)
        self.chaineTV_2.setGeometry(QtCore.QRect(310, 110, 111, 31))
        self.chaineTV_2.setStyleSheet("border:1px solid gray")
        self.chaineTV_2.setText("")
        self.chaineTV_2.setObjectName("chaineTV_2")
        self.commentateur_2 = QtWidgets.QLineEdit(self.Prop_2)
        self.commentateur_2.setGeometry(QtCore.QRect(480, 110, 111, 31))
        self.commentateur_2.setStyleSheet("border:1px solid gray")
        self.commentateur_2.setText("")
        self.commentateur_2.setObjectName("commentateur_2")
        self.logoEquipe2_2 = QtWidgets.QLabel(self.Prop_2)
        self.logoEquipe2_2.setGeometry(QtCore.QRect(680, 36, 40, 40))
        self.logoEquipe2_2.setStyleSheet("border : 0px")
        self.logoEquipe2_2.setText("")
        self.logoEquipe2_2.setPixmap(QtGui.QPixmap("addLogo.png"))
        self.logoEquipe2_2.setScaledContents(True)
        self.logoEquipe2_2.setObjectName("logoEquipe2_2")
        self.logoEquipe2_7 = QtWidgets.QLabel(self.Prop_2)
        self.logoEquipe2_7.setGeometry(QtCore.QRect(600, 100, 40, 40))
        self.logoEquipe2_7.setStyleSheet("border : 0px")
        self.logoEquipe2_7.setText("")
        self.logoEquipe2_7.setPixmap(QtGui.QPixmap("pngwing.png"))
        self.logoEquipe2_7.setScaledContents(True)
        self.logoEquipe2_7.setObjectName("logoEquipe2_7")
        self.Stade_2 = QtWidgets.QLineEdit(self.Prop_2)
        self.Stade_2.setGeometry(QtCore.QRect(650, 110, 111, 31))
        self.Stade_2.setStyleSheet("border:1px solid gray")
        self.Stade_2.setText("")
        self.Stade_2.setObjectName("Stade_2")
        self.btnAnnulerModifMatch = QtWidgets.QToolButton(self.modifierMatch)
        self.btnAnnulerModifMatch.setGeometry(QtCore.QRect(820, 370, 31, 31))
        self.btnAnnulerModifMatch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAnnulerModifMatch.setIcon(icon1)
        self.btnAnnulerModifMatch.setIconSize(QtCore.QSize(30, 30))
        self.btnAnnulerModifMatch.setObjectName("btnAnnulerModifMatch")
        self.btnEnregModifMatch = QtWidgets.QToolButton(self.modifierMatch)
        self.btnEnregModifMatch.setGeometry(QtCore.QRect(780, 370, 31, 31))
        self.btnEnregModifMatch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEnregModifMatch.setIcon(icon2)
        self.btnEnregModifMatch.setIconSize(QtCore.QSize(30, 30))
        self.btnEnregModifMatch.setObjectName("btnEnregModifMatch")
        self.label_252 = QtWidgets.QLabel(self.modifierMatch)
        self.label_252.setGeometry(QtCore.QRect(10, 27, 31, 31))
        self.label_252.setText("")
        self.label_252.setPixmap(QtGui.QPixmap("modif.png"))
        self.label_252.setScaledContents(True)
        self.label_252.setObjectName("label_252")
        self.SupprimerMatch = QtWidgets.QWidget(self.Match)
        self.SupprimerMatch.setGeometry(QtCore.QRect(0, 700, 1111, 611))
        self.SupprimerMatch.setStyleSheet("background-color:rgba(0,0,0,0.7)")
        self.SupprimerMatch.setObjectName("SupprimerMatch")
        self.SuppComp = QtWidgets.QWidget(self.SupprimerMatch)
        self.SuppComp.setGeometry(QtCore.QRect(-50, 240, 1131, 141))
        self.SuppComp.setStyleSheet("background-color : #2d2d2d;\n"
"border-radius:20px\n"
"")
        self.SuppComp.setObjectName("SuppComp")
        self.label_215 = QtWidgets.QLabel(self.SuppComp)
        self.label_215.setGeometry(QtCore.QRect(190, 40, 871, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(24)
        self.label_215.setFont(font)
        self.label_215.setObjectName("label_215")
        self.label_216 = QtWidgets.QLabel(self.SuppComp)
        self.label_216.setGeometry(QtCore.QRect(130, 46, 41, 41))
        self.label_216.setText("")
        self.label_216.setPixmap(QtGui.QPixmap("supp.png"))
        self.label_216.setScaledContents(True)
        self.label_216.setObjectName("label_216")
        self.btnAnnulerSuppMatch = QtWidgets.QToolButton(self.SuppComp)
        self.btnAnnulerSuppMatch.setGeometry(QtCore.QRect(640, 100, 31, 31))
        self.btnAnnulerSuppMatch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAnnulerSuppMatch.setIcon(icon1)
        self.btnAnnulerSuppMatch.setIconSize(QtCore.QSize(30, 30))
        self.btnAnnulerSuppMatch.setObjectName("btnAnnulerSuppMatch")
        self.btnEnregSuppMatch = QtWidgets.QToolButton(self.SuppComp)
        self.btnEnregSuppMatch.setGeometry(QtCore.QRect(600, 100, 31, 31))
        self.btnEnregSuppMatch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEnregSuppMatch.setIcon(icon2)
        self.btnEnregSuppMatch.setIconSize(QtCore.QSize(30, 30))
        self.btnEnregSuppMatch.setObjectName("btnEnregSuppMatch")
        self.tableWidget = QtWidgets.QTableWidget(self.Match)
        self.tableWidget.setGeometry(QtCore.QRect(30, 150, 961, 121))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.btnAjoutMatch = QtWidgets.QToolButton(self.Match)
        self.btnAjoutMatch.setGeometry(QtCore.QRect(851, 50, 31, 31))
        self.btnAjoutMatch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAjoutMatch.setStyleSheet("border:none")
        self.btnAjoutMatch.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAjoutMatch.setIcon(icon3)
        self.btnAjoutMatch.setIconSize(QtCore.QSize(30, 30))
        self.btnAjoutMatch.setObjectName("btnAjoutMatch")
        self.btnModifMatch = QtWidgets.QToolButton(self.Match)
        self.btnModifMatch.setGeometry(QtCore.QRect(900, 50, 31, 31))
        self.btnModifMatch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModifMatch.setStyleSheet("border:none")
        self.btnModifMatch.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("modif.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModifMatch.setIcon(icon4)
        self.btnModifMatch.setIconSize(QtCore.QSize(30, 30))
        self.btnModifMatch.setObjectName("btnModifMatch")
        self.btnSuppMatch = QtWidgets.QToolButton(self.Match)
        self.btnSuppMatch.setGeometry(QtCore.QRect(950, 50, 31, 31))
        self.btnSuppMatch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSuppMatch.setStyleSheet("border:none")
        self.btnSuppMatch.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("supp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSuppMatch.setIcon(icon5)
        self.btnSuppMatch.setIconSize(QtCore.QSize(30, 30))
        self.btnSuppMatch.setObjectName("btnSuppMatch")
        self.btnAjoutMatch.raise_()
        self.btnModifMatch.raise_()
        self.btnSuppMatch.raise_()
        self.tableWidget.raise_()
        self.label_158.raise_()
        self.btnRetour_7.raise_()
        self.label_240.raise_()
        self.AjoutMatch.raise_()
        self.ModifMatch.raise_()
        self.SupprimerMatch.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_158.setText(_translate("Form", "Liste Des Matches"))
        self.label_241.setText(_translate("Form", "Nouveaux Match"))
        self.Equipe1.setPlaceholderText(_translate("Form", "Equipe 1"))
        self.Equipe2.setPlaceholderText(_translate("Form", "Equipe 2"))
        self.CompMatch.setPlaceholderText(_translate("Form", "Compétition"))
        self.Juge.setPlaceholderText(_translate("Form", "Juge"))
        self.chaineTV.setPlaceholderText(_translate("Form", "ChaineTV"))
        self.commentateur.setPlaceholderText(_translate("Form", "Commentateur"))
        self.Stade.setPlaceholderText(_translate("Form", "Stade"))
        self.btnAnnulerMatch.setText(_translate("Form", "..."))
        self.btnEnregSuppComp.setText(_translate("Form", "..."))
        self.label_243.setText(_translate("Form", "Modifier Match"))
        self.label_247.setText(_translate("Form", "Date"))
        self.Equipe1_2.setPlaceholderText(_translate("Form", "Equipe 1"))
        self.Equipe2_2.setPlaceholderText(_translate("Form", "Equipe 2"))
        self.CompMatch_2.setPlaceholderText(_translate("Form", "Compétition"))
        self.Juge_2.setPlaceholderText(_translate("Form", "Juge"))
        self.chaineTV_2.setPlaceholderText(_translate("Form", "ChaineTV"))
        self.commentateur_2.setPlaceholderText(_translate("Form", "Commentateur"))
        self.Stade_2.setPlaceholderText(_translate("Form", "Stade"))
        self.btnAnnulerModifMatch.setText(_translate("Form", "..."))
        self.btnEnregModifMatch.setText(_translate("Form", "..."))
        self.label_215.setText(_translate("Form", "Voulez vous vraiment supprimer cet match"))
        self.btnAnnulerSuppMatch.setText(_translate("Form", "..."))
        self.btnEnregSuppMatch.setText(_translate("Form", "..."))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "M1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Compétition"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Equipe 1"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Score E1"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Score E2"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Equipe 2"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Stade"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Commentateur"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Juge"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "TV "))

 # Crud Match
        self.btnAjoutMatch.clicked.connect(lambda:self.AjoutMatch.setGeometry(QtCore.QRect(0, 0, 1111, 611)))
        self.btnAnnulerMatch.clicked.connect(lambda:self.AjoutMatch.setGeometry(QtCore.QRect(0, 700, 1111, 611)))
        self.btnEnregSuppComp.clicked.connect(self.validateMatch)
        self.btnModifMatch.clicked.connect(lambda:self.ModifMatch.setGeometry(QtCore.QRect(0, 0, 1111, 611)))
        self.btnEnregModifMatch.clicked.connect(self.validateMatch)
        self.btnAnnulerModifMatch.clicked.connect(lambda:self.ModifMatch.setGeometry(QtCore.QRect(0, 700, 1111, 611)))
        self.btnSuppMatch.clicked.connect(lambda:self.SupprimerMatch.setGeometry(QtCore.QRect(0, 0, 1111, 611)))
        self.btnAnnulerSuppMatch.clicked.connect(lambda:self.SupprimerMatch.setGeometry(QtCore.QRect(0, 700, 1111, 611)))
 #verification et controle de saisie
    def show_popupMatch(self):
        msg = QMessageBox()
        msg.setWindowTitle("ERROR")
        msg.setText("Veillez remplir tous les champs !")
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        msg.exec_()

    def validateMatch(self):

        if self.Equipe1.text() == "" or self.Equipe1_2.text()== "":
            self.show_popupMatch()
        elif self.Equipe2.text() == "" or self.Equipe2_2.text()== "":
            self.show_popupMatch()
        else:
            print("DB  Match")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
