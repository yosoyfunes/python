import os.path as path

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
nombre_db = 'veterinaria.db'

class Clientes(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    apellido = Column(String(250))
    telefono = Column(String(250))
    email = Column(String(250))

    def __init__(self, nombre, apellido, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email


# if os.path.isfile(nombre_del_archivo):

engine = create_engine('sqlite:///' + nombre_db)

if path.exists(nombre_db):
    pass
else:
    Base.metadata.create_all(engine)
    print("paso por Base.metadata")
