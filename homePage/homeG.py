from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from homePage.home import *
from tournamentPage.compG import *
from teamPage.teamG import *
from statPage.statG import *
from matchPage.matchG import *
from entraineurPage.entraineurG import *


class homeWid(QWidget,Ui_home):
    clicked = pyqtSignal()

    def __init__(self, central_widget , parent=None):
        QWidget.__init__(self, parent=None)
        self.setupUi(self)

        self.btnClose.clicked.connect(lambda : self.close())

        self.entraineur = entraineur()
        self.tournament = tournamentWid()
        self.teams = teamWid()
        self.stats = statWid()
        self.match = matchWid()
        central_widget.addWidget(self.tournament)
        central_widget.addWidget(self.teams)
        central_widget.addWidget(self.stats)
        central_widget.addWidget(self.match)
        central_widget.addWidget(self.entraineur)



        self.btnComp.clicked.connect(lambda :central_widget.setCurrentWidget(self.tournament))

        self.btnComp.clicked.connect(lambda: self.tournament.listCompet.clear())
        self.btnComp.clicked.connect(lambda: self.tournament.loadTourList())
        self.tournament.btnRetourCom.clicked.connect(lambda :central_widget.setCurrentWidget(self))

        self.btnEquipes.clicked.connect(lambda: central_widget.setCurrentWidget(self.teams))
        self.btnStat.clicked.connect(lambda: central_widget.setCurrentWidget(self.stats))
        self.btnMatch.clicked.connect(lambda : central_widget.setCurrentWidget(self.match))
        self.btnEntraineur.clicked.connect(lambda: central_widget.setCurrentWidget(self.entraineur))
        self.btnEntraineur.clicked.connect(lambda: self.entraineur.chargementListeEntraineur())

