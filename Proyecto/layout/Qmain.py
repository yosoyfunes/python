# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

# python -m PyQt5.uic.pyuic -o Qmain.py main.ui

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        MainWindow.setMinimumSize(QtCore.QSize(900, 650))
        MainWindow.setMaximumSize(QtCore.QSize(900, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/farmacia.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_nvo_clientes = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nvo_clientes.setGeometry(QtCore.QRect(20, 20, 90, 90))
        self.btn_nvo_clientes.setStyleSheet("QPushButton {\n"
"    border: 2px solid #6A6A6A;\n"
"    background-color: #FFF;\n"
"}")
        self.btn_nvo_clientes.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/Mclientes.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_nvo_clientes.setIcon(icon1)
        self.btn_nvo_clientes.setIconSize(QtCore.QSize(70, 70))
        self.btn_nvo_clientes.setObjectName("btn_nvo_clientes")
        self.btn_nva_mascota = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nva_mascota.setGeometry(QtCore.QRect(140, 20, 90, 90))
        self.btn_nva_mascota.setStyleSheet("QPushButton {\n"
"    border: 2px solid #6A6A6A;\n"
"    background-color: #FFF;\n"
"}")
        self.btn_nva_mascota.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/Mmascotas.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_nva_mascota.setIcon(icon2)
        self.btn_nva_mascota.setIconSize(QtCore.QSize(70, 70))
        self.btn_nva_mascota.setObjectName("btn_nva_mascota")
        self.btn_ver_turnos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ver_turnos.setGeometry(QtCore.QRect(260, 20, 90, 90))
        self.btn_ver_turnos.setStyleSheet("QPushButton {\n"
"    border: 2px solid #6A6A6A;\n"
"    background-color: #FFF;\n"
"}")
        self.btn_ver_turnos.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/Mturnos_2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ver_turnos.setIcon(icon3)
        self.btn_ver_turnos.setIconSize(QtCore.QSize(70, 70))
        self.btn_ver_turnos.setObjectName("btn_ver_turnos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuCleintes = QtWidgets.QMenu(self.menubar)
        self.menuCleintes.setObjectName("menuCleintes")
        self.menuMascotas = QtWidgets.QMenu(self.menubar)
        self.menuMascotas.setObjectName("menuMascotas")
        self.menuTurnos = QtWidgets.QMenu(self.menubar)
        self.menuTurnos.setObjectName("menuTurnos")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setCheckable(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/Ucancelar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon4)
        self.actionSalir.setIconVisibleInMenu(True)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCargar = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/Mclientes_2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCargar.setIcon(icon5)
        self.actionCargar.setObjectName("actionCargar")
        self.actionListar = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/MPrint.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionListar.setIcon(icon6)
        self.actionListar.setObjectName("actionListar")
        self.actionCargarMascotas = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img/Mmascotas_2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCargarMascotas.setIcon(icon7)
        self.actionCargarMascotas.setObjectName("actionCargarMascotas")
        self.actionListarMascotas = QtWidgets.QAction(MainWindow)
        self.actionListarMascotas.setIcon(icon6)
        self.actionListarMascotas.setObjectName("actionListarMascotas")
        self.actionCargarTurnos = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img/Mturnos.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCargarTurnos.setIcon(icon8)
        self.actionCargarTurnos.setObjectName("actionCargarTurnos")
        self.actionListarTurnos = QtWidgets.QAction(MainWindow)
        self.actionListarTurnos.setIcon(icon6)
        self.actionListarTurnos.setObjectName("actionListarTurnos")
        self.menuCleintes.addAction(self.actionCargar)
        self.menuCleintes.addAction(self.actionListar)
        self.menuMascotas.addAction(self.actionCargarMascotas)
        self.menuMascotas.addAction(self.actionListarMascotas)
        self.menuTurnos.addAction(self.actionCargarTurnos)
        self.menuTurnos.addAction(self.actionListarTurnos)
        self.menuAyuda.addAction(self.actionSalir)
        self.menubar.addAction(self.menuCleintes.menuAction())
        self.menubar.addAction(self.menuMascotas.menuAction())
        self.menubar.addAction(self.menuTurnos.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_nvo_clientes.setToolTip(_translate("MainWindow", "Cargar Clientes"))
        self.btn_nva_mascota.setToolTip(_translate("MainWindow", "Cargar Mascotas"))
        self.btn_ver_turnos.setToolTip(_translate("MainWindow", "Listar Turnos"))
        self.menuCleintes.setTitle(_translate("MainWindow", "Clientes"))
        self.menuMascotas.setTitle(_translate("MainWindow", "Mascotas"))
        self.menuTurnos.setTitle(_translate("MainWindow", "Turnos"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionSalir.setText(_translate("MainWindow", "Salir "))
        self.actionSalir.setIconText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionCargar.setText(_translate("MainWindow", "Cargar"))
        self.actionListar.setText(_translate("MainWindow", "Listar"))
        self.actionCargarMascotas.setText(_translate("MainWindow", "Cargar"))
        self.actionListarMascotas.setText(_translate("MainWindow", "Listar"))
        self.actionCargarTurnos.setText(_translate("MainWindow", "Cargar"))
        self.actionListarTurnos.setText(_translate("MainWindow", "Listar"))

