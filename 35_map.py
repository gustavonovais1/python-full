x = [i for i in range(12, 26)]

# map faz uma alteração em uma listas (neste caso diacordo com uma condição)
x = list(map(lambda x: 10 if x < 18 else(x) ,x))

print(x)