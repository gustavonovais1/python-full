# lambda: uma função anonima que pode ser atribuida a uma variável, que sempre retornar algo

x = lambda nome, idade: print(f'Nome = {nome}\nIdade = {idade}')

x("Gustavo", 18)

# função comun que chama uma função lambda
def teste():
    return lambda *idade: print(idade)

x = teste()

x(18, 20)