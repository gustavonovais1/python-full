from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import Pessoa

def RetornaSession():
    USUARIO = 'root'
    SENHA = '222545'
    HOST = 'localhost'
    BAMCO = 'python-full'
    PORT = '3306'

    CONECTION = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BAMCO}'

    engine = create_engine(CONECTION, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session = RetornaSession()

x = Pessoa(nome='Gustavo',
            usuario='gustavo',
            senha='1234')


y = Pessoa(nome='',
            usuario='gustavo',
            senha='1234')


session.add_all([x, y])
session.rollback()
session.commit()