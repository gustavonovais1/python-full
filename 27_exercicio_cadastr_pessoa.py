pessoas = {'nome':[], 'idade':[], 'altura':[]}

while True:
    opcao = int(input("Digite 1 para cadastrar uma pessoa ou 2 para sair: "))
    if opcao == 1:
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))

        pessoas["nome"].append(nome)
        pessoas["idade"].append(idade)
        pessoas["altura"].append(altura)

        print(pessoas)
    else:
        break

