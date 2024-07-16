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
s1 = set() # vazio
s1 = {'Ana', 'Lara', 1, 2, 3} # com dados
print(s1)

# Sets são eficientes para remover valores duplicados de ireáveis
# eles não têm indexes
# eles não garantem ordem
# eles são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard