from fastAPI import FastAPI

app = FastAPI()

usuarios = [(1,'Gustavo','senha1'),(2, 'matheus', 'senha1')]

@app.post('/usuario')
def main(nome):
    for i in usuarios: 
        if i[1] == nome:
            return i

    return 'Não existe esse usuario'