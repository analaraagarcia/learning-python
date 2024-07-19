time = int(input())

hour = time // 3600

min = (time % 3600) // 60

sec = time % 60

print(f'{hour}:{min}:{sec}')