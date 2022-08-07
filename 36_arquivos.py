"""# w para escrever a para adicionar e r para ler 

arquivo = open("pessoas.txt", "a")

x = 0
while True:
    if x >= 2:
        break
    arquivo.write(input("Digite o nome da pessoa: ") + " " + input("Digite a idade: ") + "\n")
    x += 1

# Ler o arquivo

arquivo = open("pessoas.txt", "r")
resultado = arquivo.read()

print(resultado)"""

# with forma mais usual de abrir um arquivo

with open('pessoas.txt', 'r') as arq:
    x = arq.read()
    print(x)