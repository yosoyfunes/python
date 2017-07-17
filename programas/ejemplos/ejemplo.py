#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QWidget, QPushButton, QDialog, QLabel
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.resize(300, 300)
        self.setWindowTitle("Cuadro de diálogo")
        self.etiqueta = QLabel(self)

        btn = QPushButton('SALIR', self)
        btn.clicked.connect(qApp.quit)


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        btn = QPushButton('PRESIONAR', self)
        btn.setToolTip('Presionar para abrir una segunda <b>Ventana</b> ')
        # btn.clicked.connect(QCoreApplication.instance().quit)
        btn.clicked.connect(self.change_text)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()
        self.dialogo = Dialogo()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle('Menubar')
        self.show()

    def change_text(self):
        print('Presionaste el boton')
        self.dialogo.exec_()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

