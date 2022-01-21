n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

cost = oil[0]
sum = 0
for i in range(n-1):
    if oil[i] < cost:
        cost = oil[i]
    sum += cost * road[i]
print(sum)
