m = int(input())
n = int(input())

decimal = []
for i in range(m, n+1):
    for j in range(2, i+1):
        if j == i:
            decimal.append(i)
        if i % j == 0:
            break
if decimal:
    print(sum(decimal))
    print(decimal[0])
else:
    print(-1)
