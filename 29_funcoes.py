# Função comun
from re import X
from numpy import arange


def minha_funcao():
    soma = 0
    for i in range(1, 101):
        soma += i
    print(soma)

minha_funcao()

# função com argumentos

def soma_numeros(n1, n2):
    print(n1 + n2)

soma_numeros(5, 7)
# Ou sem manter a ordem expecificando os valores
soma_numeros(n2 =7, n1 =5)

# função com argumentos indeterminados que empacota em uma tupla
def Args(*args):
    print(args)

Args(1, 2 ,4, 5, 4)

# função com argumentos indeterminados que empacota em um dicionario

def kwargs(**kwargs):
    x = kwargs.get("teste4")
    if x:
        print("Foi passado")
    else: 
        print("Não foi passado")

kwargs(teste1 = 1, teste2 = 2, teste3 = 3)

# retonrando valores de funções 

def soma_valores(n1, n2):
    soma = n1 + n2
    return soma, n1, n2

soma, n1, n2  = soma_valores(1, 2)
print(n1)