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
            print(row.nombre + "  " +row.apellido)
            print('paso' + str(row.id))
            
            id = QTableWidgetItem(row.id)
            nombre = QTableWidgetItem(row.nombre)
            apellido = QTableWidgetItem(row.apellido)
            telefono = QTableWidgetItem(row.telefono)
            email = QTableWidgetItem(row.email)

            self.tabla.setItem(0, 0, id)
            self.tabla.setItem(0, 1, nombre)
            self.tabla.setItem(0, 2, apellido)
            self.tabla.setItem(0, 3, telefono)
            self.tabla.setItem(0, 4, email)

            self.tabla.insertRow(row.id)

            cont = cont + 1

#        id = QTableWidgetItem('2')
#        nombre = QTableWidgetItem('Pepe')
#        apellido = QTableWidgetItem('Argento')
#        telefono = QTableWidgetItem('1546730387')
#        email = QTableWidgetItem('matias@gmail.com')

#        self.tabla.setItem(1, 0, id)
#        self.tabla.setItem(1, 1, nombre)
#        self.tabla.setItem(1, 2, apellido)
#        self.tabla.setItem(1, 3, telefono)
#        self.tabla.setItem(1, 4, email)
