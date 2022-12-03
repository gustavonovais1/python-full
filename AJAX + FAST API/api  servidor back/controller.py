from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Pessoa, Tokens
from secrets import token_hex
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from hashlib import sha256

app = FastAPI()

def conectaBanco():
    engine = create_engine("sqlite:///sqlite.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/cadastro")
def cadastro(user: str, email: str, senha: str):
    if len(senha) < 6:
        return {'erro': 1}

    senha = sha256(senha.encode()).hexdigest()
    session = conectaBanco()
    usuario = session.query(Pessoa).filter_by(email=email, senha=senha).all()

    if len(usuario) > 0:
        return {'erro': 2}

    try:
        novo_usuario = Pessoa(
            usuario = user,
            email = email,
            senha = senha
        )

        session.add(novo_usuario)
        session.commit()
        return {'erro': 0}
    except Exception as e:
        return {'erro': 3, 'erro': e}

@app.post("/login")
def login(user: str, senha: str):
    
    senha = sha256(senha.encode()).hexdigest()
    session = conectaBanco()
    usuario = session.query(Pessoa).filter_by(usuario=user, senha=senha).all()

    if len(usuario) > 0:
        while True:
            token = token_hex(50)
            tokenExiste = session.query(Tokens).filter_by(token=token).all()
            if len(tokenExiste) == 0:
                pessoaExiste = session.query(Tokens).filter_by(id_pessoa=usuario[0].id).all()
                if len(pessoaExiste) == 0:
                    novoToken = Tokens(id_pessoa=usuario[0].id, token=token)
                    session.add(novoToken)
                elif len(pessoaExiste) > 0:
                    pessoaExiste[0].token = token
                
                session.commit()
                return {'erro': 4}
            break

        session.commit()

    elif len(usuario) == 0:
        return {'erro': 5}

if __name__ == "__main__":
    uvicorn.run('controller:app', port=5000, reload=True, access_log=False)