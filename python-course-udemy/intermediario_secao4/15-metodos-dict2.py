"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""

p1 = {
    'nome': 'Ana',
    'sobrenome': 'Bernardinello'
}

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'novo valor',
#     'idade': 23,
# })
# p1.update(nome='novo valor', idade=23)

tupla = (('nome', 'novo valor'), ('idade', 23))
lista = [['nome', 'novo valor'], ['idade', 23]]

p1.update(lista)
print(p1)