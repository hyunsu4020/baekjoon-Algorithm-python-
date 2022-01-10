n, k = map(int, input().split())

a = []
for i in range(n):
    a.append(int(input()))

coin = 0
for i in reversed(range(n)):
    coin += k // a[i]
    k = k % a[i]
print(coin)
