class Pessoa:

    def falar(self):
        print("Estou falando")

    def andar(self):
        print("Estou andando")

class Vendedor:

    def vender(self):
        print("Estou vendendo")


class Cliente(Pessoa):

    def comprar(self):
        print("Estou comprando")