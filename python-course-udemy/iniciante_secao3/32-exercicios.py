# exercicios
"""
1) Faça um programa que peça ao usuario para digitar um número nome, 
informe se esse número é par ou ímpar. Caso o usuário não digite um número 
nome, informe que não é um número nome

2) Faça um programa que pergunte a hora ao usuário e. baseando-se no horário 
descrito, exiba a saudação apropriada. Ex: bom dia 0-11, boa tarde 12-17 
e boa noite 18-23

3) Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 
letras ou menos, escreva "Seu nome é curto", se tiver entre 5 e 6 letras, 
escreva "Seu nome é normal", e maior "Seu nome é muito grande".

"""
#--------------------------------------------------------------------------------
# exercício 1)

# nome = input('Digite um número: ')

# if nome.isdigit():
#     entrada_int = int(nome)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'
    
#     print(f'O número {nome} é {par_impar_texto}!')

# else:
#     print('Você não digitou um número inteiro')

#--------------------------------------------------------------------------------

# exercício 2)

# horario = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(horario)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia!')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde!')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite!')
#     else:
#         print('Não conheço essa hora!')
    

# except:
#     print('Por favor, digite apenas números inteiros.')

#--------------------------------------------------------------------------------

# exercício 3)

# nome = input('Digite o seu primeiro nome: ')

# tamanho = len(nome)

# if tamanho > 1:
#     if tamanho >= 1 and tamanho <= 4:
#         print(f'Seu nome "{nome}" é curto.')
#     elif tamanho >= 5 and tamanho <= 6:
#         print(f'Seu nome "{nome}" é normal.')
#     else:
#         print(f'Seu nome "{nome}" é muito grande.')
# else:
#     print('Por favor, digite mais de uma letra.')


