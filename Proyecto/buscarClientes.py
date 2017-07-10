from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5 import uic

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Clientes, Base, nombre_db

engine = create_engine('sqlite:///' + nombre_db)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class buscarClientes(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("layout/buscar.ui", self)

        self.tabla.clearContents()

        self.tabla.setColumnCount(5)
        self.tabla.setRowCount(1)
        self.tabla.setHorizontalHeaderLabels(['id', 'nombre', 'apellido', 'telefono', 'email'])

        # self.tabla.insertRow(1)

        personas = session.query(Clientes).all()
        cont = 0
        for row in personas:
            print(row.id)
            
            id = QTableWidgetItem(str(cont))
            nombre = QTableWidgetItem(row.nombre)
            apellido = QTableWidgetItem(row.apellido)
            telefono = QTableWidgetItem(row.telefono)
            email = QTableWidgetItem(row.email)

            self.tabla.setItem(cont, 0, id)
            self.tabla.setItem(cont, 1, nombre)
            self.tabla.setItem(cont, 2, apellido)
            self.tabla.setItem(cont, 3, telefono)
            self.tabla.setItem(cont, 4, email)

            self.tabla.insertRow(row.id)

            cont = cont + 1