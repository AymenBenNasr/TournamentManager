from datetime import *

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from dbConnection import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

from matchPage.match import *

class matchWid(QWidget, Ui_Form):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=None)
        self.setupUi(self)