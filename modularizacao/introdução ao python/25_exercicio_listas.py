# receba 10 valores e mostre a soma de todos eles

x = [int(input('Digite um numero: ')) for i in range(0, 10)]

soma  = 0 
for i in x:
    soma += 1

print(soma)