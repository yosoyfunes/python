#!/usr/bin/python
# -*- coding: utf-8 -*-

# http://nullege.com/codes/show/src%40p%40y%40pyqt5-HEAD%40examples%40pyuic%40load_ui1.py/45/PyQt5.uic.loadUi/python

import sys
  
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
  
  
app = QApplication(sys.argv)
widget = loadUi('ejemplo.ui')
widget.show()
sys.exit(app.exec_())

