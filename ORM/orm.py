from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# configuracion
# http://docs.sqlalchemy.org/en/rel_0_8/orm/tutorial.html#connecting
engine = create_engine('sqlite:///perctrl.db', echo=True)
Session = sessionmaker(bind=eng)

# creando una session 
# http://docs.sqlalchemy.org/en/rel_0_8/orm/tutorial.html#creating-a-session
session = Session()

# mapeando la tabla 'perctrl' a la clase Perctrl
# http://docs.sqlalchemy.org/en/rel_0_8/orm/tutorial.html#declare-a-mapping
Base = declarative_base()

class Perctrl(Base):
    __tablename__ = 'perctrl'

    perctrl_id = Column(Integer, primary_key=True)
    cp_empresa = Column(String)
    cp_ejercicio = Column(String)
    cp_item_numerator = Column(String)
    cp_periodo = Column(String)
    cp_libro = Column(String)
    cp_flag_abierto_cerrado = Column(String)

    def __init__(self, empresa, ejercicio, periodo, libro, item_numerator, flag_abierto_cerrado):
        self.cp_empresa = empresa
        self.cp_ejercicio = ejercicio
        self.cp_periodo = periodo
        self.cp_libro = libro
        self.cp_item_numerator = item_numerator
        self.cp_flag_abierto_cerrado = flag_abierto_cerrado

    def __repr__(self):
        return "<Soy una instancia de Perctrl('%s','%s', '%s', '%s'. '%s')>" % (self.cp_empresa, self.cp_ejercicio, self.cp_periodo, self.cp_libro, self.cp_flag_abierto_cerrado)


# Ejemplos
# 1
# crear una instancia de Perctrl
pc = Perctrl('bb', '2008', '07', 'A01', '1', 'A')
print pc.cp_empresa, pc.cp_ejercicio, pc.cp_periodo, pc.cp_libro, pc.cp_item_numerator, pc.cp_flag_abierto_cerrado
print pc
# agregamos el objeto, pero aun no impacta la db
session.add(pc)

# 2
# tomando de referencia el triggerx132001t, abrimos los libros para las condiciones dadas
empresa, ejercicio, periodo, flag = 'vv', '2009', '05', 'C'
session.query(Perctrl).filter_by(cp_empresa=empresa, cp_ejercicio=ejercicio, cp_periodo=periodo).\
    update({'cp_flag_abierto_cerrado': flag})


# para que los cambios impacten la db
session.commit()
# mas informacion sobre Session 
# https://sqlalchemy.readthedocs.org/en/rel_0_6/orm/session.html
session.close()

# revisar el trigger x132001t, que fue implementado usando sqlalchemy-orm