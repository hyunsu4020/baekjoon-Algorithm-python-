station = []
sum = 0
for i in range(4):
    a, b = map(int, input().split())
    sum += b
    sum -= a
    station.append(sum)
print(max(station))
