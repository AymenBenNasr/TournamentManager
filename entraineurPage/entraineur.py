# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entraineur.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_entraineur(object):
    def setupUi(self, entraineur):
        entraineur.setObjectName("entraineur")
        entraineur.resize(1100, 599)
        entraineur.setStyleSheet("background-color : #2d2d2d;\n"
"color : #b5b5b5")
        self.Entreneur = QtWidgets.QWidget(entraineur)
        self.Entreneur.setEnabled(True)
        self.Entreneur.setGeometry(QtCore.QRect(0, 0, 1101, 601))
        self.Entreneur.setStyleSheet("")
        self.Entreneur.setObjectName("Entreneur")
        self.listEntraineur = QtWidgets.QListWidget(self.Entreneur)
        self.listEntraineur.setGeometry(QtCore.QRect(50, 150, 441, 391))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.listEntraineur.setFont(font)
        self.listEntraineur.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listEntraineur.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listEntraineur.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listEntraineur.setAutoScrollMargin(16)
        self.listEntraineur.setIconSize(QtCore.QSize(30, 30))
        self.listEntraineur.setModelColumn(0)
        self.listEntraineur.setObjectName("listEntraineur")
        self.label_10 = QtWidgets.QLabel(self.Entreneur)
        self.label_10.setGeometry(QtCore.QRect(75, 40, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(36)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.txtRechEntr = QtWidgets.QLineEdit(self.Entreneur)
        self.txtRechEntr.setGeometry(QtCore.QRect(55, 119, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.txtRechEntr.setFont(font)
        self.txtRechEntr.setStyleSheet("border : 1px groove;border-color:#b5b5b5;color:white")
        self.txtRechEntr.setObjectName("txtRechEntr")
        self.label_11 = QtWidgets.QLabel(self.Entreneur)
        self.label_11.setGeometry(QtCore.QRect(460, 123, 20, 20))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../../../Desktop/mahdi/cherche.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.btnModifEntre = QtWidgets.QToolButton(self.Entreneur)
        self.btnModifEntre.setGeometry(QtCore.QRect(965, 60, 31, 31))
        self.btnModifEntre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModifEntre.setStyleSheet("border:none")
        self.btnModifEntre.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Desktop/mahdi/modif.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModifEntre.setIcon(icon)
        self.btnModifEntre.setIconSize(QtCore.QSize(30, 30))
        self.btnModifEntre.setObjectName("btnModifEntre")
        self.widget_2 = QtWidgets.QWidget(self.Entreneur)
        self.widget_2.setGeometry(QtCore.QRect(545, 130, 511, 451))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 101, 101))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("../../../Desktop/mahdi/user.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.labNomEntre = QtWidgets.QLabel(self.widget_2)
        self.labNomEntre.setGeometry(QtCore.QRect(230, 10, 240, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labNomEntre.setFont(font)
        self.labNomEntre.setStyleSheet("color : white")
        self.labNomEntre.setObjectName("labNomEntre")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 491, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(20, 20, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.labNaisEntre = QtWidgets.QLabel(self.groupBox_2)
        self.labNaisEntre.setGeometry(QtCore.QRect(140, 20, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labNaisEntre.setFont(font)
        self.labNaisEntre.setStyleSheet("color : white")
        self.labNaisEntre.setObjectName("labNaisEntre")
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        self.label_31.setGeometry(QtCore.QRect(270, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.labNatioEntre = QtWidgets.QLabel(self.groupBox_2)
        self.labNatioEntre.setGeometry(QtCore.QRect(350, 20, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labNatioEntre.setFont(font)
        self.labNatioEntre.setStyleSheet("color : white")
        self.labNatioEntre.setObjectName("labNatioEntre")
        self.label_35 = QtWidgets.QLabel(self.groupBox_2)
        self.label_35.setGeometry(QtCore.QRect(20, 50, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.labContratEntre = QtWidgets.QLabel(self.groupBox_2)
        self.labContratEntre.setGeometry(QtCore.QRect(150, 50, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labContratEntre.setFont(font)
        self.labContratEntre.setStyleSheet("color : white")
        self.labContratEntre.setObjectName("labContratEntre")
        self.label_37 = QtWidgets.QLabel(self.groupBox_2)
        self.label_37.setGeometry(QtCore.QRect(20, 80, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.labDebutEntre = QtWidgets.QLabel(self.groupBox_2)
        self.labDebutEntre.setGeometry(QtCore.QRect(100, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labDebutEntre.setFont(font)
        self.labDebutEntre.setStyleSheet("color : white")
        self.labDebutEntre.setObjectName("labDebutEntre")
        self.labFinEntre = QtWidgets.QLabel(self.groupBox_2)
        self.labFinEntre.setGeometry(QtCore.QRect(330, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labFinEntre.setFont(font)
        self.labFinEntre.setStyleSheet("color : white")
        self.labFinEntre.setObjectName("labFinEntre")
        self.label_41 = QtWidgets.QLabel(self.groupBox_2)
        self.label_41.setGeometry(QtCore.QRect(270, 80, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.groupBox_2)
        self.label_42.setGeometry(QtCore.QRect(300, 50, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.labDurEntre = QtWidgets.QLabel(self.groupBox_2)
        self.labDurEntre.setGeometry(QtCore.QRect(350, 50, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labDurEntre.setFont(font)
        self.labDurEntre.setStyleSheet("color : white")
        self.labDurEntre.setObjectName("labDurEntre")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 240, 491, 171))
        self.groupBox_4.setObjectName("groupBox_4")
        self.ListCarrier = QtWidgets.QTableWidget(self.groupBox_4)
        self.ListCarrier.setGeometry(QtCore.QRect(7, 37, 481, 121))
        self.ListCarrier.setStyleSheet("color:white")
        self.ListCarrier.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ListCarrier.setLineWidth(0)
        self.ListCarrier.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ListCarrier.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.ListCarrier.setTextElideMode(QtCore.Qt.ElideNone)
        self.ListCarrier.setGridStyle(QtCore.Qt.NoPen)
        self.ListCarrier.setColumnCount(3)
        self.ListCarrier.setObjectName("ListCarrier")
        self.ListCarrier.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.ListCarrier.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListCarrier.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListCarrier.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Desktop/mahdi/48/Algeria.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.ListCarrier.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListCarrier.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListCarrier.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../Desktop/mahdi/48/Slovakia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.ListCarrier.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListCarrier.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListCarrier.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../Desktop/mahdi/48/Belgium.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.ListCarrier.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListCarrier.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ListCarrier.setItem(2, 2, item)
        self.ListCarrier.horizontalHeader().setVisible(False)
        self.ListCarrier.horizontalHeader().setDefaultSectionSize(156)
        self.ListCarrier.horizontalHeader().setHighlightSections(True)
        self.ListCarrier.verticalHeader().setVisible(False)
        self.ListCarrier.verticalHeader().setDefaultSectionSize(35)
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_20.setObjectName("label_20")
        self.label_33 = QtWidgets.QLabel(self.groupBox_4)
        self.label_33.setGeometry(QtCore.QRect(170, 20, 61, 16))
        self.label_33.setObjectName("label_33")
        self.label_38 = QtWidgets.QLabel(self.groupBox_4)
        self.label_38.setGeometry(QtCore.QRect(330, 20, 47, 13))
        self.label_38.setObjectName("label_38")
        self.label_47 = QtWidgets.QLabel(self.widget_2)
        self.label_47.setGeometry(QtCore.QRect(140, 10, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.labCinEntre = QtWidgets.QLabel(self.widget_2)
        self.labCinEntre.setGeometry(QtCore.QRect(230, 90, 240, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labCinEntre.setFont(font)
        self.labCinEntre.setStyleSheet("color : white")
        self.labCinEntre.setObjectName("labCinEntre")
        self.label_48 = QtWidgets.QLabel(self.widget_2)
        self.label_48.setGeometry(QtCore.QRect(140, 90, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.labPrenomEntre = QtWidgets.QLabel(self.widget_2)
        self.labPrenomEntre.setGeometry(QtCore.QRect(230, 50, 240, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labPrenomEntre.setFont(font)
        self.labPrenomEntre.setStyleSheet("color : white")
        self.labPrenomEntre.setObjectName("labPrenomEntre")
        self.label_49 = QtWidgets.QLabel(self.widget_2)
        self.label_49.setGeometry(QtCore.QRect(140, 50, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.Entreneur)
        self.label_50.setGeometry(QtCore.QRect(555, 110, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.btnRetour_2 = QtWidgets.QToolButton(self.Entreneur)
        self.btnRetour_2.setGeometry(QtCore.QRect(20, 550, 41, 30))
        self.btnRetour_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRetour_2.setStyleSheet("border:none")
        self.btnRetour_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../Desktop/mahdi/retour.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRetour_2.setIcon(icon4)
        self.btnRetour_2.setIconSize(QtCore.QSize(30, 30))
        self.btnRetour_2.setObjectName("btnRetour_2")
        self.btnSupp_2 = QtWidgets.QToolButton(self.Entreneur)
        self.btnSupp_2.setGeometry(QtCore.QRect(1015, 60, 31, 31))
        self.btnSupp_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSupp_2.setStyleSheet("border:none")
        self.btnSupp_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../../Desktop/mahdi/supp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSupp_2.setIcon(icon5)
        self.btnSupp_2.setIconSize(QtCore.QSize(30, 30))
        self.btnSupp_2.setObjectName("btnSupp_2")
        self.btnAjoutEntre = QtWidgets.QToolButton(self.Entreneur)
        self.btnAjoutEntre.setGeometry(QtCore.QRect(915, 60, 31, 31))
        self.btnAjoutEntre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAjoutEntre.setStyleSheet("border:none")
        self.btnAjoutEntre.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../../Desktop/mahdi/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAjoutEntre.setIcon(icon6)
        self.btnAjoutEntre.setIconSize(QtCore.QSize(30, 30))
        self.btnAjoutEntre.setObjectName("btnAjoutEntre")
        self.label_51 = QtWidgets.QLabel(self.Entreneur)
        self.label_51.setGeometry(QtCore.QRect(25, 46, 40, 40))
        self.label_51.setText("")
        self.label_51.setPixmap(QtGui.QPixmap("../../../Desktop/mahdi/entreneur.png"))
        self.label_51.setScaledContents(True)
        self.label_51.setObjectName("label_51")
        self.AjoutEntrain = QtWidgets.QWidget(self.Entreneur)
        self.AjoutEntrain.setGeometry(QtCore.QRect(0, 700, 1111, 611))
        self.AjoutEntrain.setStyleSheet("background-color:rgba(0,0,0,0.7)")
        self.AjoutEntrain.setObjectName("AjoutEntrain")
        self.ajouterEntre = QtWidgets.QWidget(self.AjoutEntrain)
        self.ajouterEntre.setGeometry(QtCore.QRect(210, 70, 681, 461))
        self.ajouterEntre.setStyleSheet("background-color : #2d2d2d;\n"
"border-radius:20px\n"
"")
        self.ajouterEntre.setObjectName("ajouterEntre")
        self.label_43 = QtWidgets.QLabel(self.ajouterEntre)
        self.label_43.setGeometry(QtCore.QRect(50, 20, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(24)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.ajouterEntre)
        self.label_44.setGeometry(QtCore.QRect(13, 16, 31, 31))
        self.label_44.setText("")
        self.label_44.setPixmap(QtGui.QPixmap("../../../Desktop/mahdi/add.png"))
        self.label_44.setScaledContents(True)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.ajouterEntre)
        self.label_45.setGeometry(QtCore.QRect(290, 130, 21, 16))
        self.label_45.setObjectName("label_45")
        self.ajouNomEntre = QtWidgets.QLineEdit(self.ajouterEntre)
        self.ajouNomEntre.setGeometry(QtCore.QRect(292, 150, 291, 31))
        self.ajouNomEntre.setStyleSheet("border:1px solid gray")
        self.ajouNomEntre.setObjectName("ajouNomEntre")
        self.label_46 = QtWidgets.QLabel(self.ajouterEntre)
        self.label_46.setGeometry(QtCore.QRect(290, 70, 31, 16))
        self.label_46.setObjectName("label_46")
        self.ajouCinEntre = QtWidgets.QLineEdit(self.ajouterEntre)
        self.ajouCinEntre.setGeometry(QtCore.QRect(292, 90, 291, 31))
        self.ajouCinEntre.setStyleSheet("border:1px solid gray")
        self.ajouCinEntre.setText("")
        self.ajouCinEntre.setObjectName("ajouCinEntre")
        self.label_52 = QtWidgets.QLabel(self.ajouterEntre)
        self.label_52.setGeometry(QtCore.QRect(290, 190, 41, 16))
        self.label_52.setObjectName("label_52")
        self.ajouPrenomEntre = QtWidgets.QLineEdit(self.ajouterEntre)
        self.ajouPrenomEntre.setGeometry(QtCore.QRect(291, 210, 291, 31))
        self.ajouPrenomEntre.setStyleSheet("border:1px solid gray")
        self.ajouPrenomEntre.setText("")
        self.ajouPrenomEntre.setObjectName("ajouPrenomEntre")
        self.label_53 = QtWidgets.QLabel(self.ajouterEntre)
        self.label_53.setGeometry(QtCore.QRect(29, 280, 101, 16))
        self.label_53.setObjectName("label_53")
        self.ajouNatioEntre = QtWidgets.QLineEdit(self.ajouterEntre)
        self.ajouNatioEntre.setGeometry(QtCore.QRect(360, 300, 291, 31))
        self.ajouNatioEntre.setStyleSheet("border:1px solid gray")
        self.ajouNatioEntre.setText("")
        self.ajouNatioEntre.setObjectName("ajouNatioEntre")
        self.label_54 = QtWidgets.QLabel(self.ajouterEntre)
        self.label_54.setGeometry(QtCore.QRect(360, 280, 71, 16))
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.ajouterEntre)
        self.label_55.setGeometry(QtCore.QRect(30, 340, 71, 16))
        self.label_55.setObjectName("label_55")
        self.ajouEquipeEntre = QtWidgets.QComboBox(self.ajouterEntre)
        self.ajouEquipeEntre.setGeometry(QtCore.QRect(31, 360, 291, 31))
        self.ajouEquipeEntre.setStyleSheet("border:1px solid gray")
        self.ajouEquipeEntre.setObjectName("ajouEquipeEntre")
        self.ajouEquipeEntre.addItem("")
        self.ajouDateDebEntre = QtWidgets.QDateEdit(self.ajouterEntre)
        self.ajouDateDebEntre.setGeometry(QtCore.QRect(360, 360, 121, 31))
        self.ajouDateDebEntre.setStyleSheet("border:1px solid gray")
        self.ajouDateDebEntre.setObjectName("ajouDateDebEntre")
        self.label_57 = QtWidgets.QLabel(self.ajouterEntre)
        self.label_57.setGeometry(QtCore.QRect(360, 340, 61, 16))
        self.label_57.setObjectName("label_57")
        self.ajouDateNaissEntre = QtWidgets.QDateEdit(self.ajouterEntre)
        self.ajouDateNaissEntre.setGeometry(QtCore.QRect(30, 300, 291, 31))
        self.ajouDateNaissEntre.setStyleSheet("border:1px solid gray")
        self.ajouDateNaissEntre.setObjectName("ajouDateNaissEntre")
        self.label_58 = QtWidgets.QLabel(self.ajouterEntre)
        self.label_58.setGeometry(QtCore.QRect(530, 340, 61, 16))
        self.label_58.setObjectName("label_58")
        self.ajouDateFinEntre = QtWidgets.QDateEdit(self.ajouterEntre)
        self.ajouDateFinEntre.setGeometry(QtCore.QRect(530, 360, 121, 31))
        self.ajouDateFinEntre.setStyleSheet("border:1px solid gray")
        self.ajouDateFinEntre.setObjectName("ajouDateFinEntre")
        self.ajoutPhotoEntre = QtWidgets.QLabel(self.ajouterEntre)
        self.ajoutPhotoEntre.setGeometry(QtCore.QRect(90, 80, 151, 161))
        self.ajoutPhotoEntre.setText("")
        self.ajoutPhotoEntre.setPixmap(QtGui.QPixmap("../../../Desktop/mahdi/user.png"))
        self.ajoutPhotoEntre.setScaledContents(True)
        self.ajoutPhotoEntre.setObjectName("ajoutPhotoEntre")
        self.btnUplodEntre = QtWidgets.QToolButton(self.ajouterEntre)
        self.btnUplodEntre.setGeometry(QtCore.QRect(120, 250, 91, 21))
        self.btnUplodEntre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../../Desktop/mahdi/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUplodEntre.setIcon(icon7)
        self.btnUplodEntre.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnUplodEntre.setObjectName("btnUplodEntre")
        self.btnAnnuleEntre = QtWidgets.QToolButton(self.ajouterEntre)
        self.btnAnnuleEntre.setGeometry(QtCore.QRect(570, 420, 31, 31))
        self.btnAnnuleEntre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../../../Downloads/closecircularbutton_79562 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAnnuleEntre.setIcon(icon8)
        self.btnAnnuleEntre.setIconSize(QtCore.QSize(30, 30))
        self.btnAnnuleEntre.setObjectName("btnAnnuleEntre")
        self.btnEnregEntre = QtWidgets.QToolButton(self.ajouterEntre)
        self.btnEnregEntre.setGeometry(QtCore.QRect(620, 420, 31, 31))
        self.btnEnregEntre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../../../Downloads/closecircularbutton_79562 (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEnregEntre.setIcon(icon9)
        self.btnEnregEntre.setIconSize(QtCore.QSize(30, 30))
        self.btnEnregEntre.setObjectName("btnEnregEntre")
        self.ModifEntrain = QtWidgets.QWidget(self.Entreneur)
        self.ModifEntrain.setGeometry(QtCore.QRect(0, 700, 1111, 611))
        self.ModifEntrain.setStyleSheet("background-color:rgba(0,0,0,0.7)")
        self.ModifEntrain.setObjectName("ModifEntrain")
        self.modifEntre = QtWidgets.QWidget(self.ModifEntrain)
        self.modifEntre.setGeometry(QtCore.QRect(210, 70, 681, 461))
        self.modifEntre.setStyleSheet("background-color : #2d2d2d;\n"
"border-radius:20px\n"
"")
        self.modifEntre.setObjectName("modifEntre")
        self.label_56 = QtWidgets.QLabel(self.modifEntre)
        self.label_56.setGeometry(QtCore.QRect(50, 20, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(24)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.label_59 = QtWidgets.QLabel(self.modifEntre)
        self.label_59.setGeometry(QtCore.QRect(13, 16, 31, 31))
        self.label_59.setText("")
        self.label_59.setPixmap(QtGui.QPixmap("../../../Desktop/mahdi/modif.png"))
        self.label_59.setScaledContents(True)
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.modifEntre)
        self.label_60.setGeometry(QtCore.QRect(290, 130, 21, 16))
        self.label_60.setObjectName("label_60")
        self.modifNomEntre = QtWidgets.QLineEdit(self.modifEntre)
        self.modifNomEntre.setGeometry(QtCore.QRect(292, 150, 291, 31))
        self.modifNomEntre.setStyleSheet("border:1px solid gray")
        self.modifNomEntre.setObjectName("modifNomEntre")
        self.label_61 = QtWidgets.QLabel(self.modifEntre)
        self.label_61.setGeometry(QtCore.QRect(290, 70, 31, 16))
        self.label_61.setObjectName("label_61")
        self.modifCinEntre_2 = QtWidgets.QLineEdit(self.modifEntre)
        self.modifCinEntre_2.setGeometry(QtCore.QRect(292, 90, 291, 31))
        self.modifCinEntre_2.setStyleSheet("border:1px solid gray")
        self.modifCinEntre_2.setObjectName("modifCinEntre_2")
        self.label_62 = QtWidgets.QLabel(self.modifEntre)
        self.label_62.setGeometry(QtCore.QRect(290, 190, 41, 16))
        self.label_62.setObjectName("label_62")
        self.modifPrenomEntre = QtWidgets.QLineEdit(self.modifEntre)
        self.modifPrenomEntre.setGeometry(QtCore.QRect(291, 210, 291, 31))
        self.modifPrenomEntre.setStyleSheet("border:1px solid gray")
        self.modifPrenomEntre.setObjectName("modifPrenomEntre")
        self.label_63 = QtWidgets.QLabel(self.modifEntre)
        self.label_63.setGeometry(QtCore.QRect(29, 280, 101, 16))
        self.label_63.setObjectName("label_63")
        self.modifNatioEntre = QtWidgets.QLineEdit(self.modifEntre)
        self.modifNatioEntre.setGeometry(QtCore.QRect(360, 300, 291, 31))
        self.modifNatioEntre.setStyleSheet("border:1px solid gray")
        self.modifNatioEntre.setObjectName("modifNatioEntre")
        self.label_64 = QtWidgets.QLabel(self.modifEntre)
        self.label_64.setGeometry(QtCore.QRect(360, 280, 71, 16))
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.modifEntre)
        self.label_65.setGeometry(QtCore.QRect(30, 340, 71, 16))
        self.label_65.setObjectName("label_65")
        self.modifEquipeEntre = QtWidgets.QComboBox(self.modifEntre)
        self.modifEquipeEntre.setGeometry(QtCore.QRect(31, 360, 291, 31))
        self.modifEquipeEntre.setStyleSheet("border:1px solid gray")
        self.modifEquipeEntre.setObjectName("modifEquipeEntre")
        self.modifEquipeEntre.addItem("")
        self.modifEquipeEntre.addItem(icon1, "")
        self.modifDateDebEntre = QtWidgets.QDateEdit(self.modifEntre)
        self.modifDateDebEntre.setGeometry(QtCore.QRect(360, 360, 121, 31))
        self.modifDateDebEntre.setStyleSheet("border:1px solid gray")
        self.modifDateDebEntre.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 17), QtCore.QTime(0, 0, 0)))
        self.modifDateDebEntre.setObjectName("modifDateDebEntre")
        self.label_66 = QtWidgets.QLabel(self.modifEntre)
        self.label_66.setGeometry(QtCore.QRect(360, 340, 61, 16))
        self.label_66.setObjectName("label_66")
        self.modifDateNaissEntre = QtWidgets.QDateEdit(self.modifEntre)
        self.modifDateNaissEntre.setGeometry(QtCore.QRect(30, 300, 291, 31))
        self.modifDateNaissEntre.setStyleSheet("border:1px solid gray")
        self.modifDateNaissEntre.setDateTime(QtCore.QDateTime(QtCore.QDate(1992, 1, 17), QtCore.QTime(0, 0, 0)))
        self.modifDateNaissEntre.setObjectName("modifDateNaissEntre")
        self.label_67 = QtWidgets.QLabel(self.modifEntre)
        self.label_67.setGeometry(QtCore.QRect(530, 340, 61, 16))
        self.label_67.setObjectName("label_67")
        self.modifDateFinEntre = QtWidgets.QDateEdit(self.modifEntre)
        self.modifDateFinEntre.setGeometry(QtCore.QRect(530, 360, 121, 31))
        self.modifDateFinEntre.setStyleSheet("border:1px solid gray")
        self.modifDateFinEntre.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 17), QtCore.QTime(0, 0, 0)))
        self.modifDateFinEntre.setObjectName("modifDateFinEntre")
        self.modifPhotoEntre = QtWidgets.QLabel(self.modifEntre)
        self.modifPhotoEntre.setGeometry(QtCore.QRect(90, 80, 151, 161))
        self.modifPhotoEntre.setText("")
        self.modifPhotoEntre.setPixmap(QtGui.QPixmap("../../../Desktop/mahdi/user.png"))
        self.modifPhotoEntre.setScaledContents(True)
        self.modifPhotoEntre.setObjectName("modifPhotoEntre")
        self.btnModifUplodEntre = QtWidgets.QToolButton(self.modifEntre)
        self.btnModifUplodEntre.setGeometry(QtCore.QRect(120, 250, 91, 21))
        self.btnModifUplodEntre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModifUplodEntre.setIcon(icon7)
        self.btnModifUplodEntre.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnModifUplodEntre.setObjectName("btnModifUplodEntre")
        self.btnModifAnnuleEntre = QtWidgets.QToolButton(self.modifEntre)
        self.btnModifAnnuleEntre.setGeometry(QtCore.QRect(570, 420, 31, 31))
        self.btnModifAnnuleEntre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModifAnnuleEntre.setIcon(icon8)
        self.btnModifAnnuleEntre.setIconSize(QtCore.QSize(30, 30))
        self.btnModifAnnuleEntre.setObjectName("btnModifAnnuleEntre")
        self.btnModifEnregEntre = QtWidgets.QToolButton(self.modifEntre)
        self.btnModifEnregEntre.setGeometry(QtCore.QRect(620, 420, 31, 31))
        self.btnModifEnregEntre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModifEnregEntre.setIcon(icon9)
        self.btnModifEnregEntre.setIconSize(QtCore.QSize(30, 30))
        self.btnModifEnregEntre.setObjectName("btnModifEnregEntre")
        self.SupprimerEntrain = QtWidgets.QWidget(self.Entreneur)
        self.SupprimerEntrain.setGeometry(QtCore.QRect(0, 700, 1111, 611))
        self.SupprimerEntrain.setStyleSheet("background-color:rgba(0,0,0,0.7)")
        self.SupprimerEntrain.setObjectName("SupprimerEntrain")
        self.ajouterEntre_3 = QtWidgets.QWidget(self.SupprimerEntrain)
        self.ajouterEntre_3.setGeometry(QtCore.QRect(-20, 240, 1131, 141))
        self.ajouterEntre_3.setStyleSheet("background-color : #2d2d2d;\n"
"border-radius:20px\n"
"")
        self.ajouterEntre_3.setObjectName("ajouterEntre_3")
        self.label_78 = QtWidgets.QLabel(self.ajouterEntre_3)
        self.label_78.setGeometry(QtCore.QRect(200, 34, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(24)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.label_79 = QtWidgets.QLabel(self.ajouterEntre_3)
        self.label_79.setGeometry(QtCore.QRect(120, 30, 61, 61))
        self.label_79.setText("")
        self.label_79.setPixmap(QtGui.QPixmap("../../../Desktop/mahdi/supp.png"))
        self.label_79.setScaledContents(True)
        self.label_79.setObjectName("label_79")
        self.btnSuppAnnuleEntre = QtWidgets.QToolButton(self.ajouterEntre_3)
        self.btnSuppAnnuleEntre.setGeometry(QtCore.QRect(940, 100, 31, 31))
        self.btnSuppAnnuleEntre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSuppAnnuleEntre.setIcon(icon8)
        self.btnSuppAnnuleEntre.setIconSize(QtCore.QSize(30, 30))
        self.btnSuppAnnuleEntre.setObjectName("btnSuppAnnuleEntre")
        self.btnSuppEnregEntre = QtWidgets.QToolButton(self.ajouterEntre_3)
        self.btnSuppEnregEntre.setGeometry(QtCore.QRect(990, 100, 31, 31))
        self.btnSuppEnregEntre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSuppEnregEntre.setIcon(icon9)
        self.btnSuppEnregEntre.setIconSize(QtCore.QSize(30, 30))
        self.btnSuppEnregEntre.setObjectName("btnSuppEnregEntre")

        self.retranslateUi(entraineur)
        self.modifEquipeEntre.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(entraineur)

    def retranslateUi(self, entraineur):
        _translate = QtCore.QCoreApplication.translate
        entraineur.setWindowTitle(_translate("entraineur", "Form"))
        self.label_10.setText(_translate("entraineur", "Liste Des Entraineurs"))
        self.txtRechEntr.setPlaceholderText(_translate("entraineur", "Chercher par nom"))
        self.labNomEntre.setText(_translate("entraineur", "Chargui"))
        self.groupBox_2.setTitle(_translate("entraineur", "Coordonné"))
        self.label_29.setText(_translate("entraineur", "Date de Naissance :"))
        self.labNaisEntre.setText(_translate("entraineur", "17/01/1992"))
        self.label_31.setText(_translate("entraineur", "Nationalité :"))
        self.labNatioEntre.setText(_translate("entraineur", "Tunisien"))
        self.label_35.setText(_translate("entraineur", "Contrat Signié avec :"))
        self.labContratEntre.setText(_translate("entraineur", "Algerie"))
        self.label_37.setText(_translate("entraineur", "Date Debut :"))
        self.labDebutEntre.setText(_translate("entraineur", "17/02/2020"))
        self.labFinEntre.setText(_translate("entraineur", "17/01/2023"))
        self.label_41.setText(_translate("entraineur", "Date Fin :"))
        self.label_42.setText(_translate("entraineur", "Durré :"))
        self.labDurEntre.setText(_translate("entraineur", "3 ans"))
        self.groupBox_4.setTitle(_translate("entraineur", "Carrière"))
        item = self.ListCarrier.verticalHeaderItem(0)
        item.setText(_translate("entraineur", "Nouvelle ligne"))
        item = self.ListCarrier.verticalHeaderItem(1)
        item.setText(_translate("entraineur", "Nouvelle ligne"))
        item = self.ListCarrier.verticalHeaderItem(2)
        item.setText(_translate("entraineur", "Nouvelle ligne"))
        __sortingEnabled = self.ListCarrier.isSortingEnabled()
        self.ListCarrier.setSortingEnabled(False)
        item = self.ListCarrier.item(0, 0)
        item.setText(_translate("entraineur", "Algerie"))
        item = self.ListCarrier.item(0, 1)
        item.setText(_translate("entraineur", "17/02/2020"))
        item = self.ListCarrier.item(0, 2)
        item.setText(_translate("entraineur", "17/01/2023"))
        item = self.ListCarrier.item(1, 0)
        item.setText(_translate("entraineur", "Slouvakia"))
        item = self.ListCarrier.item(1, 1)
        item.setText(_translate("entraineur", "01/06/2015"))
        item = self.ListCarrier.item(1, 2)
        item.setText(_translate("entraineur", "30/12/2017"))
        item = self.ListCarrier.item(2, 0)
        item.setText(_translate("entraineur", "Belgium"))
        item = self.ListCarrier.item(2, 1)
        item.setText(_translate("entraineur", "18/05/2010"))
        item = self.ListCarrier.item(2, 2)
        item.setText(_translate("entraineur", "15/05/2015"))
        self.ListCarrier.setSortingEnabled(__sortingEnabled)
        self.label_20.setText(_translate("entraineur", "Equipes"))
        self.label_33.setText(_translate("entraineur", "Date Debut"))
        self.label_38.setText(_translate("entraineur", "Date Fin"))
        self.label_47.setText(_translate("entraineur", "NOM :"))
        self.labCinEntre.setText(_translate("entraineur", "04826640"))
        self.label_48.setText(_translate("entraineur", "CIN :"))
        self.labPrenomEntre.setText(_translate("entraineur", "Mahdi"))
        self.label_49.setText(_translate("entraineur", "PRENOM :"))
        self.label_50.setText(_translate("entraineur", "Fiche Entraineur"))
        self.label_43.setText(_translate("entraineur", "Nouvelle Entraineur"))
        self.label_45.setText(_translate("entraineur", "Nom"))
        self.ajouNomEntre.setPlaceholderText(_translate("entraineur", "Ex : Msekni"))
        self.label_46.setText(_translate("entraineur", "CIN"))
        self.ajouCinEntre.setPlaceholderText(_translate("entraineur", "Ex : 04826640"))
        self.label_52.setText(_translate("entraineur", "Prenom"))
        self.ajouPrenomEntre.setPlaceholderText(_translate("entraineur", "Ex : Youssef"))
        self.label_53.setText(_translate("entraineur", "Date de Naissance"))
        self.ajouNatioEntre.setPlaceholderText(_translate("entraineur", "Ex : Tunisien"))
        self.label_54.setText(_translate("entraineur", "Nationnalité"))
        self.label_55.setText(_translate("entraineur", "Equipe"))
        self.ajouEquipeEntre.setItemText(0, _translate("entraineur", "Selectioner un equipe "))
        self.label_57.setText(_translate("entraineur", "Date Fin"))
        self.label_58.setText(_translate("entraineur", "Date debut"))
        self.btnUplodEntre.setText(_translate("entraineur", " Upload photo"))
        self.btnAnnuleEntre.setText(_translate("entraineur", "..."))
        self.btnEnregEntre.setText(_translate("entraineur", "..."))
        self.label_56.setText(_translate("entraineur", "Modifier Entraineur"))
        self.label_60.setText(_translate("entraineur", "Nom"))
        self.modifNomEntre.setText(_translate("entraineur", "Chargui"))
        self.modifNomEntre.setPlaceholderText(_translate("entraineur", "Ex : Msekni"))
        self.label_61.setText(_translate("entraineur", "CIN"))
        self.modifCinEntre_2.setText(_translate("entraineur", "04826640"))
        self.modifCinEntre_2.setPlaceholderText(_translate("entraineur", "Ex : 04826640"))
        self.label_62.setText(_translate("entraineur", "Prenom"))
        self.modifPrenomEntre.setText(_translate("entraineur", "Mehdi"))
        self.modifPrenomEntre.setPlaceholderText(_translate("entraineur", "Ex : Youssef"))
        self.label_63.setText(_translate("entraineur", "Date de Naissance"))
        self.modifNatioEntre.setText(_translate("entraineur", "Tunisien"))
        self.modifNatioEntre.setPlaceholderText(_translate("entraineur", "Ex : Tunisien"))
        self.label_64.setText(_translate("entraineur", "Nationnalité"))
        self.label_65.setText(_translate("entraineur", "Equipe"))
        self.modifEquipeEntre.setItemText(0, _translate("entraineur", "Selectioner un equipe "))
        self.modifEquipeEntre.setItemText(1, _translate("entraineur", "Algerie"))
        self.label_66.setText(_translate("entraineur", "Date Fin"))
        self.label_67.setText(_translate("entraineur", "Date debut"))
        self.btnModifUplodEntre.setText(_translate("entraineur", " Upload photo"))
        self.btnModifAnnuleEntre.setText(_translate("entraineur", "..."))
        self.btnModifEnregEntre.setText(_translate("entraineur", "..."))
        self.label_78.setText(_translate("entraineur", "Voulez vous vraiment supprimer cette  entraineur ?"))
        self.btnSuppAnnuleEntre.setText(_translate("entraineur", "..."))
        self.btnSuppEnregEntre.setText(_translate("entraineur", "..."))
