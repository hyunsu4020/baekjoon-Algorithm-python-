t = int(input())

sum = 0
prize = []
for _ in range(t):
    a, b, c = map(int, input().split())
    if a == b == c:
        sum = 10000 + a * 1000
    elif a == b or a == c:
        sum = 1000 + a * 100
    elif b == c:
        sum = 1000 + b * 100
    elif a != b != c:
        sum = max(a, b, c) * 100
    prize.append(sum)
print(max(prize))
