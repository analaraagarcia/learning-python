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
pessoa = {
        'nome': 'Ana Lara',
        'sobrenome': 'Alves Garcia',
        # 'idade': 900,
}

pessoa.setdefault('idade', None)
print(pessoa['idade'])

print(len(pessoa))

# mostra as chaves ('nome', 'sobrenome')
print(list(pessoa.keys()))

# mostra o conteúdo das chave (valor) ('Ana Lara', 'Garcia')
print(list(pessoa.values()))

# mostra a chave e o valor
print(list(pessoa.items()))

for valor in pessoa.values():
    print(valor)