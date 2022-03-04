a, b, c = map(int, input().split())

sum = 0
if a == b == c:
    sum = 10000 + a*1000
elif a == b:
    sum = 1000 + a*100
elif a == c:
    sum = 1000 + a*100
elif b == c:
    sum = 1000 + b*100
else:
    sum = max(a, b, c)*100
print(sum)
