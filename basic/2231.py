n = int(input())

for i in range(1, n+1):
    a = list(map(int, str(i)))
    if i + sum(a) == n:
        print(i)
        break
    if i == n:
        print(0)
