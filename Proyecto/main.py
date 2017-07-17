#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python -m PyQt5.uic.pyuic -o Qmain.py main.ui

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtWidgets import QDialog, QSplashScreen, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtCore

# from src.login import Ui_Login, Ui_Bienvenida
from src.Qmain import Ui_MainWindow

def Ui_Bienvenida():
	splash_pix = QtGui.QPixmap('img/fondo_pantalla_de_bienvenida.png')
	splash = QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
	splash.show()

	def Bienvenida():
		splash.close()
		Ingresar()

	QtCore.QTimer.singleShot(1000, Bienvenida)

def Ingresar():
	window.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	window = QMainWindow()
	main_window = Ui_MainWindow()
	main_window.setupUi(window)
#	window.show()

	Ui_Bienvenida()
	sys.exit(app.exec_())