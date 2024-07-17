A, B, C = map(int, input().split())

MaiorAB = (A + B + abs(A - B)) / 2
maior = int(MaiorAB)

if maior > C:
    print(f'{maior} eh o maior')
else:
    print(f'{C} eh o maior')