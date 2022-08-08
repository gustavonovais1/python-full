LOGIN = 'gustavo'
SENHA = '123'

while True:

    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    if login == LOGIN and senha == senha:
        print('Logado com sucesso')
        break
    else:
        print('Usuário ou senha inválidos')