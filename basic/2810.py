n = int(input())
seat = input()

cup = 0
if len(seat) == n:
    for i in range(n):
        if seat[i] == 'L':
            cup += 1
if cup == 0:
    print(n)
else:
    print(n - (cup // 2 - 1))
