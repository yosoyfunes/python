import re
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic

from buscarClientes import buscarClientes

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Clientes, Base, nombre_db

engine = create_engine('sqlite:///' + nombre_db)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Cliente(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("layout/validacion.ui", self)
        self.iniciar()

    def limpiarFormulario(self):
        self.nombre.setText(None)
        self.apellido.setText(None)
        self.telefono.setText(None)
        self.email.setText(None)

        self.nombre.setStyleSheet(None)
        self.email.setStyleSheet(None)

    def iniciar(self):
        self.limpiarFormulario()
        self.nombre.setEnabled(False)
        self.apellido.setEnabled(False)
        self.telefono.setEnabled(False)
        self.email.setEnabled(False)

        self.btnNuevo.setEnabled(True)
        self.btnEditar.setEnabled(False)
        self.btnGuardar.setEnabled(False)
        self.btnCancelar.setEnabled(False)
        self.btnBuscar.setEnabled(True)

        self.btnNuevo.clicked.connect(self.cargarNuevoCliente)
        self.btnGuardar.clicked.connect(self.validar_formulario)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnBuscar.clicked.connect(self.buscar)

    def cargarNuevoCliente(self):
        self.nombre.setEnabled(True)
        self.apellido.setEnabled(True)
        self.telefono.setEnabled(True)
        self.email.setEnabled(True)

        self.btnNuevo.setEnabled(False)
        self.btnEditar.setEnabled(False)
        self.btnGuardar.setEnabled(True)
        self.btnCancelar.setEnabled(True)
        self.btnBuscar.setEnabled(False)

        self.setTabOrder(self.nombre, self.apellido)
        self.setTabOrder(self.apellido, self.telefono)
        self.setTabOrder(self.telefono, self.email)

        self.setTabOrder(self.email, self.btnGuardar)
        self.setTabOrder(self.btnGuardar, self.btnCancelar)
        self.setTabOrder(self.btnCancelar, self.nombre)

        self.nombre.textChanged.connect(self.validar_nombre)
        self.email.textChanged.connect(self.validar_email)

    def validar_nombre(self):
        nombre = self.nombre.text()
        validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', nombre, re.I)
        if nombre == "":
            self.nombre.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.nombre.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.nombre.setStyleSheet("border: 1px solid green;")
            return True

    def validar_email(self):
        email = self.email.text()
        validar = re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email, re.I)
        if email == "":
            self.email.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.email.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.email.setStyleSheet("border: 1px solid green;")
            return True

    def validar_formulario(self, parent=None):
        if self.validar_nombre() and self.validar_email():
            nuevoCliente = Clientes(nombre=self.nombre.text(),
                apellido=self.apellido.text(),telefono=self.telefono.text(),email=self.email.text())
            session.add(nuevoCliente)
            session.commit()
            QMessageBox.information(self, "Formulario correcto", "Datos cargados correctamente", QMessageBox.Discard)
            self.iniciar()
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "Validación incorrecta", QMessageBox.Discard)
    
    def editar(self):
        pass
    def guardar(self):
        pass

    def cancelar(self):
        self.iniciar()
        self.close()

    def buscar(self):
        self.buscarCl = buscarClientes()
        self.buscarCl.exec_()