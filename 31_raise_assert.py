# raise forsa a chamada de uma exessão

def soma(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError("Essa função não soma números negativos!")
    return n1 + n2

print(soma(1, 2))

# assert for que uma afirmação seja verdade, caso contrrio tras uma ecessão
x =-1
assert x > 0, "x é menor que 0"