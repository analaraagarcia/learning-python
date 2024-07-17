cod1, num1, value1 = map(float, input().split())
cod2, num2, value2 = map(float, input().split())

total = num1 * value1 + num2 * value2

print(f'VALOR A PAGAR: R$ {total:.2f}')
