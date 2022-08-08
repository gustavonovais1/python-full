n1 = eval(input("Digite um número: "))
n2 = eval(input("Digite um número: "))

try:
    print(n1/n2)
except:
    print("Não foi possível fazer a divisão")
finally:
    print("Finalizado:!")

# tratamento de exessão diacordo com o erro
try:
    n1 = eval(input("Digite um número: "))
    print(5/n1)
except ZeroDivisionError:
    print("Não é possível dividir um número por zero!")
except NameError:
    print("Digite um número inteiro!")

# verificação de ecessaão
try:
    n1 = eval(input("Digite um número: "))
    print(5/n1)
except Exception as e:
    print(e)