name = input()
salary = float(input())
sold_in_month = float(input())

TOTAL = salary + (0.15 * sold_in_month)

print(f'TOTAL = R$ {TOTAL:.2f}')