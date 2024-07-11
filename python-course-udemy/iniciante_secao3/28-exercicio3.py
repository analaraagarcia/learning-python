''' 
exercicio
Peça ao usuário para digitar seu nome e a idade
Exiba:
    seu nome é {nome}
    seu nome invertido é {nome invertido}
    seu nome contém (ou não) espaços
    seu nome tem {n} letras
    a primeira letra do seu nome é {letra}
    a última letra do seu nome é {letra}
Se nada for digitado em nome ou idade exiba "Desculpe, você deixou campos vazios"
'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print(f'Seu nome tem {len(nome) - 1} letras') # não conta o espaço como letra
        print('Seu nome contém espaços')
    else:
        print(f'Seu nome tem {len(nome)} letras') # não tem espaço então conta as letras normalmente
        print('Seu nome não contém espaços')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios!')