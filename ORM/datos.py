# -- coding: utf-8 --

from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Autor, Etiqueta, Libro

# conexion
engine = create_engine('sqlite:///libros.db', echo=True)
# sesion
Session = sessionmaker(bind=engine)
session = Session()

# insertamos autores
autor_1 = Autor('Patrick Rothfuss')
autor_2 = Autor('Fred Saberhagen')

lista_autores = (autor_1, autor_2)
session.add_all(lista_autores)
session.commit()

# insertamos etiquetas
etiqueta_1 = Etiqueta('aventuras')
session.add(etiqueta_1)

# insertamos libros
libro_1 = Libro('El nombre del fuego', date(2009, 5, 30), '978-8401337208')
libro_1.etiquetas.append(etiqueta_1)
libro_1.autores.append(autor_1)


session.add(libro_1)
session.commit()

# realizando una consulta
libro = session.query(Libro).filter(Libro.isbn=='978-8401337208').first()
print libro

# alterando uno de los atributos
libro.titulo = 'El nombre del viento'
session.commit()

print libro