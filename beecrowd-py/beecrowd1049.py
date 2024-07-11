first = input()
second = input()
third = input()


if first == 'vertebrado':
    if second == 'ave':
        if third == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    
    elif second == 'mamifero':
        if third == 'onivoro':
            print('homem')
        else:
            print('vaca')

elif first == 'invertebrado':
    if second == 'inseto':
        if third == 'hematofago':
            print('pulga')
        else:
            print('lagarta')

    elif second == 'anelideo':
        if third == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
