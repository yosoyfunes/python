import sys, re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic
from PyQt5.uic import loadUi

class Cliente(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("layout/validacion.ui", self)
		self.nombre.textChanged.connect(self.validar_nombre)
		self.email.textChanged.connect(self.validar_email)
		self.boton.clicked.connect(self.validar_formulario)
		self.volver.clicked.connect(self.close)
		
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