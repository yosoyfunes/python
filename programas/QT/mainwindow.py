#!/usr/bin/python
# -*- coding: utf-8 -*-

# Convierte temperaturas
# www.pythondiario.com

import sys
from PyQt4 import QtCore, QtGui, uic

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("ejemplo.ui")[0]

class MyAplicacion(QtGui.QMainWindow, form_class):
 def __init__(self, parent=None):
  QtGui.QMainWindow.__init__(self, parent)
  self.setupUi(self)

app = QtGui.QApplication(sys.argv)
MyWindow = MyAplicacion(None)
MyWindow.show()
app.exec_()

