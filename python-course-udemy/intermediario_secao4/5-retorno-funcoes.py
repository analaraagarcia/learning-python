"""
Retorno de valores das funções (return)
"""
def soma(x, y):
    # print(x + y)
    if x > 1:
        return 1
    return x + y

# variavel = soma(1, 2)
# print(variavel)
# variavel = int('1')
# print(variavel)

soma1 = soma(2, 2)
soma2 = soma(4, 5)
soma3 = soma(3, 3)

print(soma1 + soma2 - soma3)
