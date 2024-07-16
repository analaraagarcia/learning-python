"""
Sets - conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno
"""

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Lara')
# s1 = set() # vazio
# s1 = {'Ana', 'Lara', 1, 2, 3} # com dados
# print(s1)

# Sets são eficientes para remover valores duplicados de ireáveis
# eles não têm indexes
# eles não garantem ordem
# eles são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1, 2, 3}
# print(3 in s1)

# for numero in s1:
#     print(numero)

# Métodos úteis:
# add, update, clear, discard
# s1 = set()
# s1.add('Ana')
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# # s1.clear()
# print(s1)
# s1.discard('Olá mundo')
# print(s1)
# s1.discard('Ana')
# print(s1)

# Operadores úteis:
# união |
# iintersecção &
# diferença - itens presentes apenas no set da esquerda
# diferenã simétrica ^- itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
print(s3)

s3 = s1 - s2
print(s3)

s3 = s2 - s1
print(s3)

s3 = s1 ^ s2
print(s3)

