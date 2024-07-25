A, B, C, D = map(float, input().split())

media = (A * 2 + B * 3 + C * 4 + D * 1) / 10.0

print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')

elif media < 5.0:
    print('Aluno reprovado.')

elif media >= 5.0 and media <= 6.9:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    media2 = (media + exame) / 2.0
    if media2 >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    
    print(f'Media final: {media2:.1f}')