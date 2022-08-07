import pickle 

"""
x = [1, 2, 3, 4]

string = pickle.dumps(x)
print(string)
print(pickle.loads(string))
"""

# Escrevendo(serealizando) em binario em um arquivo .pkl e trazendo a informação de volta com load
x = [1, 2, 3, 4]

arq = open("arquivo.pkl", "wb")
pickle.dump(x, arq)

arq = open("arquivo.pkl", "rb")
retornou = pickle.load(arq)

print(retornou)