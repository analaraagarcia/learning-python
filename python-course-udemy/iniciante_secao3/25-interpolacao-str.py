""" 
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal
"""
nome = 'Ana'
preco = 350.5048723
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %X' % (15, 15))