n = list(map(int, input().split()))

num = 0
sum = 0
for i in n:
    num = i**2
    sum += num
print(sum%10)
