"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável
"""

def  multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total

mult = multiply(2, 3, 6)
print(mult)


"""
Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar
"""

def even_odd(number):
    even = number % 2 == 0

    if even:
        return f'{number} is even.'

    return f'{number} is odd.'


print(even_odd(2))
print(even_odd(3))
print(even_odd(15))
print(even_odd(22))


