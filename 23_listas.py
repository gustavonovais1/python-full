nomes = []

while True:
    nome = input('Digite um nome: ')
    if nome == '-1':
        break
    else:
        nomes.append(nome)

print(nomes)

nomes = ['Gustavo', 'pedro', 'matheus', 'joao' ,'joao' ,'joao']

# inserindo 
nomes.insert(1, 'kamilly')

# apagando o ultimo
nomes.pop()
# apagando pelo id
nomes.pop(1)
# inserindo pelo dado no final da lista
nomes.append("Lucas")
# removando pelo dado
nomes.remove('joao')
print(nomes.index('joao'))
print(nomes)

numeros = [2, 6, 4, 7, 10, 45, 65, 78, 40]
#cria uma nova lista (neste caso ordenada)
numeros_ord = sorted(numeros, reverse=True)
# ordenando a lista
nomes.sort()
print(numeros_ord)
# ordenando a lista em ordem decresente
numeros_ord.sort(reverse=False)
print(numeros_ord)

x = list(range(10, 29))
print(x)


for i , j in enumerate(x):
    print(f"i = {i} j = {j}")

# matriz e listas de listas
matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10], 
    [11, 12, 13, 14, 15]
]

for i in range(0, len(matriz)):
    for j in range(0 , len(matriz[i])):
        print(matriz[i][j])

