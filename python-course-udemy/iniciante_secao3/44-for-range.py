"""
for + range
range -> range(start, stop, step)
o step é a quantidade de numeros que se deseja pular
então por ex: se eu colocar range(0, 100, 2) ele irá retornar todos os múltiplos de 2 dee 0 a 100
"""
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)

