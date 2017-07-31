from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5 import uic

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.base import Clientes, Base, nombre_db, engine

# engine = create_engine('sqlite:///' + nombre_db)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class buscarClientes(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("layout/buscar.ui", self)
        self.line_cliente.textChanged.connect(self.mostrarDatos)

        self.tabla.clearContents()
        self.tabla.setColumnCount(5)
        self.tabla.setRowCount(1)
        self.tabla.setHorizontalHeaderLabels(['id', 'nombre', 'apellido', 'telefono', 'email'])

        # personas = session.query(Clientes).all()
        # user = session.query(Clientes).filter(Clientes.id == 1)

    def mostrarDatos(self):
    	self.tabla.clearContents()
    	# print(self.line_cliente.text())

    	contador = 0

    	dato = self.line_cliente.text()

    	msj = session.query(Clientes).filter(Clientes.nombre.like('%'+dato+'%'))
    	self.tabla.setRowCount(1)

    	for row in msj:
            id = QTableWidgetItem(str(contador))
            nombre = QTableWidgetItem(row.nombre)
            apellido = QTableWidgetItem(row.apellido)
            telefono = QTableWidgetItem(row.telefono)
            email = QTableWidgetItem(row.email)

            self.tabla.setItem(contador, 0, id)
            self.tabla.setItem(contador, 1, nombre)
            self.tabla.setItem(contador, 2, apellido)
            self.tabla.setItem(contador, 3, telefono)
            self.tabla.setItem(contador, 4, email)

            self.tabla.insertRow(row.id)

            contador = contador + 1
