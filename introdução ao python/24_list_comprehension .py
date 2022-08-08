# Funcional 
'''x = [i for i in range(0, 10)]

print(x)

# Procedural
y = []
for i in range(0, 10):
    y.append(i)

print(y)

x = [input('Digite um nome: ') for i in range(0, 3)]

print(x)

# estrutura tridimencional
x = [[[ input() for j in range(0, 2)] for j in range(0, 2)] for i in range(0, 2)]

print(x)'''

x = [i for i in range(0, 10) if i >4]
print(x)

''' y = []
for i in range(0, 10):
    if i > 4:
        y.append(i)'''

x = [1, 2, 3]
y = x.copy()
y[0] = 2

print(hex(id(x)))
print(hex(id(y)))