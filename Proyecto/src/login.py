#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QSplashScreen, QDesktopWidget
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5 import uic

from src.Qmain import Ui_MainWindow

# class Ui_Login(QDialog):
# 	def __init__(self):
# 		QDialog.__init__(self)

class Ui_Login(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		uic.loadUi("layout/login.ui", self)
		self.aceptar.clicked.connect(self.btn_aceptar)
		self.cancelar.clicked.connect(self.salir)

	def btn_aceptar(self):
		global window
		window = QMainWindow()
		main_window = Ui_MainWindow()
		main_window.setupUi(window)
		window.show()
		self.close()
#		login.close()

	def salir(self):
		self.close()

def Ui_Bienvenida():
	splash_pix = QtGui.QPixmap('img/fondo_pantalla_de_bienvenida.png')
	splash = QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
	splash.show()

	def Bienvenida():
		splash.close()

	QtCore.QTimer.singleShot(500, Bienvenida)