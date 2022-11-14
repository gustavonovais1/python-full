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

x = session.query(Pessoa).all()

for i in x:
    print(i.id)

x = session.query(Pessoa).filter(Pessoa.nome == 'Gustavo')
for i in x:
    print(i.id) 

x = session.query(Pessoa).filter_by(nome = 'Gustavo', id = '1')
for i in x:
    print(i.id) 