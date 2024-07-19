N = int(input())

years = N // 365
months = (N % 365) // 30
days = (N % 365) % 30

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')