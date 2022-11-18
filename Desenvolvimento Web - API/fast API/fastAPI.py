from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'Mensagem': 'Olá mundo'}

@app.get('/cadastro')
def cadastro():
    return {'Mensagem': 'Cadastro'}

@app.get('/login')
def login():
    return {'Mensagem': 'Login'}