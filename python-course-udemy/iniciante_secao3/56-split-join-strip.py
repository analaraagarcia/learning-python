"""
split e join com list e str
split - divide uma string
join - une uma string
"""
frase = 'Olha só, que coisa interessante'
print(frase)

lista_frases = frase.split(', ')

lista_nova = []
for i, frase in enumerate(lista_frases):
    lista_nova.append(lista_frases[i].strip())

print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)