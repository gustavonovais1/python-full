from fastAPI import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: Optional(str)
    senha: str

lista = [Usuario(id=1, nome='Gustavo', senha='1234'),
        Usuario(id=2, nome='Matheus', senha='12345'),
        Usuario(id=3, nome='Pedro', senha='123456')
]

@app.post('/usuario')
def main(usuario: Usuario):
    lista.append(usuario)
    return 'Usuário cadastrado.'

@app.get('/usuarioListar')
def main():
    return lista