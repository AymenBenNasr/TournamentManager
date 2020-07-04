from datetime import *

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from dbConnection import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

from teamPage.equipe import *

class statWid(QWidget, Ui_widget):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=None)
        self.setupUi(self)