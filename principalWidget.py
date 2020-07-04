from PyQt5.QtWidgets import QStackedWidget


class centralWidget(QStackedWidget):
    def __init__(self, parent= None):

        QStackedWidget.__init__(self , parent)
        self.central_widget = QStackedWidget()
        self.central_widget.resize(1100,600)
