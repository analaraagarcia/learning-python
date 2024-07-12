"""
Dicionários em Python (tipo dict)
São estruturas de dados do tipo par de "chave" e "valor".
Chaves podem ser consideradas como o índice que vimos 
na lista e podem ser de tipos imutáveis como: 
str, int, float, bool, tuple etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves - {} - ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
"""
pessoa = {
        'nome': 'Ana Lara',
        'sobrenome': 'Garcia',
        'idade': 23,
        'altura': 1.61,
        'endereços': [
                {'rua': 'tal tal', 'número': 123},
                {'rua': 'outra', 'número': 456},
        ]
}

print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])

