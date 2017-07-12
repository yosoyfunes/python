#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from layout.Qmain import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    main_window = Ui_MainWindow()
    main_window.setupUi(window)
    window.setWindowFlags(Qt.FramelessWindowHint | Qt.CustomizeWindowHint)
    window.show()

    sys.exit(app.exec_())