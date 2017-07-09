import sys, re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic
from PyQt5.uic import loadUi

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
		
	def validar_formulario(self):
		if self.validar_nombre() and self.validar_email():
			QMessageBox.information(self, "Formulario correcto", "Validación correcta", QMessageBox.Discard)
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
		pass

