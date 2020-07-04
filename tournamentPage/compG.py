from datetime import *

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from dbConnection import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

from tournamentPage.comp import *

class tournamentWid(QWidget, Ui_Compition_2):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=None)
        self.setupUi(self)

        self.btnAjoutCom.clicked.connect(lambda: self.AjoutComp.setGeometry(QtCore.QRect(0, 0, 1111, 611)))
        self.btnEnregComp.clicked.connect(self.validateComp)
        self.btnAnnuleComp.clicked.connect(lambda: self.AjoutComp.setGeometry(QtCore.QRect(0, 700, 1111, 611)))
        # self.btnModifCom.clicked.connect(lambda: self.ModifComp.setGeometry(QtCore.QRect(0, 0, 1111, 611)))
        self.btnAnnuleModifComp.clicked.connect(lambda: self.ModifComp.setGeometry(QtCore.QRect(0, 700, 1111, 611)))
        self.btnSuppCom.clicked.connect(lambda: self.SupprimerComp.setGeometry(QtCore.QRect(0, 0, 1111, 611)))
        self.btnAnnulerSuppComp.clicked.connect(lambda: self.SupprimerComp.setGeometry(QtCore.QRect(0, 700, 1111, 611)))

        self.listCompet.itemClicked.connect(self.display)

        self.btnModifCom.clicked.connect(self.loadUpdate)
        self.btnEnregModifComp.clicked.connect(self.update)
        self.btnEnregComp.clicked.connect(self.addcomp)
        self.btnEnregSuppComp.clicked.connect(self.suppComp)

    def loadTourList(self):

        db = MyDBTest()
        db.cursor.execute("SELECT tounamentName from tournaments ")
        result = db.cursor.fetchall()
        for i in result:
                self.listCompet.addItem("%s" % i)

    def show_popupID(self):
        msg = QMessageBox()
        msg.setWindowTitle("ERROR")
        msg.setText("Veuillez verifier l'identifiant !")
        msg.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    def show_popupNom(self):
        msg1 = QMessageBox()
        msg1.setWindowTitle("ERROR")
        msg1.setText("Veuillez verifier le nom !")
        msg1.setIcon(QMessageBox.Warning)
        msg1.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        msg1.exec_()

    def show_popupLocal(self , error):
        msg = QMessageBox()
        msg.resize(400,100)

        msg.setWindowTitle("ERROR")
        # msg.setText("Le champ local ne doit pas être vide !")
        msg.setText(error)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        msg.exec_()
    def validateComp(self):


        if self.ajouNomComp.text() == "" or self.modifNomComp.text()== "":
            self.show_popupLocal("nom vide")
        else:
            print("DB  comp")

    def display(self , selectedItem):
        item = selectedItem.text()
        db = MyDBTest()

        req = ("select * from tournaments where tounamentName = %s ")
        db.cursor.execute(req , (item,))
        result = db.cursor.fetchall()
        for row in result:

            self.IdCompFiche.setText("%s" % row[0])
            self.NomCompFiche.setText("%s" % row[1])
            self.datedebFiche.setText("%s" % row[2] )
            self.datefinFiche.setText("%s" % row[3])
            self.labelPremiPrix.setText("%s" % row[4])
            self.labelDeuxPrix.setText("%s" % row[5])
            self.labelTroiPrix.setText("%s" % row[6])

    def loadUpdate(self):
            if(self.listCompet.currentItem()):
                self.ModifComp.setGeometry(QtCore.QRect(0, 0, 1111, 611))
                id = self.modifIdComp
                nom = self.modifNomComp
                dateDeb =self.modifDateDebComp
                dateFin = self.modifDateFinComp
                first = self.ModifPremiPrix
                second = self.ModifDeuxPrix
                third = self.ModifTroisPrix

                id.setText(self.IdCompFiche.text())
                nom.setText(self.NomCompFiche.text())

                time_str = self.datedebFiche.text()
                time_object = datetime.strptime(time_str, '%Y-%m-%d').date()
                dateDeb.setDate(time_object)


                dateFin.setDate(datetime.strptime(self.datefinFiche.text(), '%Y-%m-%d').date())

                first.setText(self.labelPremiPrix.text())
                second.setText(self.labelDeuxPrix.text())
                third.setText(self.labelTroiPrix.text())
            else:
                print("select an item ")


    def  update(self):
        id = self.modifIdComp.text()

        nom = self.modifNomComp.text()
        Deb = self.modifDateDebComp.date()
        Fin = self.modifDateFinComp.date()
        first = int(self.ModifPremiPrix.text())
        second = self.ModifDeuxPrix.text()
        third = self.ModifTroisPrix.text()
        db = MyDBTest()
        dateDeb = datetime.strftime(Deb.toPyDate() , '%Y-%m-%d')
        dateFin = datetime.strftime(Fin.toPyDate() , '%Y-%m-%d')
        req = " UPDATE tournaments SET tounamentName = %s , tournamentStartDate = %s , tournamentEndDate = %s , firstPrize = %s  , secondPrise = %s , thirdPrize = %s where idTour = %s"

        data = (nom , dateDeb , dateFin , first , second , third ,id)
        db.cursor.execute(req , data)
        db.db.commit()
        print("updated")

    def addcomp(self):
            self.AjoutComp.setGeometry(QtCore.QRect(0, 700, 1111, 611))
            id = self.ajouIdCom.text()
            nom = self.ajouNomComp.text()
            Deb = self.ajouDateDebComp.date()
            Fin = self.ajouDateFinComp.date()
            first = self.ajouPrixPrem.text()
            second = self.ajouPrixDeux.text()
            third = self.ajouPrixTrois.text()

            dateDeb = datetime.strftime(Deb.toPyDate(), '%Y-%m-%d')
            dateFin = datetime.strftime(Fin.toPyDate(), '%Y-%m-%d')
            db= MyDBTest()
            req = "INSERT INTO tournaments (tounamentName,tournamentStartDate ,  tournamentEndDate , firstPrize , secondPrise , thirdPrize ) VALUES (%s ,%s ,%s ,%s ,%s ,%s )"
            data = (nom, dateDeb, dateFin, first, second, third)
            db.cursor.execute(req , data)
            db.db.commit()
            self.listCompet.clear()
            self.loadTourList()

    def suppComp(self):
        if (self.listCompet.currentItem()):
            id = self.IdCompFiche.text()
            bd = MyDBTest()
            req = " DELETE FROM tournaments WHERE idTour = %s"
            bd.cursor.execute(req , (id,))
            bd.db.commit()
            self.listCompet.clear()
            self.loadTourList()
            self.SupprimerComp.setGeometry(QtCore.QRect(0, 0, 0, 611))
        else:
            print("select an item ")


