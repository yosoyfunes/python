# -- coding: utf-8 --

# https://alexanderae.com/sqlalchemy-orm-para-python-1.html

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///veterinaria.db', echo=True)
Base = declarative_base()

class Clientes(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), index=True, nullable=False)
    apellido = Column(String(50))
    telefono = Column(String(100))
    email = Column(String(100))

    def __init__(self, nombre, apellido, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    def __init__(self, nombre):
        self.nombre = nombre

class Mascotas(Base):
    __tablename__ = 'mascotas'
    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer)
    nombre = Column(String(120), nullable=False)
    edad = Column(String(120))

    def __init__(self, nombre):
        self.nombre = nombre

class Turnos(Base):
    __tablename__ = 'turnos'
    id = Column(Integer, primary_key=True)
    id_mascota = Column(Integer)
    id_cliente = Column(Integer)
    fecha = Column(Date)

    def __init__(self, id):
        self.id = id

Base.metadata.create_all(engine)