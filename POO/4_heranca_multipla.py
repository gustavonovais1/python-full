class Animal:

    def andar(self):
        print("Estou andando como um animal")

    def correr(self):
        print("tou correndo")

    def pular(self):
        print("Estou pulando")

class Felino(Animal):

    def felino(self):
        print("Eu sou um felino")

class Canino():

    def canino(self):
        print("Eu sou um canino")

class Gato(Felino):

    def miar(self):
        print("Estou andando com um gato")

class Cachorro(Animal, Canino):

    def latir(self):
        print("Estou latindo")

x = Gato()
x.andar()

y = Cachorro()

y.canino()