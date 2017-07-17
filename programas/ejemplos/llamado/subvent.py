from PyQt5.QtWidgets import QDialog
from PyQt5 import uic


class Subvent(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('ventana.ui', self)

        self.boton.clicked.connect(self.ocultar)

    def ocultar(self):
        self.linea.setEnabled(False)