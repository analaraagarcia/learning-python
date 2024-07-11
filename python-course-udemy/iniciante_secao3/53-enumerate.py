"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luis']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome)