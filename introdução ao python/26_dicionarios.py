# Dicionario padrão
y = {'nome': 'Gustavo', 'idade': 18, 'cep':'154675'}
y['nome'] = 'Mathus'
"""print(x)"""

# Lista dentro de um dicionario
x = {'nomes': [], 'idade': 18}

x['nomes'].append('Gustavo')
x['nomes'].append('Matheus')  

"""print(x['nomes'][0])"""
# Dicionario dentro de lista

pessoas = [
    {'nome':'Gustavo', 'idade': 18,'altura': 167}, 
    {'nome':'Matheus', 'idade': 24,'altura': 175}, 
    {'nome':'Pedro', 'idade': 56,'altura': 161}
]

for pessoa in pessoas:
    print(pessoa['nome'])
# Criando chaves no dicionario

x = {'nome': 'Gustavo', 'idade': 18, 'cep':'154675'}

x["altura"] = 167
# ou 

x.update({"rua" : 'minha rua'})

print(x)

# acessando valores e chaves 

print(x.values())

print(x.keys())

print(x.items())

for i, j in y.items():
    print(f"i = {i} j = {j}")