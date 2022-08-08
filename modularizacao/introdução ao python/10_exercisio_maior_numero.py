num1 = int(input("Digite o um numero: "))
num2 = int(input("Digite o um numero: "))
num3 = int(input("Digite o um numero: "))

if num1 > num2 and num1 > num3:
    print(f'O maior numero é {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior numero é {num2}')
elif num3 > num1 and num3 > num2:
    print(f'O maior numero é {num3}')