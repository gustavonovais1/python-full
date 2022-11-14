from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
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

x = session.query(Pessoa).filter(or_(Pessoa.nome == 'Gustavo', Pessoa.usuario == 'joao')).all()

for i in x:
    print(i.id)