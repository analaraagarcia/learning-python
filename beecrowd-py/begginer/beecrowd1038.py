A, B = map(int, input().split())

if A == 1:
    C = 4 * B
elif A == 2:
    C = 4.5 * B
elif A == 3:
    C = 5 * B
elif A == 4:
    C = 2 * B
else:
    C = 1.5 * B

print(f'Total: R$ {C:.2f}')