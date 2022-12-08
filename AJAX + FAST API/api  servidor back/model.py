from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine("sqlite:///sqlite.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    usuario = Column(String(50))
    email = Column(String(100))
    senha = Column(String(16))

class Tokens(Base):
    __tablename__ = "Tokens"
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('Pessoa.id'))
    token = Column(String(50))
    data = Column(DateTime, default=datetime.datetime.utcnow())

class Compra(Base):
    __tablename__ = "Compra"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(50))
    cidade = Column(String(60))
    estado = Column(String(2))
    cep = Column(String(10))

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    