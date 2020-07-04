from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from entraineurPage.entraineur import *
from dbConnection import *


class entraineur(QWidget, Ui_entraineur):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=None)
        self.setupUi(self)


        # cherche Entraineur
        def chercheEntraineur(self):
            db = MyDBTest()
            db.cursor.execute("SELECT * FROM Entraineur where Nom like '" + self.iu.txtRechEntr.text() + "%'")
            myresult = db.cursor.fetchall()
            self.iu.listEntraineur.clear()
            y = 0
            for x in myresult:
                item = QtWidgets.QListWidgetItem()
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap(x[7]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(icon4)
                self.iu.listEntraineur.addItem(item)
                item = self.iu.listEntraineur.item(y)
                item.setText(str(x[1] + " " + x[2]))
                y = y + 1

        # chargement Liste Des Entraineur
    def chargementListeEntraineur(self):
            # db = MyDBTest()
            # db.cursor.execute("SELECT trainername FROM trainer")
            # myresult = db.cursor.fetchall()
            # self.
            # for x in myresult:
            #     item = QtWidgets.QListWidgetItem()
            #     icon = QtGui.QIcon()
            #     icon.addPixmap(QtGui.QPixmap(x[7]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            #     item.setIcon(icon)
            #     self.iu.listEntraineur.addItem(item)
        db = MyDBTest()
        db.cursor.execute("SELECT trainerName from trainer ")
        result = db.cursor.fetchall()
        self.listEntraineur.clear()
        for i in result:
            self.listEntraineur.addItem("%s" % i)
