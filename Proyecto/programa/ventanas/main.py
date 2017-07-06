import sys, re
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QSplashScreen, QDesktopWidget
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

from clientes import *

class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        x = 900
        y = 600
        self.resize(x,y)
        self.center()  # Centro la pantalla
        self.setMaximumSize(x,y)
        self.setMinimumSize(x,y)
        self.setWindowTitle("Sistema de Turnos PyPET")
        self.boton = QPushButton(self)
        self.boton.setText("CARGAR CLIENTES")
        self.boton.resize(200, 30)
        self.dialogo = Cliente()
        self.boton.clicked.connect(self.abrirDialogo)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
  
    def abrirDialogo(self):
        self.dialogo.exec_()

class Login(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("layout/login.ui", self)
		self.aceptar.clicked.connect(self.ingresar)
		self.cancelar.clicked.connect(self.salir)

	def ingresar(self):
		global ventana
		ventana = Ventana()
		ventana.show()
		login.close()

	def salir(self):
		app.quit()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    splash_pix = QtGui.QPixmap('img/fondo_pantalla_de_bienvenida.png')
    splash = QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.show()

    def login():
        splash.close()
        global login
        login = Login()
        login.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint | Qt.CustomizeWindowHint)
        login.show()

        def mousePressEvent(self, e):
            if e.button() == Qt.LeftButton:
                self.dragPosition = e.globalPos() - self.frameGeometry().topLeft()
                e.accept()

        def mouseMoveEvent(self, e):
            if e.button() == Qt.LeftButton:
                self.move(e.globalPos() - self.dragPosition)
                e.accept()

        def keyPressEvent(self, e):
            if e.key() == Qt.Key_Escape:
                self.close()

    QtCore.QTimer.singleShot(500, login)

    sys.exit(app.exec_())