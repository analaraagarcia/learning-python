# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Ana Lara'
pessoa['sobrenome'] = 'Bernardinello'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa[chave])

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])