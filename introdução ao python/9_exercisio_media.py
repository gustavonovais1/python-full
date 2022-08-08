nota1 = float(input("Digite sua premeira nota "))
nota2 = float(input("Digite sua segunda nota "))
nota3 = float(input("Digite sua terceira nota "))
nota4 = float(input("Digite sua quarta nota "))


media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(f'APROVADO sua média foi {media}')
elif media >= 4:
    print(f'RECUPERAÇÃO sua média foi {media}')
else:
    print(f'REPROVADO sua média foi {media}')
