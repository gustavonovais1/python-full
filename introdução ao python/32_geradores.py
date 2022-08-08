from pympler.asizeof import asizesof

# mostra a quantidade de memoria ran necessaria para armazenar determinado valor
print(asizesof([1, 2, 3]))
'''
def dobro(lista):
    lista_dobro = []
    for i in lista:
        lista_dobro.append(i*2)
    
    return lista_dobro

x = asizesof(dobro(range(0, 1000)))
print(x)

def dobro():
    yield 1 

print(type(dobro([1,2,3])))'''

# yield provem apenas o proximo valore necessario
def dobro(lista):
    for i in range(0, 1000):
        yield i

def dobro2(lista):
    lista2 = []
    for i in lista:
        lista2.append(i)
    return lista2

x = dobro(range(0, 10000))
y = dobro2(range(0, 10000))

print(asizesof(x))
print(asizesof(y))

print(next(x))
print(next(x))
print(next(x))

w = dobro(range(0, 100))

while True:
    try:
        print(next(w))
    except StopIteration:
        break