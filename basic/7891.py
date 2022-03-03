t = int(input())

sum = 0
for _ in range(t):
    a, b = map(int, input().split())
    sum = a + b
    print(sum)
