# __init__ sempre sera executado (Método construtor)
# self é um atributo de instancia
import re


class Pessoas:

    posui_olho = True
    posui_boca = True
    raca = "ser humano"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        "Metodo de instancia"
        print(f"{self.retorna_nome()} está logando no sistema")
    
    @classmethod
    def andar(cls):
        "Metodo de classe"
        cls.posui_boca = False

    @staticmethod
    def e_adulto(idade):
        if idade > 18:
            return True
        return False

# instancia da classe pessoas
p1 = Pessoas("Gustavo", 18)

# metodo de instancia
# print(p1.posui_olho)
# p1.andar()

# metodo de classe
print(Pessoas.posui_boca)
Pessoas.andar()
print(Pessoas.posui_boca)

print(Pessoas.e_adulto(10))