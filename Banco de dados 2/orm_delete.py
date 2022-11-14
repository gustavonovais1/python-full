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

x = session.query(Pessoa).filter(Pessoa.id == 2).delete()

session.commit()
# OU 
x = session.query(Pessoa).filter(Pessoa.id == 3).one()

session.delete(x)

session.commit()