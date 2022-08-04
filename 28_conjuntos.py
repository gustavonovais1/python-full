# não permite repetições
x = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(x)
x = set(x)
print(x)

x = {1, 2, 3, 5}
y = {5, 6, 7, 8, 9, 10}
# uni os dois conjuntos 
t = x.union(y)

print(t)
# mostra o que os dois conjuntos tem em comum
t = x.intersection(y)

print(t)

# mostra o que tem de diferente do x conjunto m em relação ao conjunto y
t = x.difference(y)

print(t)

# forma um novo conjunto com todos os valores exeto o s valores que se repetm nos dois conjuntos
t = x.symmetric_difference(y)

print(t)