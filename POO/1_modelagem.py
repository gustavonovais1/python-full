class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self):
        print(f"{self.nome} está logando no sistema")

p1 = Pessoas('Gustavo', 18, "123465764")
p2 = Pessoas('Matheus', 25, "121454578")

print(p1.nome)
p2.logar_sistema()