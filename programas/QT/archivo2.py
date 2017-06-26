#!/usr/bin/python
# -*- coding: utf-8 -*-

# http://nullege.com/codes/show/src%40p%40y%40pyqt5-HEAD%40examples%40pyuic%40load_ui1.py/45/PyQt5.uic.loadUi/python

import sys
  
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProyectoFinal(QWidget):
    def setupUi(self, ProyectoFinal):
        ProyectoFinal.setObjectName("ProyectoFinal")
        ProyectoFinal.resize(650, 520)
        ProyectoFinal.setMinimumSize(QtCore.QSize(650, 520))
        ProyectoFinal.setMaximumSize(QtCore.QSize(650, 520))
        self.centralwidget = QtWidgets.QWidget(ProyectoFinal)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 631, 271))
        self.pushButton.setObjectName("pushButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(170, 290, 321, 191))
        self.calendarWidget.setObjectName("calendarWidget")
        # self.calendarWidget.setObjectName(2017, 01, 01) # Set Fecha Incial
        ProyectoFinal.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(ProyectoFinal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 19))
        self.menubar.setObjectName("menubar")
        self.menuALGO = QtWidgets.QMenu(self.menubar)
        self.menuALGO.setObjectName("menuALGO")
        self.menuCATEGORIAS = QtWidgets.QMenu(self.menubar)
        self.menuCATEGORIAS.setObjectName("menuCATEGORIAS")
        self.menuTURNOS = QtWidgets.QMenu(self.menubar)
        self.menuTURNOS.setObjectName("menuTURNOS")
        self.menuAYUDA = QtWidgets.QMenu(self.menubar)
        self.menuAYUDA.setObjectName("menuAYUDA")
        self.menuINFORMES = QtWidgets.QMenu(self.menubar)
        self.menuINFORMES.setObjectName("menuINFORMES")
        ProyectoFinal.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(ProyectoFinal)
        self.statusbar.setObjectName("statusbar")
        ProyectoFinal.setStatusBar(self.statusbar)
        
        self.actionNUEVO = QtWidgets.QAction(ProyectoFinal)
        self.actionNUEVO.setObjectName("actionNUEVO")
        self.actionNUEVO_2 = QtWidgets.QAction(ProyectoFinal)
        self.actionNUEVO_2.setObjectName("actionNUEVO_2")
        self.actionALTA_DE_TURNO = QtWidgets.QAction(ProyectoFinal)
        self.actionALTA_DE_TURNO.setObjectName("actionALTA_DE_TURNO")
        self.actionACERCA_DE = QtWidgets.QAction(ProyectoFinal)
        self.actionACERCA_DE.setObjectName("actionACERCA_DE")
        self.actionLISTADO = QtWidgets.QAction(ProyectoFinal)
        self.actionLISTADO.setObjectName("actionLISTADO")
        self.actionCLIENTES = QtWidgets.QAction(ProyectoFinal)
        self.actionCLIENTES.setObjectName("actionCLIENTES")
        self.actionCATEGORIAS = QtWidgets.QAction(ProyectoFinal)
        self.actionCATEGORIAS.setObjectName("actionCATEGORIAS")
        self.actionTURNOS = QtWidgets.QAction(ProyectoFinal)
        self.actionTURNOS.setObjectName("actionTURNOS")
        self.menuALGO.addAction(self.actionNUEVO)
        self.menuCATEGORIAS.addAction(self.actionNUEVO_2)
        self.menuTURNOS.addAction(self.actionALTA_DE_TURNO)
        self.menuAYUDA.addAction(self.actionACERCA_DE)
        self.menuINFORMES.addAction(self.actionCLIENTES)
        self.menuINFORMES.addAction(self.actionCATEGORIAS)
        self.menuINFORMES.addAction(self.actionTURNOS)
        self.menubar.addAction(self.menuALGO.menuAction())
        self.menubar.addAction(self.menuCATEGORIAS.menuAction())
        self.menubar.addAction(self.menuTURNOS.menuAction())
        self.menubar.addAction(self.menuINFORMES.menuAction())
        self.menubar.addAction(self.menuAYUDA.menuAction())

        self.retranslateUi(ProyectoFinal)
        QtCore.QMetaObject.connectSlotsByName(ProyectoFinal)

    def retranslateUi(self, ProyectoFinal):
        _translate = QtCore.QCoreApplication.translate
        ProyectoFinal.setWindowTitle(_translate("ProyectoFinal", "MainWindow"))
        self.pushButton.setText(_translate("ProyectoFinal", "ACEPTAR"))
        self.menuALGO.setTitle(_translate("ProyectoFinal", "CLIENTES"))
        self.menuCATEGORIAS.setTitle(_translate("ProyectoFinal", "CATEGORIAS"))
        self.menuTURNOS.setTitle(_translate("ProyectoFinal", "TURNOS"))
        self.menuAYUDA.setTitle(_translate("ProyectoFinal", "AYUDA"))
        self.menuINFORMES.setTitle(_translate("ProyectoFinal", "INFORMES"))
        self.actionNUEVO.setText(_translate("ProyectoFinal", "NUEVO"))
        self.actionNUEVO_2.setText(_translate("ProyectoFinal", "NUEVO"))
        self.actionALTA_DE_TURNO.setText(_translate("ProyectoFinal", "ALTA DE TURNO"))
        self.actionACERCA_DE.setText(_translate("ProyectoFinal", "ACERCA DE..."))
        self.actionLISTADO.setText(_translate("ProyectoFinal", "LISTADO"))
        self.actionCLIENTES.setText(_translate("ProyectoFinal", "CLIENTES"))
        self.actionCATEGORIAS.setText(_translate("ProyectoFinal", "CATEGORIAS"))
        self.actionTURNOS.setText(_translate("ProyectoFinal", "TURNOS"))
  
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
	widget = Ui_ProyectoFinal()
	widget.show()
	sys.exit(app.exec_())