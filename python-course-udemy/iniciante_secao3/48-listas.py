"""
Listas em Python
Tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
métodos úteis: 
    append: adiciona um item no final
    insert:adiciona um item no índice escolhido
    pop:remove do final ou do índice escolhido
    del: apaga um índice
    clear: limpa a lista
    extend: estende a lista
    +: concatena listas
create read update delete
criar ler alterar apagar
"""
#--------------------------------------------------------------

# string = 'ABCDE' # 5 caracteres (len)
# lista = [123, True, 'Ana Lara', 1.2]
# lista[2] = 'Maria' # altera na lista
# print(lista[2].upper(), type(lista[2]))
# print(lista, type(lista))

#--------------------------------------------------------------

# lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
# lista.append(50)
# lista.pop() # remove o último elemento
# lista.append(60)
# lista.append('BBB')
# ultimo_valor = lista.pop()
# print(lista, '\nRemovido:', ultimo_valor)

#--------------------------------------------------------------

# lista = [10, 20, 30, 40]
# lista.append('Ana')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# # lista.clear()
# lista.insert(0, 5)
# print(lista)

#--------------------------------------------------------------

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b) # extende a lista 'a' para a lista 'b', ou seja, "adiciona" a lista 'b' na 'a'
# print(lista_a)

#--------------------------------------------------------------

# lista_a = ['Luis', 'Ana', 1, True, 1.2]
# lista_b = lista_a.copy()

# lista_a[0] = 'Qualquer coisa'
# print(lista_a)
# print(lista_b)