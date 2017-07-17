import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import uic

#importamos el archivo
import subvent


class Principal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('conexion.ui', self)

        self.boton.clicked.connect(self.invocar)
        self.Sub = subvent.Subvent()

    def invocar(self):
        self.Sub.exec_()

app = QApplication(sys.argv)
ventana = Principal()
ventana.show()
app.exec_()