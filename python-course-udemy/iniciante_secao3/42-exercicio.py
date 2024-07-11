# qual letra apareceu mais vezes na frase?

frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'

i = 0
apareceu_mais = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    contador = frase.count(letra_atual)

    if apareceu_mais < contador:
        apareceu_mais = contador
        letra_apareceu_mais = letra_atual

    print(letra_atual, contador)
    i += 1

print('A letra que apareceu mais vezes foi ' f'{letra_apareceu_mais}, que apareceu ' f'{apareceu_mais} vezes.')
