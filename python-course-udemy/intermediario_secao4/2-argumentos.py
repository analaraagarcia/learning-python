"""
Argumentos nomeados e não nomeados em funções
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    print(f'{x = }; {y = }; {z = }', '|', 'x + y + z = ', x + y + z)

# não nomeado (deve ser na ordem que está na função)
soma(1, 2, 3)

# nomeado (pode colocar em qualquer ordem)
soma(y=2, z=3, x=1)

print(1, 2, 3, sep='-')