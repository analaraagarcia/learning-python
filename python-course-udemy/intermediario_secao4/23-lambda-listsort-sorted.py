lista = [
    {'nome': 'Luis', 'sobrenome': 'de Angelo'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Ana', 'sobrenome': 'Garcia'},
]

# def ordena(item):
#     return item['nome']     ##checa o que estiver em 'nome' e ordena

# lista.sort(key=ordena)
# lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)